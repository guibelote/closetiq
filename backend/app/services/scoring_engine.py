
from app.services.color_engine import COLOR_MATCH

def score_look(look, temperature, desired_style):

    score = 0

    colors = [item["color"] for item in look]

    base = colors[0]

    matches = COLOR_MATCH.get(base, [])

    for c in colors[1:]:
        if c in matches:
            score += 10

    if temperature > 25:
        score += 5

    return score
