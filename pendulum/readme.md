### Pendulum
Both state and action space are continuous.

<!-- TODO: add figure. -->

#### Data Collection
Skip if you want to use the given expert data.

* Install stable-baselines3
```
    pip install stable-baselines3[extra]
```
* Generate data: <a href="data_gen_pendulum.ipynb"> data_gen_pendulum.ipynb </a>


### Train Regression policy
* predict action directly from state
* MSE loss
Using Scikit-learn :  <a href="bc_pendulum_sklearn.ipynb"> bc_pendulum_sklearn.ipynb </a> </br>
 Using Pytorch : <a href="bc_pendulum_torch.ipynb">bc_pendulum_torch.ipynb</a> 
 

### run pytorch training on pendulum in colab
<a target="_blank" href="https://colab.research.google.com/github/AssistiveRoboticsUNH/bc_tutorial/blob/main/pendulum/bc_pendulum_torch.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>



<!-- TODO: add figure for both policy. -->

### Train gaussian policy
* predict mean and variance
* Negative log likelihood loss

<a href="bc_pendulum_torch_gaussian.ipynb"> bc_pendulum_torch_gaussian.ipynb </a>




