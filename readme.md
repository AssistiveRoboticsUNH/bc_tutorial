### Imitation Learning Hello World (in progress)

Imitation learning is supervised learning where data comes as expert demonstration. The expert can be a human or any other agent. Input data is referred to as "state" and output data as "action." In discrete action spaces, it resembles classification; in continuous action spaces, it is regression.

Policy $\pi: S \rightarrow A$ is the function/model that takes a state as input and outputs an action. The goal of imitation learning is to learn a policy that mimics the expert's behavior.

Behavioral Cloning (BC) is offline imitation learning that use only the collected demonstrations and doesn't use simulator during learning. 

This tutorial is educational purpose, so code isn't optimized for production but easy to understand. We will walk through following experiments.

|  Env   |   Task       |  State Space |  Action Space  |  Expert  |  Colab  |
|--------|--------------|--------------|----------------|----------|---------|
| Gym    | Mountain Car | Continuous(2)   | Discrete(3)       | Human    | train_sk, train_torch |
| Gym    | Pendulum     | Continuous(3)   | Continuous(1)     | RL       | train_sk, train_torch |
| Gym    | Car Racing   | Continuous   | Continuous     | Human    | train   |
| MuJoCo | Ant          | Continuous   | Continuous     | RL       | train   |
| MuJoCo | HalfCheetah  | Continuous   | Continuous     | RL       | train   |
| Robomimic | Lift      | Image,Low-dim   | Continuous     | Human    | train   |
| Sawyer | Block        | Image,Low-dim   | Continuous     | Human    | train   |
