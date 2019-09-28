import json

biodata = {
    'name':'Wisnu Prabowo', 
    'age': 25, 
    'address': 'Bogor', 
    'hobbies':['fotografi', 'bulutangkis'], 
    'is_married': False, 
    'list_school':[{
        'name':'UNAS', 
        'year_in':2016, 
        'year_out':2018, 
        'major':'Sistem Informasi'
    }],
    'skills':[{
        'programming':'advanced', 
        'analisis':'beginner'
    }],
    'interest_in_coding':True
}

print(json.dumps(biodata))