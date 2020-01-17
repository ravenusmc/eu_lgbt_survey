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
        columns = ['View', 'Count']
        question_one_data.append(columns)
        data_set = self.data[(self.data.CountryCode == state) & (self.data.subset == orientation)]
        data_set = data_set[(data_set.question_code == 'b1_a')]
        values = ['Very widespread', 'Fairly widespread', 'Fairly rare', 'Very rare', 'Don`t know']
        for value in values:
            rows = []
            loop_data_set = data_set
            loop_data_set = loop_data_set[(loop_data_set.answer == value)]
            print(loop_data_set.head())
            print(loop_data_set['answer'].count())
            input()



        print(values)

data = Data()
data.question_one_data('Austria', 'Lesbian')
