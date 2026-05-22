from __future__ import annotations

from typing import Any

PRIORITY_ORDER = {"P1": 0, "P2": 1, "P3": 2}


def build_queue(leads: list[dict[str, Any]]) -> list[dict[str, Any]]:
    enriched = []
    for lead in leads:
        lead = dict(lead)
        target = lead.get("target_class", "UNKNOWN")
        if target == "A_OPC":
            lead["message_angle"] = "AI提效与品牌放大"
        elif target == "B_ENERGY":
            lead["message_angle"] = "流程效率与供应链响应优化"
        else:
            lead["message_angle"] = "探索性沟通"
        enriched.append(lead)

    return sorted(
        enriched,
        key=lambda x: (PRIORITY_ORDER.get(x.get("priority_tier", "P3"), 9), -int(x.get("opportunity_score", 0))),
    )
