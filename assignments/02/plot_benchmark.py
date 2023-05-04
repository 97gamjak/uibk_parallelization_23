import matplotlib.pyplot as plt
import sys

plt.rcParams.update({'font.size': 16})


def make_fig(cores, times, title=""):
    seq_time = times[0]

    title = "default_title.png" if not title else title

    speedups = [seq_time/time for time in times]
    efficiencies = [speedup/core for speedup, core in zip(speedups, cores)]

    print(speedups)
    print(efficiencies)

    fig, ax1 = plt.subplots(figsize=(12, 8))
    ax2 = ax1.twinx()
    ax2.set_ylim(0, 1.1)

    l1 = ax1.plot(cores, speedups, '-bo', label='speedup',
                  linewidth=3, markersize=8)
    l2 = ax2.plot(cores, efficiencies, '-ro', label='efficiency',
                  linewidth=3, markersize=8)

    lns = l1 + l2
    labs = [l.get_label() for l in lns]
    # ax1.legend(lns, labs, loc="center right")

    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0,
                      box.width, box.height * 0.95])

    # Put a legend below current axis
    ax1.legend(lns, labs, loc='upper center', bbox_to_anchor=(0.5, 1.12),
               fancybox=True, shadow=True, ncol=5)

    plt.xticks([1, 2, 4, 8, 16, 32, 64])
    ax1.set_xlabel("Number of cores")
    ax1.set_ylabel("Speedup")
    ax2.set_ylabel("Efficiency")

    fig.savefig(title)
    # plt.show()


def read_times_file(filename):
    times = []
    cores = []
    with open(filename, "r") as f:
        for line in f:
            line_split = line.split()
            cores.append(int(line_split[0]))
            times.append(float(line_split[1]))

    print(cores)
    print(times)

    return cores, times


cores, times = read_times_file(sys.argv[1])

title = "default_title.png" if len(sys.argv) < 3 else sys.argv[2]


make_fig(cores, times, title)
