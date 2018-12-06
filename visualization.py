from golden_rule import main
from matplotlib.pyplot import plot


def create_plot():
    x, y = main()
    plot(x, y, 'go--', linewidth = 2)



create_plot()

