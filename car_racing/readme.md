### Self-driving car
States are image and action are continuous values (steering, gas, brake). We will use the expert data from the human player.


### Collecting human demonstration using keyboard

 
Skip this step if you want to use the provided expert data. Run the following command to collect your own human demonstration. 

``` 
python collect_human_carracing.py --n 5
```
Data will be saved in `expert_data` folder. 


### Train Behavioral Cloning policy

<a href="bc_carracing.ipynb"> bc_carracing.ipynb </a>

