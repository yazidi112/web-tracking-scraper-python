import matplotlib.pyplot as plt

class Chart:
    def __init__(self,labels,data,title,ylabel):
        self.labels = labels
        self.data = data
        self.title = title
        self.ylabel = ylabel
    
    def show(self):
        fig, ax = plt.subplots()
        ax.bar(self.labels, self.data)
        ax.set_ylabel(self.ylabel)
        ax.set_title(self.title)
        plt.show()

"""
labels = ['apple', 'blueberry', 'cherry', 'orange']
data = [40, 100, 30, 55]
title = 'Fruit supply by kind and color'
ylabel = 'fruit supply'
Chart.show(labels,data,title,ylabel)
"""