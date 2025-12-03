#list
skills = ["networking", "RF", "TS", "Presales"]

skills.append("python")
skills.append(1)

print(len(skills))
print(skills)

#loops
for skill in skills:
    print(skill)
for i, skill in enumerate(skills):
    print(f"{i} : {skill}")

