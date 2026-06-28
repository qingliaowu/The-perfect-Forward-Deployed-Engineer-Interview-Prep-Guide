"""Customer ticket triage exercise for FDE / Solutions / Product Engineer prep.

Run:
    python3 customer_ticket_triage.py --demo
    python3 customer_ticket_triage.py --input tickets.json

Input shape:
[
  {
    "id": "T-100",
    "customer": "Acme Corp",
    "severity": "high",
    "subject": "Sync failing",
    "description": "All Salesforce records fail to sync",
    "tags": ["integration", "salesforce"],
    "arr": 250000
  }
]
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from enum import Enum
import json
from pathlib import Path
from typing import Any


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


SEVERITY_POINTS = {
    Severity.LOW: 10,
    Severity.MEDIUM: 30,
    Severity.HIGH: 60,
    Severity.CRITICAL: 90,
}

KEYWORD_POINTS = {
    "down": 25,
    "outage": 25,
    "blocked": 20,
    "security": 30,
    "data loss": 40,
    "cannot login": 20,
    "sync": 15,
}


@dataclass(frozen=True)
class Ticket:
    id: str
    customer: str
    severity: Severity
    subject: str
    description: str
    tags: tuple[str, ...]
    arr: int


@dataclass(frozen=True)
class TriageResult:
    ticket: Ticket
    score: int
    action: str


def parse_ticket(raw: dict[str, Any]) -> Ticket:
    required = ["id", "customer", "severity", "subject", "description"]
    missing = [field for field in required if field not in raw]
    if missing:
        raise ValueError(f"ticket missing fields: {', '.join(missing)}")

    try:
        severity = Severity(str(raw["severity"]).lower())
    except ValueError as exc:
        allowed = ", ".join(item.value for item in Severity)
        raise ValueError(f"invalid severity {raw['severity']!r}; expected {allowed}") from exc

    tags = tuple(str(tag).strip().lower() for tag in raw.get("tags", []) if str(tag).strip())
    arr = int(raw.get("arr", 0))
    return Ticket(
        id=str(raw["id"]).strip(),
        customer=str(raw["customer"]).strip(),
        severity=severity,
        subject=str(raw["subject"]).strip(),
        description=str(raw["description"]).strip(),
        tags=tags,
        arr=arr,
    )


def keyword_score(ticket: Ticket) -> int:
    text = f"{ticket.subject} {ticket.description}".lower()
    return sum(points for keyword, points in KEYWORD_POINTS.items() if keyword in text)


def arr_score(arr: int) -> int:
    if arr >= 500_000:
        return 30
    if arr >= 100_000:
        return 20
    if arr >= 25_000:
        return 10
    return 0


def recommend_action(score: int) -> str:
    if score >= 120:
        return "page on-call engineer and create customer-facing incident update"
    if score >= 90:
        return "assign senior engineer and schedule same-day customer update"
    if score >= 60:
        return "prioritize in current sprint and request reproduction details"
    if score >= 30:
        return "route to support queue with product-area tag"
    return "acknowledge and monitor for duplicates"


def triage(ticket: Ticket) -> TriageResult:
    score = SEVERITY_POINTS[ticket.severity] + keyword_score(ticket) + arr_score(ticket.arr)
    if "vip" in ticket.tags:
        score += 15
    if "security" in ticket.tags:
        score += 20
    return TriageResult(ticket=ticket, score=score, action=recommend_action(score))


def summarize(results: list[TriageResult]) -> dict[str, Any]:
    by_customer: dict[str, list[TriageResult]] = {}
    for result in results:
        by_customer.setdefault(result.ticket.customer, []).append(result)

    return {
        "ticket_count": len(results),
        "highest_priority": [
            {
                "id": result.ticket.id,
                "customer": result.ticket.customer,
                "score": result.score,
                "action": result.action,
            }
            for result in sorted(results, key=lambda item: item.score, reverse=True)[:5]
        ],
        "customers": {
            customer: {
                "ticket_count": len(customer_results),
                "max_score": max(result.score for result in customer_results),
            }
            for customer, customer_results in sorted(by_customer.items())
        },
    }


def demo_tickets() -> list[dict[str, Any]]:
    return [
        {
            "id": "T-100",
            "customer": "Acme Corp",
            "severity": "critical",
            "subject": "Production sync outage",
            "description": "All CRM sync jobs are down after token rotation.",
            "tags": ["integration", "vip"],
            "arr": 750000,
        },
        {
            "id": "T-101",
            "customer": "Northwind",
            "severity": "medium",
            "subject": "Dashboard export is slow",
            "description": "Finance team says CSV export takes 45 seconds.",
            "tags": ["analytics"],
            "arr": 80000,
        },
        {
            "id": "T-102",
            "customer": "Globex",
            "severity": "high",
            "subject": "Security review question",
            "description": "Need clarification on audit log retention before launch.",
            "tags": ["security"],
            "arr": 200000,
        },
    ]


def load_tickets(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError("input JSON must be a list of ticket objects")
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description="Prioritize customer tickets.")
    parser.add_argument("--input", type=Path, help="Path to ticket JSON file")
    parser.add_argument("--demo", action="store_true", help="Run with built-in demo tickets")
    args = parser.parse_args()

    if args.demo:
        raw_tickets = demo_tickets()
    elif args.input:
        raw_tickets = load_tickets(args.input)
    else:
        parser.error("provide --demo or --input tickets.json")

    tickets = [parse_ticket(raw) for raw in raw_tickets]
    results = [triage(ticket) for ticket in tickets]
    print(json.dumps(summarize(results), indent=2))


if __name__ == "__main__":
    main()

