import matplotlib.pyplot as pl


class Graph:
    def __init__(self, time, value) -> None:
        pl.plot(time, value)
        
        pl.show()