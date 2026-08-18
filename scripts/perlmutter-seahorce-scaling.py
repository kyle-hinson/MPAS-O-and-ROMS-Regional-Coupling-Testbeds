import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

#plt.style.use('seaborn-bright')

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['axes.prop_cycle'] = cycler(color=['r', 'b', 'g', 'k', 'm', "#332288", "#88CCEE", "#44AA99", "#117733", "#999933", "#DDCC77", "#CC6677", "#882255", "#AA4499"])
# mpl.rcParams['axes.color_cycle'] = cycler(color=["#332288", "#88CCEE", "#44AA99", "#117733", "#999933", "#DDCC77", "#CC6677", "#882255", "#AA4499"])

def plot_seahorce(title, dataA):
    plt.figure()
    start=0
    threads = dataA[start:, 0]
    plt.loglog(threads, dataA[start:,1], marker=".", label=r"$N_z=100$")
    plt.loglog(threads, dataA[start:,2], marker="v", label=r"$N_z=50$")
    plt.loglog(threads, dataA[start,1] / threads, '--', color='r', label=r"Ideal from $N_z=100$")
    plt.loglog(threads, dataA[start,2] / threads, '--', color='b', label=r"Ideal from $N_z=50$")
    plt.ylabel("Four-field projection time (s)", fontsize=18)
    plt.xlabel("OpenMP threads per Perlmutter CPU node", fontsize=18)
    plt.gca().set_xticks(threads)
    plt.yticks(fontsize=18)
    plt.gca().set_xticklabels(['1', '2', '4', '8', '16', '32', '64'], fontsize=18)
    plt.legend(loc="upper right", fontsize=13)
    plt.xlim(1, 64)
    plt.ylim(0.1, 40)
    plt.grid()

data_seahorce = np.array([
    [1,        18.6355,   17.8628],
    [2,        9.43428,   9.06075],
    [4,        4.76889,   4.63319],
    [8,        2.41759,   2.34106],
    [16,       1.31619,   1.25711],
    [32,       0.810559,  0.789665],
    [64,       0.540362,  0.531125],
])

plot_seahorce("Strong scaling on-node", data_seahorce)
plt.tight_layout()
plt.savefig("Figures/conv_omp_scaling_perlmutter.png", dpi=300)
plt.close()
