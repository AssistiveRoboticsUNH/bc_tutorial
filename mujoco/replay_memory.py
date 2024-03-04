import numpy as np 

class Memory: 
    def __init__(self, maxlen=1_000_000):  
        self.states=None
        self.actions=None
        self.ids=None
        self.maxlen=maxlen
        
    def add_data(self, states, actions,ids):
        """
        add N s,a,r
        """
        if self.states is None: #first time
            self.states =states[-self.maxlen:] 
            self.actions=actions[-self.maxlen:]
            self.ids=ids[-self.maxlen:]
        else:
            self.states = np.concatenate([self.states, states])[-self.maxlen:] 
            self.actions = np.concatenate([self.actions, actions])[-self.maxlen:] 
            self.ids = np.concatenate([self.ids, ids])[-self.maxlen:]
        
    def sample_batch(self, batch_size):
        indices = np.random.permutation(len(self))[:batch_size]
        batch_states=self.states[indices] 
        batch_actions=self.actions[indices]
        batch_ids=self.ids[indices] 
        return batch_states, batch_actions, batch_ids
        
    def __len__(self):
        return len(self.states)

