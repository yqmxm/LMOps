"""Runtime environment configuration for the lead agent pipeline."""

from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AgentEnv:
    run_mode: str
    region_focus: str
    max_daily_outreach: int
    feedback_min_samples: int


def load_agent_env() -> AgentEnv:
    return AgentEnv(
        run_mode=os.getenv("OPC_RUN_MODE", "dev"),
        region_focus=os.getenv("OPC_REGION_FOCUS", "EU,SEA"),
        max_daily_outreach=int(os.getenv("OPC_MAX_DAILY_OUTREACH", "50")),
        feedback_min_samples=int(os.getenv("OPC_FEEDBACK_MIN_SAMPLES", "20")),
    )
