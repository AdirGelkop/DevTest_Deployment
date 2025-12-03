years_exp = 4

def get_level(years):
    if years < 2:
        print("Junior")
    elif years < 5:
        print("Mid")
    else:
        print("Senior")

get_level(years_exp)