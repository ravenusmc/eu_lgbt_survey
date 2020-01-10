#This file will deal with testing out ideas for this project.

#importing supporting libraries
import numpy as np
import pandas as pd

class Test():

    def __init__(self):
        self.data = pd.read_csv('./data/LGBT_Survey_DailyLife.csv')

    def show_Some_Data(self):
        print(self.data.head())

    def show_Unique_Elements(self):
        print(self.data['question_label'].unique())

    def show_unique_question_answers(self):
        data = self.data[self.data.question_label == 'In your opinion, how widespread are casual jokes in everyday life about lesbian, gay, bisexual and/or transgender people in the country you live?']
        print(data['answer'].unique())
        # death_data_set = self.data[(self.data.FATALITY_YEAR >= yearOne) & (self.data.FATALITY_YEAR <= yearTwo)]


test = Test()
#test.show_Some_Data()()
test.show_unique_question_answers()
