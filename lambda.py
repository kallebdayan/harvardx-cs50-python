people = [
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Cho", "house":"Havenclaw"},
    {"name":"Draco", "house":"Slytherin"}
]


#def f(person):
#    return person["house"]

#people.sort(key=f)
people.sort(key=lambda person: person["house"])

print(people)