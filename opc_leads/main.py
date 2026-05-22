from __future__ import annotations

import argparse
import json
from pathlib import Path

from opc_leads.classifier.rules import classify_target
from opc_leads.outreach_queue.builder import build_queue
from opc_leads.scorer.scoring import score_opportunity


def run(input_path: Path, output_path: Path) -> None:
    leads = []
    with input_path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            raw = json.loads(line)
            text = raw.get("text", "")
            region = raw.get("region", "EU")

            cls = classify_target(text, region=region)
            decision_level = raw.get("decision_level", "specialist")
            demand_strength = int(raw.get("demand_strength", min(100, len(cls.signals) * 20)))
            pain_strength = int(raw.get("pain_strength", 60 if cls.target_class == "A_OPC" else 50))
            contact_reachable = bool(raw.get("contact_hint"))

            score, tier = score_opportunity(
                decision_level=decision_level,
                demand_strength=demand_strength,
                pain_strength=pain_strength,
                contact_reachable=contact_reachable,
            )

            leads.append(
                {
                    **raw,
                    "target_class": cls.target_class,
                    "intent_signal": cls.signals,
                    "opportunity_score": score,
                    "priority_tier": tier,
                }
            )

    queue = build_queue(leads)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(queue, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    run(Path(args.input), Path(args.output))
