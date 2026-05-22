# OPC Leads Engine (MVP)

This module operationalizes `overseas_channel_automation.md` into an executable pipeline for two target classes:
- `A_OPC`: EU/SEA OPC individuals and small commercial entities.
- `B_ENERGY`: EU energy practitioners with decision influence.

## Quick start
```bash
python3 opc_leads/main.py --input opc_leads/data/sample_raw.jsonl --output opc_leads/data/daily_outreach.json
```

## Pipeline
1. Normalize raw records into unified lead schema.
2. Classify into `A_OPC` / `B_ENERGY`.
3. Score opportunity and assign priority tier (`P1/P2/P3`).
4. Build daily outreach queue sorted by priority and score.
