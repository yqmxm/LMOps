from __future__ import annotations


def score_opportunity(*, decision_level: str, demand_strength: int, pain_strength: int, contact_reachable: bool) -> tuple[int, str]:
    decision_weight = {
        "founder": 100,
        "director": 95,
        "head": 90,
        "manager": 75,
        "lead": 70,
        "specialist": 55,
        "analyst": 45,
    }.get(decision_level.lower(), 40)

    demand = max(0, min(demand_strength, 100))
    pain = max(0, min(pain_strength, 100))
    reach = 100 if contact_reachable else 30

    score = round(decision_weight * 0.30 + demand * 0.30 + pain * 0.20 + reach * 0.20)

    if score >= 80 and contact_reachable:
        tier = "P1"
    elif score >= 60:
        tier = "P2"
    else:
        tier = "P3"

    return score, tier
