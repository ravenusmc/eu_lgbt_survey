#This file will deal with getting the data for the project.

#importing supporting libraries
import numpy as np
import pandas as pd
import datetime

class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/LGBT_Survey_DailyLife.csv')

    def question_one_data(self, state, orientation):
        question_one_data = []
        columns = ['View', 'Percentage']
        question_one_data.append(columns)
        data_set = self.data[(self.data.CountryCode == state) & (self.data.subset == orientation)]
        questionCodes = ['b1_a', 'b1_e', 'b1_c', 'b1_d', 'b1_b']
        data_set = data_set[(data_set.question_code == 'b1_a')]
        values = ['Very widespread', 'Fairly widespread', 'Fairly rare', 'Very rare', 'Don`t know']
        for value in values:
            rows = []
            loop_data_set = data_set
            loop_data_set = loop_data_set[(loop_data_set.answer == value)]
            percentage_point = loop_data_set['percentage']
            rows.append(value)
            rows.append(int(percentage_point.iloc[0]))
            question_one_data.append(rows)
        return question_one_data




# data = Data()
# data.question_one_data('Austria', 'Lesbian')
