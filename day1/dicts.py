#dict
profile = {
    "name" : "Adir",
    "age" : 25,
    "years_exp" : 4,
    "top_skill" : "Details"
}

print(profile)

print(profile["top_skill"])

profile["target_role"] = "Engineer"

for k, v in profile.items():
    print(f"{k} : {v}")
