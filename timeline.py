import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

def show_timeline(data, states):
    print("show timeline")
    colormapping = {}
    for i, state in enumerate(states):
        colormapping[state] = f"C{i}"

    points = []
    colors = []
    for bar_line in data:
        bar_start, bar_end, bar_color = bar_line
        v =  [(bar_start, states.index(bar_color)+1-0.4),
              (bar_start, states.index(bar_color)+1+0.4),
              (bar_end  , states.index(bar_color)+1+0.4),
              (bar_end  , states.index(bar_color)+1-0.4),
              (bar_start, states.index(bar_color)+1-0.4)]
        points.append(v)
        colors.append(colormapping[bar_color])

    bars = PolyCollection(points, facecolors=colors)

    fig, ax = plt.subplots()
    ax.add_collection(bars)
    ax.autoscale()

    ax.set_yticks([i+1 for i in range(len(states))])
    ax.set_yticklabels(states)
    plt.show()
    

data = [(0,5,'idle'),(5,8,'sleep'),(8,12,'idle'),(12,18,'stress'),
        (18,23,'idle'),(23,30,'sleep'),(30,35,'idle'),(35,38,'sleep'),
        (38,40,'idle'),(40,44,'stress'),(44,47,'idle')]
states = ["sleep", "idle", "stress"]
show_timeline(data, states)