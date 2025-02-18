### Robomimic 
In this tutorial we will show a minimilastic example of training policy. For official robomimic tutorial please refer to [robomimic tutorial](https://robomimic.github.io/docs/introduction/overview.html)


### Quick start
Quick start with minimal implementation, open In Colab [train_lift_minimal.ipynb](https://colab.research.google.com/github/AssistiveRoboticsUNH/bc_tutorial/blob/main/robomimic_tasks/train_lift_minimal.ipynb)




### 1. Installation
The following commands are taken from this [link](https://robomimic.github.io/docs/introduction/installation.html) 

```
conda create -n robomimic_venv python=3.8.0
conda activate robomimic_venv
```

Install PyTorch
* Install from here https://pytorch.org/get-started/locally/


Install robomimic
```
cd <PATH_TO_YOUR_INSTALL_DIRECTORY>
git clone https://github.com/ARISE-Initiative/robomimic.git
cd robomimic
pip install -e .
```

Install robosuite (Use from source installation, don't use pip install robosuite)
```
cd <PATH_TO_INSTALL_DIR>
git clone https://github.com/ARISE-Initiative/robosuite.git
cd robosuite
git checkout v1.4.1

pip install -r requirements.txt
```
 

### 2. Collecting human demonstration.

#### Step 1: give demonstration using robosuite codebase

<b>Option 1:</b> Collect data using keyboard
```
cd robosuite/robosuite/scripts
conda activate robomimic_venv
python collect_human_demonstrations.py
```

Press CTRL+C when you are done giving demonstrations. 
The data will be saved in the robosuite/robosuite/models/assets/demonstrations folder. Remember the filepath in your computer, that should be similar to the following file path.
```
/home/ns/robosuite/robosuite/models/assets/demonstrations/1739396875_9637682/demo.hdf5
```  

<b>Option 2:</b> Collect data using Spacemouse.
Pleasee [see](spacemouse_install.md) for installation instruction.

Then run 
```
cd robosuite/robosuite/scripts
conda activate robomimic_venv
python collect_human_demonstrations.py --device spacemouse
```


#### Step 2: convert data to robomimic format using robomimic codebase
```bash
   cd  robomimic/robomimic/scripts/conversion
   conda activate robomimic_venv
   python convert_robosuite.py --dataset  demo_file_path.hdf5
```
* Change the "demo_file_path.hdf5" with your hdf5 file accordingly.

#### Step 3: Generate image observation data using robomimic codebase
```bash
   cd  robomimic/robomimic/scripts/
   conda activate robomimic_venv
   python dataset_states_to_obs.py --dataset demo_file_path.hdf5 \
                                 --output_name output_filepath.hdf5\
                                 --done_mode 2 --camera_names agentview robot0_eye_in_hand --camera_height 84 --camera_width 84  
```
* Note: change the dataset path and the output path accordingly.


#### Step 4: (Optional) create videos from *.hdf5 using this codebase.
 
```bash
   cd bc_tutorial/robomimic_tasks
   conda activate robomimic_venv
   python hdf52videos.py --dataset demo_image_filepath.hdf5 
```
The videos will be saved inside "videos" folder in the same directory where the hdf5 file is located.



### 3. Understanding Robomimic data

* The data is stored in hdf5 format. The structure is as follows:
```
low_dim_v141.hdf5
├──data
│  ├──demo_0
│  │  ├──action(7)
│  │  ├──obs
│  │       ├──Object(10)
│  │       ├──robot0_eef_pos(3)
│  │       ├──robot0_eef_quat(4)
│  │       ├──robot0_gripper_qpos(2)
│  │       ├──robot0_joint_pos(7)
│  │       ...
│  │  ├──next_obs
│  │  ├──rewards
│  │  ...
│  ├──demo_1
│  ...
├──mask
```

From this data we are interested in
   * action: 7 dimensional action space (delta x, delta y, delta z, delta roll, delta pitch, delta yaw, gripper)
   * obs: observation space (object(10), robot0_eef_pos(3), robot0_eef_quat(4), robot0_gripper_qpos(2)) that is 19 dimensional


* See the <a href="data_info.ipynb">data_info.ipynb</a> file to understand the data structure.


### 4. Training policy 

Please see the robomimic tutorials here [Getting Started](https://robomimic.github.io/docs/introduction/getting_started.html)


<!-- Quick start with minimal implementation <a href="train_minimal_lift.ipynb"> train_minimal_lift.ipynb </a>

For general training policy, plese see   robomimic/robomimic/scripts/train.py  after you done installing.



### (Optional) Download data
* Download Proficient-Human low-dimensional lift data from here [link](https://robomimic.github.io/docs/datasets/robomimic_v0.1.html)

* direct link to download [Proficient-Human low-dimensional lift data](http://downloads.cs.stanford.edu/downloads/rt_benchmark/lift/ph/low_dim_v141.hdf5) save as to download, click may not work. -->

### Common Trouble shooting


```bash
sudo apt install libosmesa6-dev libgl1-mesa-glx libglfw3 patchelf

conda install -c conda-forge glew
conda install -c conda-forge mesalib
conda install -c menpo glfw3
 

```

You can also try to install in the "base" environment instead of "robomimic_venv" environment. 
