import statistics
import csv
import random
import pandas as pd
import plotly.figure_factory as ff

pf = pd.read_csv("medium_data.csv")
data = pf["reading_time"].tolist()

mean = statistics.mean(data)
print("Population_mean: ", mean)
figure = ff.create_distplot([data], ["reading_time"], show_hist = False)
figure.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["temp"], show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    print("Sampling mean: ", statistics.mean(mean_list))

setup()
