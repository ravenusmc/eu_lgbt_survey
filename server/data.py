#This file will deal with getting the data for the project.

#importing supporting libraries
import numpy as np
import pandas as pd
import datetime
from support import *

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

    def get_map_data(self, data):
        answer = data['answer']
        sex = data['sex']
        #The support class is called to convert the question to the question code
        support = Support()
        question_code = support.get_question_code(data)
        #Creating a new dataset based on the data that the user selects
        data_set = self.data[(self.data.question_code == question_code) & (self.data.answer == answer)
        & (self.data.subset == sex)]
        states = ['Austria', 'Belgium', 'Bulgaria', 'Cyprus', 'Czech Republic', 'Germany',
            'Denmark', 'Estonia', 'Greece', 'Spain', 'Finland', 'France', 'Croatia',
            'Hungary', 'Ireland', 'Italy', 'Lithuania', 'Luxembourg', 'Latvia', 'Malta',
            'Netherlands', 'Poland', 'Portugal', 'Romania', 'Sweden', 'Slovenia',
            'Slovakia', 'United Kingdom']
        map_data = []
        for state in states:
            rows = []
            #The data set needs to be reset during each loop
            state_data_set = data_set
            state_data_set = state_data_set[(state_data_set.CountryCode == state)]
            percentage = int(state_data_set.iloc[0][5])
            rows.append(state)
            rows.append(percentage)
            map_data.append(rows)
        return map_data




# data = Data()
# data.question_one_data('Austria', 'Lesbian')
