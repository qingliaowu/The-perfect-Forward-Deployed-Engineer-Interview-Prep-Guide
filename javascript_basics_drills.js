"use strict";

// JavaScript basics for customer-facing AI engineering.
//
// Run:
//   node javascript_basics_drills.js

const tickets = [
  {
    id: "T-100",
    customer: "Acme Corp",
    severity: "critical",
    tags: ["integration", "vip"],
    arr: 750000,
  },
  {
    id: "T-101",
    customer: "Northwind",
    severity: "medium",
    tags: ["analytics"],
    arr: 80000,
  },
  {
    id: "T-102",
    customer: "Globex",
    severity: "high",
    tags: ["security"],
    arr: 200000,
  },
];

const severityPoints = {
  low: 10,
  medium: 30,
  high: 60,
  critical: 90,
};

function scoreTicket(ticket) {
  const base = severityPoints[ticket.severity] ?? 0;
  const revenueBoost = ticket.arr >= 500000 ? 30 : ticket.arr >= 100000 ? 20 : 0;
  const vipBoost = ticket.tags.includes("vip") ? 15 : 0;
  return base + revenueBoost + vipBoost;
}

function groupBy(items, keyFn) {
  return items.reduce((groups, item) => {
    const key = keyFn(item);
    groups[key] = groups[key] ?? [];
    groups[key].push(item);
    return groups;
  }, {});
}

function summarizeTickets(rawTickets) {
  const scored = rawTickets.map((ticket) => ({
    ...ticket,
    score: scoreTicket(ticket),
  }));

  const highPriority = scored
    .filter((ticket) => ticket.score >= 80)
    .sort((left, right) => right.score - left.score);

  return {
    ticketCount: scored.length,
    highPriority,
    byCustomer: groupBy(scored, (ticket) => ticket.customer),
  };
}

async function fetchPage(cursor) {
  const pages = {
    start: { items: ["doc-1", "doc-2"], nextCursor: "page-2" },
    "page-2": { items: ["doc-3"], nextCursor: null },
  };
  await new Promise((resolve) => setTimeout(resolve, 5));
  return pages[cursor ?? "start"];
}

async function fetchAllPages() {
  const items = [];
  let cursor = null;

  do {
    const page = await fetchPage(cursor);
    items.push(...page.items);
    cursor = page.nextCursor;
  } while (cursor);

  return items;
}

async function main() {
  console.log(JSON.stringify(summarizeTickets(tickets), null, 2));
  const documentIds = await fetchAllPages();
  console.log(JSON.stringify({ documentIds }, null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});

