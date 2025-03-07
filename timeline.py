import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

def show_timeline(data, states):
    colormapping = {}
    for i, state in enumerate(states):
        colormapping[state] = f"C{i}"

    points = []
    colors = []
    for bar_line in data:
        bar_start, bar_end, bar_color = bar_line
        v =  [(bar_start, states.index(bar_color)+1),
              (bar_start, states.index(bar_color)+1),
              (bar_end  , states.index(bar_color)+1),
              (bar_end  , states.index(bar_color)+1),
              (bar_start, states.index(bar_color)+1)]
        points.append(v)
        colors.append(colormapping[bar_color])

    ax = PolyCollection(points, facecolors=colors)
    ax.set_yticks([i+1 for i in range(len(states))])
    ax.set_yticklabels(states)
    plt.show()

data = [(0,5,'sleep'),(6,9,'stress')]
states = ["sleep", "idle", "stress"]
show_timeline(data, states)