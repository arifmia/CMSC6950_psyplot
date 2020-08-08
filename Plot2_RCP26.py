import pymagicc
from pymagicc import scenarios
import pandas as pd
from matplotlib import pyplot as plt

results_df = scenarios['RCP26']
for key, data in results_df.items():
    rcp26_df = pd.DataFrame.from_dict(data, orient='columns')   
    
#print(rcp26_df.keys())
print(rcp26_df.drop_duplicates())
plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = 16, 9
lines = rcp26_df.plot.line()
plt.savefig('Plot2_RCP26.png', dpi=96)