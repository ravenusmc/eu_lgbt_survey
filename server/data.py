#This file will deal with getting the data for the project.

#importing supporting libraries
import numpy as np
import pandas as pd
import datetime

class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/LGBT_Survey_DailyLife.csv')

    def question_one_data(self, state, orientation):
        question_data_one = []
        question_data_two = []
        question_data_three = []
        question_data_four = []
        question_data_five = []
        data_lists = [question_data_one, question_data_two, question_data_three,
        question_data_four, question_data_five]
        columns = ['View', 'Percentage']
        for data_list in data_lists:
            data_list.append(columns)
        data_set = self.data[(self.data.CountryCode == state) & (self.data.subset == orientation)]
        questionCodes = ['b1_a', 'b1_e', 'b1_c', 'b1_d', 'b1_b']
        count = 0
        for questionCode in questionCodes:
            question_data_set = data_set
            question_data_set = question_data_set[(question_data_set.question_code == questionCode)]
            values = ['Very widespread', 'Fairly widespread', 'Fairly rare', 'Very rare', 'Don`t know']
            for value in values:
                rows = []
                loop_data_set = question_data_set
                loop_data_set = loop_data_set[(loop_data_set.answer == value)]
                percentage_point = loop_data_set['percentage']
                rows.append(value)
                rows.append(int(percentage_point.iloc[0]))
                data_lists[count].append(rows)
            count += 1
        return data_lists




# data = Data()
# data.question_one_data('Austria', 'Lesbian')
