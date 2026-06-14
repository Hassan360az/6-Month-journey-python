

# mydictionay = {
#     "name": "abc",
#     "age": 34,
# }

# print (mydictionay["name"])


# thisdict = {
#     "brand": "ford",
#     "model": "Mustang",
#     "year": "1964"
# }

# thisdict ["year"] = 2020

# thisdict["color"] = "red"

# thisdict.pop("brand")

# del thisdict ["year"]

# thisdict.clear()

# print (thisdict)


x = print(input("want to clear your data:\n"))

user_data = {
    "name": "ali",
    "age": "20"
}

cop_data = user_data.copy()
print (cop_data)

if x == "yes":
    print(user_data.clear())
elif x == "no":
    print(user_data)

for x in user_data.values():
    print(x)

