#funcs
def calc_start_age(current_age, experience):
    return (current_age-experience)

def summarize_profile(name, role, years):
    return f"{name} is currently a {role} with {years} years of exp"

print(calc_start_age(25, 4))
print(summarize_profile("adir", "solutions architect", 4))
