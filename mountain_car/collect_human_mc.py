import gym
import readchar
import numpy as np
import argparse
import pickle
 
Push_Left = 0
No_Push = 1
Push_Right = 2

env_name='MountainCar-v0'
 
arrow_keys = {
    '\x1b[D': Push_Left,
    '\x1b[B': No_Push,
    '\x1b[C': Push_Right}

def main(n_trajectories):
    info=f""" 
        First, (select) click the terminal not the game window.
        Now, press left/right arrow keys to control the car.

        Collect human demonstrations for {env_name}
    """
    
    print(info)
    env = gym.make(env_name, render_mode='human')
    trajectories = []

 
    total_reward=0
    for episode in range(n_trajectories):
        trajectory = []
        step = 0
 
        env.reset() 
        episode_reward=0
        while True: 
            env.render()  
            key = readchar.readkey() 

            if key not in arrow_keys.keys():
                print('skip demo')
                break 

            action = arrow_keys[key]
            state, reward, done, trunc, info = env.step(action)
            episode_reward+=reward

            if state[0] >= env.env.goal_position and step > 129: # trajectory_length : 130
                break

            if done or trunc:
                # print('done or truncated')
                break

            trajectory.append((state, action))
            step += 1

       
        total_reward+=episode_reward
        trajectories.append(trajectory)

        print(f'\nEpisode: {episode+1}/{n_trajectories} | reward: {episode_reward}')

    env.close()
 
    average_reward=total_reward//n_trajectories

    print(f'Total trajectory: {n_trajectories} |  Average reward: {average_reward}')
    
    data_path = "expert_data/"+f'human_demos_{n_trajectories}_{average_reward}.pkl'

    with open(data_path, 'wb') as f:
        pickle.dump(trajectories, f)

    print('Expert trajectories saved')

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--n", type=int, default=10)
    args = args.parse_args()
    main(args.n)
