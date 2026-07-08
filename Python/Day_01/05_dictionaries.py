
analyst_profile = {
    "name": "Dinesh",
    "role": "Data Analyst",
    "experience": 2,
    "tools": ["Python", "SQL", "Tableau"]
}

print(type(analyst_profile)) 
print(analyst_profile["role"]) 
print(analyst_profile["tools"][1])

#
print(analyst_profile.get("salary", "Key Not Found!")) 


analyst_profile["experience"] = 3 
analyst_profile["location"] = "Chennai" 

print(analyst_profile)


print(analyst_profile.keys()) 


print(analyst_profile.values()) 


print(analyst_profile.items())

user_profile = {"name": "Dinesh", "role": "Analyst", "location": "Chennai"}

removed_value = user_profile.pop("location")

print(f"Removed Data: {removed_value}") 
print(user_profile)

user_profile = {"name": "Dinesh", "role": "Analyst", "location": "Chennai"}


del user_profile["role"]

print(user_profile)

user_profile = {"name": "Dinesh", "role": "Analyst", "location": "Chennai"}

user_profile.clear()

print(user_profile) 

user_profile = {"name": "Dinesh"}

status = user_profile.pop("salary", "Key already missing bro!")
print(status)