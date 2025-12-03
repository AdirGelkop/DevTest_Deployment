def is_qual(candidate):
    if candidate["exp"] >= 3:
        return True
    else:
        return False

def get_level(years):
    if years < 2:
        print("Junior")
    elif years < 5:
        print("Mid")
    else:
        print("Senior")

app1 = {
    "name" : "adir",
    "age" : 25,
    "exp" : 4,
    "skill" : "Details"
}
app2 = {
    "name" : "moshe",
    "age" : 30,
    "exp" : 2,
    "skill" : "RF"
}
app3 = {
    "name" : "nir",
    "age" : 12,
    "exp" : 11,
    "skill" : "network"
}

applicants = [app1, app2, app3]

for app in applicants:
    print(app["name"])
    print(f"Qualified? {is_qual(app)}")
    get_level(app["exp"])
