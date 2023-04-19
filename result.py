from chart import *
from db import View

class Result:
    @staticmethod
    def show():
        Result.request()
        Result.content()

    @staticmethod
    def request():
        results = View.request()
        labels = []
        data = []
        for x in results[0:5]:
            labels.append(x[0])
            data.append(x[1])
        
        title = 'Top request'
        ylabel = 'percent'
        chart = Chart(labels,data,title,ylabel)
        chart.show()
    
    @staticmethod
    def content():
        results = View.content_type()
        labels = []
        data = []
        for x in results[1:5]:
            print(x)
            labels.append(x[0])
            data.append(x[1])
        
        title = 'Top Content Type'
        ylabel = 'percent'
        chart = Chart(labels,data,title,ylabel)
        chart.show()

