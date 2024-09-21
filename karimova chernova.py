#14.1
chel = {"first_name": "aschotik",'last_name': "Tigranovich", 'age': "25", "city": "Moscow"}
lilpeep = {"first_name": "gulnara",'last_name': "Pechenkina", 'age': "22", "city": "Tuemen"}
lolkek = {"first_name": "Maga",'last_name': "Zabivnoi", 'age': "28", "city": "Orel"}
users = [chel, lilpeep, lolkek]

for user in users:
   print(user)

#14.2
people_user = {'Mark': [17, 52, 228],'lev': [666,33, 28],'dava': [228, 999, 19],'david': [222, 9, 23],'oleg': [555, 7, 13]}
for people, value in people_user.items():
    print(f"{people}")
    for value in people_user: 


#14.3
cities = {"Тюмень, Казань, Омск"}
cities_info = {'contry': 'Россия', 'chicl': '1m', }