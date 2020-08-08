import matplotlib.pyplot as plt
import pymagicc
from pymagicc import scenarios

for name, scen in scenarios.items():
    results, params = pymagicc.run(scen, return_config=True)
    print(name)
    temp = (results["SURFACE_TEMP"].GLOBAL.loc[1850:] -
            results["SURFACE_TEMP"].GLOBAL.loc[1850:1900].mean())
    temp.plot(label=name)

plt.legend()
plt.title("Global Mean Temperature Projection")
plt.ylabel(u"°C over pre-industrial (1850-1900 mean)")
plt.savefig('Plot1_GlobalMeanTemperatureProjection.png', dpi=96)