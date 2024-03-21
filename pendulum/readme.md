### Pendulum
Both state and action space are continuous.

TODO: add figure.

#### Data Collection
* Skip if you want to use the given expert data.

```
    # install stable-baseline-3
```


### Train policy

* Step 2: Train the model & Evaluate
```
# Scikit-learn Model
bc_pendulum_sklearn.ipynb

# Pytorch Model with MSE loss
bc_pendulum_torch.ipynb

# Pytorch Model (Gaussian Actor) with MLE loss
bc_pendulum_torch_gaussian.ipynb

