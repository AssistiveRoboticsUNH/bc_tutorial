import numpy as np 
import time 
import numpy as np
import torch
import torch.nn as nn
import time
import gym 
import pickle 
from replay_memory import Memory
import argparse
import torch.nn.functional as F
from torch.distributions import Normal
from torch.distributions.transformed_distribution import TransformedDistribution
from torch.distributions.transforms import TanhTransform

EPS = 1e-7

class MLP(nn.Module):
    def __init__(self, ac_dim, ob_dim, size=54):
        super().__init__()
        self.mlp = nn.ModuleList()
        self.mlp.append(nn.Linear(ob_dim, size))
        self.mlp.append(nn.Tanh())

        self.mlp.append(nn.Linear(size, size))
        self.mlp.append(nn.Tanh()) 
        
    def forward(self, x):
        for layer in self.mlp:
            x = layer(x)
        return x 
    

class Actor(MLP):
    def __init__(self, action_dim, ob_dim, size=54):
        # super().__init__() 
        super(Actor, self).__init__(action_dim, ob_dim, size)
        self.mlp.append(nn.Linear(size, action_dim)) 

    def forward(self, x):
        for layer in self.mlp:
            x = layer(x)
        return x
    
    def get_action(self, x):
        return self.forward(x)

    
class Actor_D(MLP):
    def __init__(self, action_dim, ob_dim, size=54):
        # super(Actor, self).__init__()
        super(Actor_D, self).__init__(action_dim, ob_dim, size)
        
        self.mu_head = nn.Linear(size, action_dim)
        self.sigma_head = nn.Linear(size, action_dim)

    def _get_outputs(self, x):
        for layer in self.mlp:
            x = layer(x) 
        mu = self.mu_head(x)
        # mu = torch.clip(mu, MEAN_MIN, MEAN_MAX)
        log_sigma = self.sigma_head(x)
        # log_sigma = torch.clip(log_sigma, LOG_STD_MIN, LOG_STD_MAX)
        sigma = torch.exp(log_sigma)

        ndist=Normal(mu, sigma)
        a_distribution = TransformedDistribution(
            ndist, TanhTransform(cache_size=1)
        )
        a_tanh_mode = torch.tanh(mu)
        # return a_distribution, a_tanh_mode
        return ndist, a_tanh_mode
    
    def get_mean(self, x):
        for layer in self.mlp:
            x = layer(x)
        
        mu = self.mu_head(x)
        return mu
    
    def get_action(self, x, deterministic=False):
        a_dist, a_tanh_mode = self._get_outputs(x)
        if deterministic:
            action = a_tanh_mode
        else:
            action = a_dist.rsample()
        return action

    def forward(self, state):
        a_dist, a_tanh_mode = self._get_outputs(state)
        action = a_dist.rsample()
        logp_pi = a_dist.log_prob(action).sum(axis=-1)
        return action, logp_pi, a_tanh_mode

    def get_log_density(self, state, action):
        a_dist, _ = self._get_outputs(state)
        action_clip = torch.clip(action, -1. + EPS, 1. - EPS)
        logp_action = a_dist.log_prob(action_clip)
        return logp_action
    
    # def get_action_probability(self, state, action):
    #     a_dist, _ = self._get_outputs(state)
    #     action_clip = torch.clip(action, -1. + EPS, 1. - EPS)
    #     logp_action = a_dist.log_prob(action_clip)
    #     return logp_action