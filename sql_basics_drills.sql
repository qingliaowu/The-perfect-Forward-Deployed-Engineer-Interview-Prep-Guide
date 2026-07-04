-- SQL basics for customer-facing AI engineering.
--
-- Run:
--   sqlite3 < sql_basics_drills.sql

.headers on
.mode column

DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS usage_events;
DROP TABLE IF EXISTS ai_answers;

CREATE TABLE accounts (
  account_id TEXT PRIMARY KEY,
  customer_name TEXT NOT NULL,
  plan TEXT NOT NULL,
  arr INTEGER NOT NULL
);

CREATE TABLE tickets (
  ticket_id TEXT PRIMARY KEY,
  account_id TEXT NOT NULL,
  severity TEXT NOT NULL,
  subject TEXT NOT NULL,
  created_at TEXT NOT NULL,
  resolved_at TEXT,
  FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

CREATE TABLE usage_events (
  event_id TEXT PRIMARY KEY,
  account_id TEXT NOT NULL,
  user_id TEXT NOT NULL,
  feature TEXT NOT NULL,
  occurred_at TEXT NOT NULL,
  FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

CREATE TABLE ai_answers (
  answer_id TEXT PRIMARY KEY,
  ticket_id TEXT NOT NULL,
  confidence REAL NOT NULL,
  escalated INTEGER NOT NULL,
  corrected_by_human INTEGER NOT NULL,
  created_at TEXT NOT NULL,
  FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id)
);

INSERT INTO accounts VALUES
  ('A-1', 'Acme Corp', 'enterprise', 750000),
  ('A-2', 'Globex', 'enterprise', 200000),
  ('A-3', 'Northwind', 'business', 80000);

INSERT INTO tickets VALUES
  ('T-100', 'A-1', 'critical', 'Salesforce sync outage', '2026-07-01', '2026-07-01'),
  ('T-101', 'A-1', 'high', 'SSO login failures', '2026-07-02', NULL),
  ('T-102', 'A-2', 'high', 'Security review docs', '2026-07-02', '2026-07-03'),
  ('T-103', 'A-3', 'medium', 'Dashboard export slow', '2026-07-03', NULL);

INSERT INTO usage_events VALUES
  ('E-1', 'A-1', 'u-1', 'support_agent', '2026-07-01'),
  ('E-2', 'A-1', 'u-2', 'support_agent', '2026-07-01'),
  ('E-3', 'A-1', 'u-1', 'eval_dashboard', '2026-07-02'),
  ('E-4', 'A-2', 'u-3', 'security_review', '2026-07-02'),
  ('E-5', 'A-3', 'u-4', 'analytics_export', '2026-07-03');

INSERT INTO ai_answers VALUES
  ('ANS-1', 'T-100', 0.66, 0, 0, '2026-07-01'),
  ('ANS-2', 'T-101', 0.41, 1, 1, '2026-07-02'),
  ('ANS-3', 'T-102', 0.78, 0, 0, '2026-07-02'),
  ('ANS-4', 'T-103', 0.52, 1, 0, '2026-07-03');

-- 1. Tickets joined to account value.
SELECT
  t.ticket_id,
  a.customer_name,
  a.arr,
  t.severity,
  t.subject
FROM tickets t
JOIN accounts a ON a.account_id = t.account_id
ORDER BY a.arr DESC, t.created_at DESC;

-- 2. Ticket count by severity.
SELECT
  severity,
  COUNT(*) AS ticket_count
FROM tickets
GROUP BY severity
ORDER BY ticket_count DESC;

-- 3. Feature adoption by account.
SELECT
  a.customer_name,
  u.feature,
  COUNT(DISTINCT u.user_id) AS active_users
FROM usage_events u
JOIN accounts a ON a.account_id = u.account_id
GROUP BY a.customer_name, u.feature
ORDER BY a.customer_name, active_users DESC;

-- 4. AI quality metrics by customer.
SELECT
  a.customer_name,
  COUNT(ans.answer_id) AS ai_answer_count,
  ROUND(AVG(ans.confidence), 2) AS avg_confidence,
  ROUND(AVG(ans.escalated), 2) AS escalation_rate,
  ROUND(AVG(ans.corrected_by_human), 2) AS correction_rate
FROM ai_answers ans
JOIN tickets t ON t.ticket_id = ans.ticket_id
JOIN accounts a ON a.account_id = t.account_id
GROUP BY a.customer_name
ORDER BY correction_rate DESC, avg_confidence ASC;

-- 5. CTE for high-priority unresolved tickets.
WITH unresolved AS (
  SELECT
    t.ticket_id,
    a.customer_name,
    a.arr,
    t.severity,
    t.subject
  FROM tickets t
  JOIN accounts a ON a.account_id = t.account_id
  WHERE t.resolved_at IS NULL
)
SELECT *
FROM unresolved
WHERE severity IN ('critical', 'high') OR arr >= 100000
ORDER BY arr DESC;

-- 6. Window function to rank accounts by ticket volume.
WITH account_ticket_counts AS (
  SELECT
    a.customer_name,
    COUNT(t.ticket_id) AS ticket_count
  FROM accounts a
  LEFT JOIN tickets t ON t.account_id = a.account_id
  GROUP BY a.customer_name
)
SELECT
  customer_name,
  ticket_count,
  RANK() OVER (ORDER BY ticket_count DESC) AS ticket_volume_rank
FROM account_ticket_counts;
