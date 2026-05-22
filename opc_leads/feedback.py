from __future__ import annotations

from collections import Counter
from typing import Any


def summarize_feedback(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate human feedback records for continuous optimization.

    Expected fields per record:
    - target_class: A_OPC / B_ENERGY
    - priority_tier: P1/P2/P3
    - outcome: replied/meeting/proposal/won/lost/no_response
    - quality_label: good_fit/weak_fit/noise
    """
    total = len(records)
    if total == 0:
        return {
            "total": 0,
            "reply_rate": 0.0,
            "meeting_rate": 0.0,
            "won_rate": 0.0,
            "quality_breakdown": {},
            "outcome_breakdown": {},
            "suggestions": ["Collect at least 20 reviewed leads before tuning thresholds."],
        }

    outcome_counter = Counter((r.get("outcome") or "unknown") for r in records)
    quality_counter = Counter((r.get("quality_label") or "unknown") for r in records)

    reply_rate = outcome_counter.get("replied", 0) / total
    meeting_rate = outcome_counter.get("meeting", 0) / total
    won_rate = outcome_counter.get("won", 0) / total

    suggestions: list[str] = []
    if quality_counter.get("noise", 0) / total > 0.25:
        suggestions.append("Reduce broad keywords and increase decision-level weight.")
    if reply_rate < 0.15:
        suggestions.append("Refresh outreach copy and tighten P1 criteria.")
    if meeting_rate < 0.08:
        suggestions.append("Improve offer-fit extraction and CTA clarity.")
    if not suggestions:
        suggestions.append("Keep current rules; run another feedback cycle.")

    return {
        "total": total,
        "reply_rate": round(reply_rate, 4),
        "meeting_rate": round(meeting_rate, 4),
        "won_rate": round(won_rate, 4),
        "quality_breakdown": dict(quality_counter),
        "outcome_breakdown": dict(outcome_counter),
        "suggestions": suggestions,
    }
