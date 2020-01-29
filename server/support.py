#The purpose of this file is to provide methods that will support the main data class.

class Support():

    #This method will take the question that the user selects and convert the question
    #to a question code. This will help me with the sort of the data. 
    def get_question_code(self, data):
        if data['question'] == 'In your opinion, how widespread is offensive language about lesbian gay bisexual or transgender people by politicians in the country where you live?':
            question_code = 'b1_a'
        elif data['question'] == 'In your opinion, how widespread is same-sex partners holding hands in public in the country where you live?':
            question_code = 'b1_e'
        elif data['question'] == 'In your opinion, how widespread are expressions of hatred and aversion towards lesbian, gay, bisexual and/or transgender in public in the country where you live?':
            question_code = 'b1_c'
        elif data['question'] == 'In your opinion, how widespread are assaults and harassment against lesbian, gay, bisexual and/or transgender people in the country where you live?':
            question_code = 'b1_d'
        elif data['question'] == 'In your opinion, how widespread are casual jokes in everyday life about lesbian, gay, bisexual and/or transgender people in the country you live?':
            question_code = 'b1_b'
        return question_code
