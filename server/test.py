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
        print(self.data['CountryCode'].unique())


test = Test()
#test.show_Some_Data()()
test.show_Unique_Elements()
