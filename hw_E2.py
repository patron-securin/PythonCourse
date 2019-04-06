import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

pareto = np.random.pareto(100, 1000)

sns.distplot (pareto,label = "pareto")
plt.legend ()
plt.show ()
