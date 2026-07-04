# Foundations: Python, JavaScript, TypeScript, and SQL

Customer-Facing AI Engineer interviews often look AI-heavy, but the basics still decide whether you can actually build, debug, and explain. This track gives you the practical foundation to support RAG, agents, evals, APIs, dashboards, and customer data workflows.

## How To Use This Track

Run the drills:

```bash
python3 python_foundations_drills.py
node javascript_basics_drills.js
sqlite3 < sql_basics_drills.sql
```

Read the TypeScript drill:

```bash
cat typescript_basics_drills.ts
```

Target bar:

- You can explain every line.
- You can modify each drill without breaking it.
- You can connect each concept to a customer-facing AI workflow.

## Python Basics

Why it matters:

- Python is the default language for AI prototyping, evals, data scripts, integrations, and internal tools.

Must know:

- variables and control flow
- functions and return values
- lists, dictionaries, sets, tuples
- comprehensions
- classes and dataclasses
- type hints
- exceptions
- file I/O
- JSON and CSV
- CLI arguments
- basic testing mindset

Practice tasks:

- Parse customer ticket JSON.
- Normalize inconsistent customer names.
- Count active users by feature.
- Rank tickets by severity and revenue.
- Validate malformed API payloads.
- Refuse unsafe or low-confidence AI outputs.

Interview explanation pattern:

```text
I would keep parsing, validation, scoring, and output formatting separate so each part can be tested. For production, I would add structured logs, schema validation, retries around external calls, and metrics for success/failure counts.
```

## JavaScript Basics

Why it matters:

- Many AI products expose web apps, browser extensions, frontend surfaces, SDKs, and API clients.
- Cursor-style and product engineering interviews may expect you to reason about frontend state and async API calls.

Must know:

- `let` and `const`
- arrays and objects
- functions and arrow functions
- destructuring
- spread syntax
- `map`, `filter`, `reduce`
- promises
- `async` / `await`
- error handling
- modules
- JSON handling

Practice tasks:

- Fetch all pages from a paginated API.
- Transform API responses into UI rows.
- Validate a customer intake form.
- Group tickets by status.
- Safely handle failed requests.

Interview explanation pattern:

```text
I would keep the API client small and typed at the boundary, normalize the response into a UI-friendly shape, and make loading/error/empty states explicit.
```

## TypeScript Basics

Why it matters:

- TypeScript lets you model API contracts, AI structured outputs, tool parameters, and UI state safely.
- It is especially relevant for Cursor, product engineering, frontend-heavy AI products, and SDK work.

Must know:

- primitive types
- arrays and records
- interfaces
- type aliases
- optional fields
- union types
- discriminated unions
- narrowing
- generics
- `unknown` vs `any`
- typed API results

Practice tasks:

- Model an AI workflow request.
- Type a support ticket payload.
- Type structured model output.
- Create a generic `groupBy` helper.
- Use discriminated unions for success/error responses.
- Narrow risky action types before execution.

Interview explanation pattern:

```text
I would type the boundary between the model and application very carefully. The model can produce structured output, but the application must validate and narrow it before taking action.
```

## SQL Basics

Why it matters:

- Customer-facing AI work often starts with customer data: usage, tickets, billing, logs, documents, feedback, and eval results.
- SQL helps you measure adoption, debug data quality, and prove ROI.

Must know:

- `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`
- `GROUP BY` and aggregates
- `JOIN`
- `CASE`
- `COALESCE`
- CTEs with `WITH`
- window functions
- date/time filtering
- data quality checks

Practice tasks:

- Count support tickets by severity.
- Find customers with rising ticket volume.
- Calculate feature adoption by account.
- Join tickets to accounts and ARR.
- Identify stale documents in a RAG index.
- Measure AI answer correction rate.

Interview explanation pattern:

```text
I would first define the metric precisely, then write the simplest query that proves it. After that I would check data freshness, missing values, duplicate events, and whether the metric can be segmented by customer, plan, or workflow.
```

## 2-Week Basics Sprint

### Days 1-2: Python

- Run and modify `python_foundations_drills.py`.
- Add one new field to the usage event.
- Add validation for missing timestamps.
- Explain the difference between a list, dict, set, and tuple.

### Days 3-4: JavaScript

- Run and modify `javascript_basics_drills.js`.
- Add one more API page to the mock client.
- Add an error case.
- Explain `map`, `filter`, `reduce`, and `async` / `await`.

### Days 5-6: TypeScript

- Read `typescript_basics_drills.ts`.
- Add one new model action type.
- Add one new API result variant.
- Explain discriminated unions and why `unknown` is safer than `any`.

### Days 7-8: SQL

- Run `sqlite3 < sql_basics_drills.sql`.
- Add a new customer, tickets, and events.
- Write one new query for AI answer quality.
- Explain joins, grouping, CTEs, and window functions.

### Days 9-10: Integration

Build a tiny end-to-end workflow:

1. SQL query finds a customer with high ticket volume.
2. Python script summarizes the tickets.
3. JavaScript function formats the result for a UI.
4. TypeScript type defines the response contract.

## Readiness Checklist

You are ready when you can:

- write Python without looking up basic syntax
- explain async JavaScript clearly
- model API responses in TypeScript
- write SQL joins and aggregations
- debug malformed JSON
- explain how data quality affects AI output
- connect language fundamentals to customer-facing AI systems

