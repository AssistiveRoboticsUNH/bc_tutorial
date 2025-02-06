### Robomimic 
In this tutorial we will show a minimilastic example of training policy. For official robomimic tutorial please refer to [robomimic tutorial](https://robomimic.github.io/docs/introduction/overview.html)


### Installation
Follow this [link](https://robomimic.github.io/docs/introduction/installation.html) to install robomimic and robosuite simulator.

### Download data
* For quick start download Proficient-Human low-dimensional lift data from here [link](https://robomimic.github.io/docs/datasets/robomimic_v0.1.html)

* direct link to download [Proficient-Human low-dimensional lift data](http://downloads.cs.stanford.edu/downloads/rt_benchmark/lift/ph/low_dim_v141.hdf5) save as to download, click may not work.


### Understanding Robomimic data

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


### Training policy 
* BC:  <a href="train_minimal_lift.ipynb"> train_minimal_lift.ipynb </a>



### Collecting human demonstration.
We will see how we can collect demonstration using keyboard. TODO: to be added.


### run minimal lift in colab
<a target="_blank" href="https://colab.research.google.com/github/AssistiveRoboticsUNH/bc_tutorial/blob/main/robomimic/train_minimal_lift.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

