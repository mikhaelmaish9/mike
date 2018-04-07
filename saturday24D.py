names = ("John","Mary","Hellen","Mike","Mckenzie")
print(names)
print(names[0])
# print(names[6])
# names[0]="Johnny"
# print(names)
#tuple works with data that doesnt change


#lists
cities = ["Nairobi","Mombasa","Kisumu","Kampala","Arusha"]
print(cities[0])
print(cities[2])
cities [0] = "Abuja" #changing first city
print(cities)

cities.append("Lusaka")
print(cities)
scores =[84,34,45,32,76,98,23,90,10.5]
print(scores[8])


#dictionary
city ={"name":"Nrb","population":4000000,"continent":"Africa"}
print(city["population"])

results =[{"name":"Mary","score":468},{"name":"John","score":345},{"name":"mike","score":378},{"name":"Thomas","score":354}]
student = results[2]
print(student)
print(student["name"],student["score"])