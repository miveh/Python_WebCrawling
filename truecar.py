from bs4 import BeautifulSoup
import requests
import email
import re

# import mysql.connector


"""
    my database name: employee
    my table name: car
    my columns: model,value
"""


"""
    The section commented below is for connecting to the database.
"""
# cnx = mysql.connector.connect(user = 'root', password = 'root',
#                                 host = '127.0.0.1', database = 'employee',
#                                 auth_plugin = 'mysql_native_password')
# cursor = cnx.cursor()
# query = 'insert into car (model,value) value (%s,%s)'


car_brands = {'acura', 'alfa Romeo', 'am general', 'aston martin', 'audi', 'bentley', 'bmw', 'buick', 'cadillac',
              'chevrolet', 'chrysler', 'dodge', 'ferrari', 'fiat', 'fisker', 'ford', 'freightliner', 'genesis', 'geo',
              'gmc', 'honda', 'hummer', 'hyundai', 'infiniti', 'isuzu', 'Jaguar', 'Jeep', 'Karma', 'Kia', 'Lamborghini',
              'Land Rover', 'Lexus', 'Lincoln', 'Lotus', 'Maserati', 'Maybach', 'Mazda', 'McLaren', 'mercedes-benz',
              'mercury', 'mini', 'mitsubishi', 'nissan', 'oldsmobile', 'panoz', 'plymouth', 'pontiac', 'porsche', 'ram',
              'rolls-royce', 'saab', 'saturn', 'scion', 'smart', 'subaru', 'suzuki', 'tesla', 'toyota', 'volkswagen',
              'volvo'}


inter_brand = input()


tr = False
while not tr:
    if inter_brand in car_brands:
        tr = True
    else:
        print('please inter a valid brand.')
        inter_brand = input()


str_ = 'https://www.truecar.com/used-cars-for-sale/listings/' + inter_brand
r = requests.get(str_)
soup = BeautifulSoup(r.text, "html.parser")


all_agahi = soup.find_all('div',
                          attrs={'data-test': "cardContent", 'class': ['card-content', 'vehicle-card-body', 'order-3'],
                                 'data-qa': 'CardContent'})


for agahi in all_agahi[:20]:
    A = agahi.find('div', attrs={'class': ['vehicle-card-top'], 'data-qa': 'VehicleCardTop'})
    B = agahi.find('div', attrs={'class': ['vehicle-card-bottom', 'vehicle-card-bottom-top-spacing'],
                                 'data-qa': 'VehicleCardMiddle'})
    C = B.find('div', attrs={'class': ['d-flex', 'w-100', 'vehicle-card-bottom-pricing', 'justify-content-between'],
                             'style': 'min-height:43px'})
    D = C.find('div', attrs={
        'class': ['padding-left-3', 'vehicle-card-bottom-pricing-secondary', 'vehicle-card-bottom-max-50']})
    # val = [A.text]

    print(A.text, D.text)


"""
    for database.
"""
# all_agahi = soup.find_all('div', attrs={'data-test': "cardContent",
#                                             'class': ['card-content', 'vehicle-card-body', 'order-3'],
#                                             'data-qa': 'CardContent'})

# cursor.execute(query,val)
# cnx.commit()
# cnx.close()
