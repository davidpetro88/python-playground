cars = {}
cars['corola'] = "red"
cars['fit'] = "green"
cars['320'] = "black"

print(cars.keys())
print("Car Corola ->    " + cars['corola'])

for key, value in cars.items():
    print(key + " = " + value)

user = dict(name='David', lastName='Petro', city='Porto Alegre')
print (user)
print ("user name : " + user['name'])

user2= {
    'name' : 'David',
    'lastName' : 'Petro',
    'city' : 'Porto Alegre'
}

print (user2)
print ("user2 city : " + user2['city'])