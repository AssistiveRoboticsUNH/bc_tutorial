
### Collecting human demonstration using MC environment

```bash
pip install gym==0.26.2
pip install readchar
``` 

<img src="human_mc.png" width=60%>


### Mountain Car
Continuous state and discrete action.

* Step 1: Data Collection (Human Expert)
``` 
python collect_human_mc.py --n 10
```

* Step 2: Train the model & Evaluate
```
# Scikit-learn Model
bc_mc_sklearn.ipynb

# Pytorch Model
bc_mc_torch.ipynb
```