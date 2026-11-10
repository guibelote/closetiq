
import itertools

def generate_combinations(items):

    tops = [i for i in items if i["category"] == "top"]
    bottoms = [i for i in items if i["category"] == "bottom"]
    shoes = [i for i in items if i["category"] == "shoes"]

    combinations = []

    for t,b,s in itertools.product(tops,bottoms,shoes):
        combinations.append([t,b,s])

    return combinations
