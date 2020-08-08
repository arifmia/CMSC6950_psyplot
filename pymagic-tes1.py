# -*- coding: utf-8 -*-
import sys
import os
#from pymagicc.io import MAGICCData
import matplotlib.pyplot as plt
import pandas as pd
import pymagicc
from pymagicc import scenarios


plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = 10, 5
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.size"] = 12


output_path = os.path.join(
    os.path.dirname(__file__),
    './example-plot.png'
)
results_df = pd.DataFrame()
results_df = scenarios['RCP45']
results_df
for name, scen in scenarios.items():
    #print(scen['RCP26'])
    #results = pymagicc.run(scen)
    results, params = pymagicc.run(scen, return_config=True)    
    #print(results["BCB_EMIS"])
    #, "**kwargs"
    print(list(results.keys()))
    results_df = pd.DataFrame.from_dict(results, orient=results.keys)
    print(results_df)
    #results_df.set_index("time", inplace=True)

    global_temp_time_rows = (
        (results_df.var == "Surface Temperature")
        & (results_df.region == "World")
    )

    temp = (
        results_df.values[global_temp_time_rows].loc[1850:]
        - results_df.values[global_temp_time_rows].loc[1850:1900].mean()
    )
    temp.plot(label=name)

plt.legend()
plt.title("Global Mean Temperature Projection")
plt.ylabel("°C over pre-industrial (1850-1900 mean)")
plt.legend(loc="best")

plt.savefig(output_path, dpi=96)