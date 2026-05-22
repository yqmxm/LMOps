# OPC Leads Engine (MVP)

This module operationalizes `overseas_channel_automation.md` into an executable pipeline for two target classes:
- `A_OPC`: EU/SEA OPC individuals and small commercial entities.
- `B_ENERGY`: EU energy practitioners with decision influence.

## Agent environment
Environment variables:
- `OPC_RUN_MODE` (`dev`/`prod`)
- `OPC_REGION_FOCUS` (default `EU,SEA`)
- `OPC_MAX_DAILY_OUTREACH` (default `50`)
- `OPC_FEEDBACK_MIN_SAMPLES` (default `20`)

## Human feedback loop
- Annotators review outreach outcomes and store records in JSON.
- Pipeline generates `feedback_report.json` with reply/meeting/won rates and optimization suggestions.
- Use suggestions to tune keywords, priority thresholds and outreach messaging each cycle.

## Quick start
```bash
python3 -m opc_leads.main \
  --input opc_leads/data/sample_raw.jsonl \
  --output opc_leads/data/daily_outreach.json \
  --feedback opc_leads/data/sample_feedback.json
```

## Pipeline
1. Normalize raw records into unified lead schema.
2. Classify into `A_OPC` / `B_ENERGY`.
3. Score opportunity and assign priority tier (`P1/P2/P3`).
4. Build daily outreach queue sorted by priority and score.
5. Aggregate human feedback for continuous optimization.
