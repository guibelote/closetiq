
from app.services.combination_engine import generate_combinations
from app.services.scoring_engine import score_look

def generate_best_looks(items, temperature, desired_style, limit=5):

    combinations = generate_combinations(items)

    scored = []

    for look in combinations:
        score = score_look(look, temperature, desired_style)

        scored.append({
            "look": look,
            "score": score
        })

    ranked = sorted(scored, key=lambda x: x["score"], reverse=True)

    return ranked[:limit]
