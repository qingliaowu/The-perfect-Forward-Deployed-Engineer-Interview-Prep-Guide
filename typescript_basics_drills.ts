// TypeScript basics for customer-facing AI engineering.
//
// This file is intentionally dependency-free. Read it as a typed reference or
// compile it in your own TypeScript setup.

type Severity = "low" | "medium" | "high" | "critical";
type RiskLevel = "low" | "medium" | "high";

interface SupportTicket {
  id: string;
  customer: string;
  severity: Severity;
  subject: string;
  body: string;
  tags: string[];
  arr?: number;
}

interface Citation {
  documentId: string;
  title: string;
  quote: string;
}

type AiAnswer =
  | {
      kind: "answered";
      ticketId: string;
      confidence: number;
      response: string;
      citations: Citation[];
    }
  | {
      kind: "escalated";
      ticketId: string;
      reason: string;
      riskLevel: RiskLevel;
    };

type ApiResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string; retryable: boolean };

interface ToolCall {
  name: "search_docs" | "create_ticket" | "summarize_account";
  arguments: Record<string, unknown>;
  requiresApproval: boolean;
}

function isHighSeverity(ticket: SupportTicket): boolean {
  return ticket.severity === "high" || ticket.severity === "critical";
}

function renderAnswer(answer: AiAnswer): string {
  switch (answer.kind) {
    case "answered":
      return `${answer.response} (${answer.citations.length} citations)`;
    case "escalated":
      return `Escalated: ${answer.reason}`;
  }
}

function groupBy<T, K extends string | number>(items: T[], keyFn: (item: T) => K): Record<K, T[]> {
  return items.reduce(
    (groups, item) => {
      const key = keyFn(item);
      groups[key] = groups[key] ?? [];
      groups[key].push(item);
      return groups;
    },
    {} as Record<K, T[]>,
  );
}

function parseUnknownTicket(value: unknown): ApiResult<SupportTicket> {
  if (typeof value !== "object" || value === null) {
    return { ok: false, error: "ticket must be an object", retryable: false };
  }

  const candidate = value as Partial<SupportTicket>;
  if (!candidate.id || !candidate.customer || !candidate.severity) {
    return { ok: false, error: "ticket missing required fields", retryable: false };
  }

  return {
    ok: true,
    data: {
      id: candidate.id,
      customer: candidate.customer,
      severity: candidate.severity,
      subject: candidate.subject ?? "",
      body: candidate.body ?? "",
      tags: candidate.tags ?? [],
      arr: candidate.arr,
    },
  };
}

function shouldRequireHumanApproval(call: ToolCall): boolean {
  return call.requiresApproval || call.name === "create_ticket";
}

const demoTicket: SupportTicket = {
  id: "T-100",
  customer: "Acme Corp",
  severity: "critical",
  subject: "Salesforce sync outage",
  body: "All records stopped syncing after token rotation.",
  tags: ["integration", "vip"],
  arr: 750000,
};

const demoAnswer: AiAnswer = isHighSeverity(demoTicket)
  ? {
      kind: "escalated",
      ticketId: demoTicket.id,
      reason: "critical customer impact",
      riskLevel: "high",
    }
  : {
      kind: "answered",
      ticketId: demoTicket.id,
      confidence: 0.82,
      response: "Please check the connector status and OAuth token rotation logs.",
      citations: [],
    };

renderAnswer(demoAnswer);
groupBy([demoTicket], (ticket) => ticket.customer);
parseUnknownTicket(demoTicket);
shouldRequireHumanApproval({
  name: "create_ticket",
  arguments: { customer: demoTicket.customer },
  requiresApproval: true,
});

