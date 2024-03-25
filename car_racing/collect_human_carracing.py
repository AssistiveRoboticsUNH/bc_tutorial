import gym 
import readchar
import numpy as np 
import threading 
import pickle 
import argparse

env_name = "CarRacing-v2"
env=gym.make(env_name, render_mode="human")


key_pressed=0 #0->None, 1->Left, 2->right
is_alive=True 

def read_key():
    global key_pressed, is_alive
    while is_alive:
        key = readchar.readkey() 
        if key=='\x1b[D':
            key_pressed=1 
        elif key=='\x1b[C':
            key_pressed=2
        elif key=='q':
            is_alive=False
        else:
            key_pressed=0


key_thread = threading.Thread(target=read_key) 
key_thread.daemon = True 
key_thread.start()


 
def main(n_trajectories):
    global key_pressed, is_alive
    info=f""" 
        First, (select) click the terminal not the game window.
        Now, press left/right arrow keys to control the car.

        Collect human demonstrations for {env_name}
    """
    
    print(info)

    trajectories=[] 
    total_reward=0

    steer=0.5
    gas=0.02
    for t in range(n_trajectories):
        trajectory=[]
        episode_reward=0
        obs,_=env.reset()
        for i in range(1000):
            action=env.action_space.sample()
            action=np.zeros(3)
            action[1]=gas

            if key_pressed==1:
                action[0]=-steer
                key_pressed=0
            elif key_pressed==2:
                action[0]=steer
                key_pressed=0
            if is_alive==False:
                break 

            next_obs,r,done,truncated,info=env.step(action)
            trajectory.append((obs, action))
            episode_reward+=r 
            obs=next_obs 
            env.render()
            if done or truncated:
                print('stop: ', done, truncated, i)
                break 

        trajectories.append(trajectory)
        total_reward += episode_reward


    is_alive=False
    env.close()


    average_reward=total_reward//n_trajectories

    print(f'Total trajectory: {n_trajectories} |  Average reward: {average_reward}')

    data_path = "expert_data/"+f'human_demos_{n_trajectories}_{average_reward}.pkl'

    with open(data_path, 'wb') as f:
        pickle.dump(trajectories, f) 
    print('Expert trajectories saved: ', data_path)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--n", type=int, default=2)
    args = args.parse_args()
    main(args.n)
