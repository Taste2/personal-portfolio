'''
Get cordinates of the major cities in Ghana
'''
cities = {'Kumasi':['6.6885', '-1.6244'], 'Accra':['5.556', '-0.1969'], 'Bolgatanga':['10.7856', '-0.8514'], 'Wa':['6.82', '0.2546'], 'Tamale':['', ''],
          'Cape Coast':['5.103', '-1.2407'],'Sekondi-Takoradi':['4.8982', '-1.7603'], 'Koforidua':['5.4413', '-0.7879'], 'Sunyani':['7.3399', '-2.3268'], 'Ho':['6.6008', '0.4713']}

def get_city(cities_dict):
    '''
    Get cordinates of cities in Ghana
    '''
    city = input("Enter a City name in Ghana: ")
    city = city.title()
    for key, value in cities_dict.items():
        if city == key:
            return value
        
cordinates = get_city(cities)