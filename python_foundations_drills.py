"""Python 3 foundations drills for FDE / Field / Solutions / Product Engineer prep.

Run:
    python3 python_foundations_drills.py

The file is intentionally self-contained and standard-library only.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
import json
from pathlib import Path
from typing import Any, Iterable


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class UsageEvent:
    customer: str
    user_id: str
    feature: str
    timestamp: datetime


def parse_iso_datetime(value: str) -> datetime:
    """Parse a basic ISO-8601 timestamp and normalize it to UTC."""
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def normalize_customer_name(value: str) -> str:
    return " ".join(value.strip().split()).title()


def parse_usage_events(raw_events: Iterable[dict[str, Any]]) -> list[UsageEvent]:
    events: list[UsageEvent] = []
    for index, raw in enumerate(raw_events):
        try:
            event = UsageEvent(
                customer=normalize_customer_name(str(raw["customer"])),
                user_id=str(raw["user_id"]).strip(),
                feature=str(raw["feature"]).strip().lower(),
                timestamp=parse_iso_datetime(str(raw["timestamp"])),
            )
        except KeyError as exc:
            raise ValueError(f"event {index} is missing required field {exc}") from exc

        if not event.customer or not event.user_id or not event.feature:
            raise ValueError(f"event {index} has an empty required field")
        events.append(event)
    return events


def group_events_by_customer(events: Iterable[UsageEvent]) -> dict[str, list[UsageEvent]]:
    grouped: dict[str, list[UsageEvent]] = defaultdict(list)
    for event in events:
        grouped[event.customer].append(event)
    return dict(grouped)


def top_features(events: Iterable[UsageEvent], limit: int = 3) -> list[tuple[str, int]]:
    counts = Counter(event.feature for event in events)
    return counts.most_common(limit)


def active_users(events: Iterable[UsageEvent]) -> set[str]:
    return {event.user_id for event in events}


def adoption_summary(events: list[UsageEvent]) -> dict[str, Any]:
    by_customer = group_events_by_customer(events)
    return {
        customer: {
            "event_count": len(customer_events),
            "active_users": len(active_users(customer_events)),
            "top_features": top_features(customer_events),
        }
        for customer, customer_events in sorted(by_customer.items())
    }


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def demo() -> None:
    raw_events = [
        {
            "customer": " acme corp ",
            "user_id": "u-001",
            "feature": "Dashboard",
            "timestamp": "2026-06-28T10:00:00Z",
        },
        {
            "customer": "ACME   CORP",
            "user_id": "u-002",
            "feature": "Export",
            "timestamp": "2026-06-28T10:05:00Z",
        },
        {
            "customer": "Northwind",
            "user_id": "u-003",
            "feature": "Dashboard",
            "timestamp": "2026-06-28T11:00:00+00:00",
        },
        {
            "customer": "Acme Corp",
            "user_id": "u-001",
            "feature": "Dashboard",
            "timestamp": "2026-06-28T12:00:00Z",
        },
    ]
    events = parse_usage_events(raw_events)
    print(json.dumps(adoption_summary(events), indent=2, default=str))


if __name__ == "__main__":
    demo()

