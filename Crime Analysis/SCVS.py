import csv
import sklearn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn import model_selection
import pandas as pd
import seaborn as sns

def get_state_crime_data(filename):
    data = list()
    with open(filename) as file:
        csv_writer = csv.DictReader(file)

        for row in csv_writer:
            row_dict = {k: float(v) if k !='State' else v for k, v in row.items()}
            data.append(row_dict)

    return data

def growth_percentage(state_crime_data, year_1, year_2, state, category):
        for dictionary in state_crime_data: 
            if dictionary['State'] == state:
                if dictionary['Year'] == year_1:
                    statOne = dictionary[category]
                elif dictionary['Year'] == year_2:
                    statTwo = dictionary[category]

        percent = ((statTwo - statOne) / statOne) * 100
        round_percent = round(percent, 1)

        if round_percent < 0:
            round_percent *= -1
            return f"Decrease: {round_percent}%"

        else:
            return f"Increase: {round_percent}%"

def visual_model(state_crime_data, year_1, year_2, state, crime):

    if year_1 < 1960 or year_2 > 2019:
        return "This data model provides crime rate statistics for the years between 1960 and 2019"
    else:
        x_axis = [year for year in range(year_1, year_2 + 1)]
        y_axis = list()
        for dictionary in state_crime_data:
            if dictionary['State'] == state and dictionary['Year'] in x_axis:
                y_axis.append(dictionary[crime])

        xPlots = np.array(x_axis)
        yPlots = np.array(y_axis)

        plt.plot(xPlots, yPlots, label="Crime")
        plt.xticks(rotation=45)

        plt.title(f"State Crime Data ({state})")
        plt.ylabel("Rate(s) per 100,000")

        plt.legend()

        return plt.show()

def axes(state_crime_data, state, year_1, year_2, crime):

    if year_1 < 1960 or year_2 > 2019:
        return "This data model provides crime rate statistics for the years in between 1960 and 2019, please use the prediction tool for preceding or following years."

    x_axis = [i for i in range(year_1, year_2 + 1)]
    y_axis = list()
    for dictionary in state_crime_data:
        if dictionary['State'] == state and dictionary['Year'] in x_axis:
            y_axis.append(dictionary[crime])

    return (x_axis, y_axis)

def compare(state_1, state_2, year_1, year_2, crime, state_crime_data):

    stateOneAxes = axes(state_crime_data, state_1, year_1, year_2, crime)
    stateTwoAxes = axes(state_crime_data, state_2, year_1, year_2, crime)

    x_axis_1 = np.array(stateOneAxes[0])
    x_axis_2 = np.array(stateTwoAxes[0])
    y_axis_1 = np.array(stateOneAxes[1])
    y_axis_2 = np.array(stateTwoAxes[1])

    plt.plot(x_axis_1, y_axis_1, label=state_1, color='#110d25')
    plt.plot(x_axis_2, y_axis_2, label=state_2, color='#1d45c2')

    plt.legend()

    plt.title("Crime Statistics per State")
    plt.xticks(rotation=45)
    plt.ylabel("Rate(s) per 100,000")

    return plt.show()

def highest_n_category(state_crime_data, category, n):
    null = int()
    hash = dict()
    states, results = [], []

    for dictionary in state_crime_data:
        if dictionary[category] > null:
            null = dictionary[category]
            results.append(null)
            states.append(dictionary['State'])
    newRes, newStates = results[-1:-n-1:-1], states[-1:-n-1:-1]

    for i in range(len(newRes)):
        hash[newRes[i]] = newStates[i]
    return hash

def highest_n_crime(state_crime_data, category, state, n):
    output = sorted([dictionary[category]for dictionary in state_crime_data if dictionary['State'] == state])
    return output[-1:-n-1:-1]

def predict_category(state_crime_data, state, category, year_1, year_2):
    data = pd.read_csv('state_crime.csv', sep=",")
    f_data = data[data.State.isin([state])]
    
    f_data = f_data[['Year', category]]
    predict = category

    X = np.array(f_data.drop([predict], 1))
    y = np.array(f_data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.9)

    model = linear_model.LinearRegression().fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)

    # print(accuracy)
    # print("Co: ", model.coef_)
    # print("Intercept: ", model.intercept_)

    years = np.array([years for years in range(year_1, year_2)]).reshape(-1, 1)
    predictions = model.predict(years)

    x_axis, y_axis = [], []
    for x in range(len(predictions)):
        x_axis.append(predictions[x])
        y_axis.append(years[x])
    
    return x_axis, y_axis

def prediction_model_graph(state_crime_data, state, category, year_1, year_2):
    x, y = predict_category(state_crime_data, state, category, year_1, year_2)
    plt.plot(x, y, color='#110d25')

    plt.title("Growth Prediction Rate")
    plt.xticks(rotation=45)

    return plt.show()


    
