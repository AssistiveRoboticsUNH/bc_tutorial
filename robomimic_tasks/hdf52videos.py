import os
import json
import h5py
import numpy as np

import robomimic
import robomimic.utils.file_utils as FileUtils
import robomimic.utils.env_utils as EnvUtils
import robomimic.utils.obs_utils as ObsUtils
import imageio
import matplotlib.pyplot as plt
import argparse
import cv2

def playback_and_save(demo_key, f,  env, tosave, is_normalized, action_mins, action_maxs, show_timestep=False):
    video_path = os.path.join(tosave, demo_key+".mp4")
    video_writer = imageio.get_writer(video_path, fps=20)
    
    init_state = f["data/{}/states".format(demo_key)][0]
    model_xml = f["data/{}".format(demo_key)].attrs["model_file"]
    initial_state_dict = dict(states=init_state, model=model_xml)

    # reset to initial state
    env.reset_to(initial_state_dict)

    # playback actions one by one, and render frames
    actions = f["data/{}/actions".format(demo_key)][:]
    
    if is_normalized:
        ac=np.array(actions)
        ac_unnorm = action_mins +( (ac+1.0)/2.0 )*(action_maxs-action_mins)
        actions = ac_unnorm
    
    for t in range(actions.shape[0]):
        env.step(actions[t])
        video_img = env.render(mode="rgb_array", height=512, width=512, camera_name="agentview")
        video_img = np.ascontiguousarray(video_img, dtype=np.uint8)
        if show_timestep:
            cv2.putText(video_img, str(t), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)   #write timestep on image
        video_writer.append_data(video_img)

    video_writer.close()
    print('saved to',video_path)

def main(dataset_path, save_dir, mask_name, show_timestep=False):
    if save_dir==None:
        save_dir = os.path.join(os.path.dirname(dataset_path), "videos")

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    print(f'dataset: {dataset_path}')
    print(f'save to: {save_dir}')


    f = h5py.File(dataset_path, "r")
    demos = list(f["data"].keys())
    num_demos = len(demos)
    print(f"hdf5 file {dataset_path} has {num_demos} demonstrations")
    masks=[]
    if mask_name!=None:
        if mask_name=='all':
            masks=f['mask'].keys()
        else:
            masks=[mask_name]
    else:
        masks=f['mask'].keys()

    is_normalized = 'mins' in f.keys()
    action_mins = None
    action_maxs = None
    if is_normalized:
        action_mins=np.array( f['mins'] )
        action_maxs=np.array(f['maxs'])
 
    env_meta = json.loads(f["data"].attrs["env_args"]) 

    env = EnvUtils.create_env_from_metadata(
        env_meta=env_meta, 
        render=False,            # no on-screen rendering
        render_offscreen=True,   # off-screen rendering to support rendering video frames
    )
    # dummy spec necessary for playing back
    dummy_spec = dict(
        obs=dict(
                low_dim=["robot0_eef_pos"],
                rgb=["agentview_image", "robot0_eye_in_hand"],
            ),
    )
    ObsUtils.initialize_obs_utils_with_obs_specs(obs_modality_specs=dummy_spec)



    if len(masks)>0:
        parent_dir=save_dir
        for mask_name in masks:
            save_dir = os.path.join(parent_dir, mask_name)
            if not os.path.exists(save_dir):
                os.mkdir(save_dir)
        
            demos=[demo.decode('utf-8') for demo in f['mask'][mask_name]] 
            for i, demo_key in enumerate(demos):
                print(f'#demo {i+1}/{len(demos)} {demo_key}')
                playback_and_save(demo_key, f, env, save_dir, is_normalized, action_mins, action_maxs, show_timestep)

    else: 
        demos=[b  for b in f['data'].keys()]   
            
        for i, demo_key in enumerate(demos):
            print(f'#demo {i+1}/{len(demos)} {demo_key}')
            playback_and_save(demo_key, f, env, save_dir, is_normalized, action_mins, action_maxs, show_timestep)


if __name__=='__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--dataset', type=str, help='path to input hdf5 dataset', required=True)
    args.add_argument('--save_dir', type=str, help='path to save directory')
    args.add_argument('--mask', type=str, help='mask name')
    args.add_argument('--show_timestep', action='store_true', help='show timestep on video')
    args = args.parse_args()
    main(args.dataset, args.save_dir, args.mask, args.show_timestep)

# python hdf52videos.py --dataset /home/ns/robosuite/collects/1705874644_525442/demo101_jan21_image.hdf5
# python hdf52videos.py --dataset /home/ns/collect_robomimic_demos/processed/lift_image_300_v1.hdf5 --mask=all
# python hdf52videos.py --dataset /home/ns1254/robomimic/datasets/square/mh/image_v141.hdf5 --mask=worse

