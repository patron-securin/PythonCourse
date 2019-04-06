import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

poisson = np.random.poisson(lam=0.5, size=1000)
sns.distplot (poisson,label = "poisson" )
plt.legend ()
plt.show ()
