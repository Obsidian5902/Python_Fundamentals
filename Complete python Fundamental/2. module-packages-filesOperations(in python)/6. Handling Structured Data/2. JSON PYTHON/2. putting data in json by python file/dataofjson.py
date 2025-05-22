import json # just importing tha data from python file to json file....
userinfo = {'name': 'Harsh Yadav', 'city': 'Alwar', "age":44, "country": "India"}
with open("writedatafrompython.json", "r+") as f:
    json.dump(userinfo, f)
