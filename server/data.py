#This file will deal with getting the data for the project.

#importing supporting libraries
import numpy as np
import pandas as pd
import datetime

class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/LGBT_Survey_DailyLife.csv')

    def question_one_data(self, state, orientation):
        data_set = self.data[(self.data.CountryCode == state) & (self.data.subset == orientation)]
        data_set = data_set[(data_set.question_code == 'b1_a')]
        
        print(data_set.head())

data = Data()
data.question_one_data('Austria', 'Lesbian')
