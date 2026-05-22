from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from opc_leads.config import keywords


@dataclass
class ClassificationResult:
    target_class: str
    signals: list[str]


def _count_matches(text: str, phrases: Iterable[str]) -> list[str]:
    t = text.lower()
    return [p for p in phrases if p in t]


def classify_target(text: str, region: str = "EU") -> ClassificationResult:
    a_hits = (
        _count_matches(text, keywords.A_IDENTITY)
        + _count_matches(text, keywords.A_COMMERCIAL)
        + _count_matches(text, keywords.A_PAIN)
    )
    b_hits = (
        _count_matches(text, keywords.B_IDENTITY)
        + _count_matches(text, keywords.B_DEMAND)
        + _count_matches(text, keywords.B_DOMAIN)
    )

    if len(b_hits) >= len(a_hits) and b_hits:
        return ClassificationResult(target_class="B_ENERGY", signals=b_hits)

    if a_hits:
        # SEA currently focuses on A_OPC per plan.
        if region.upper() == "SEA":
            return ClassificationResult(target_class="A_OPC", signals=a_hits)
        return ClassificationResult(target_class="A_OPC", signals=a_hits)

    return ClassificationResult(target_class="A_OPC" if region.upper() == "SEA" else "UNKNOWN", signals=[])
