# Perfect Customer-Facing AI Engineer Guide

This guide prepares you for Customer-Facing AI Engineer roles, including Forward Deployed AI Engineer, AI Field Engineer, Solutions Architect for AI products, Applied AI Engineer, Product Engineer on AI platforms, and technical AI customer engineer roles.

It is inspired by `qingliaowu/google-fde-interview-guide`, but it goes further. The referenced guide is a useful map for screening, DSA, collaborative coding, behavioral prep, and agentic/ML design. This guide turns that into a role-specific, code-heavy preparation system for engineers who must build AI systems with customers, under ambiguity, with real business constraints.

## What This Role Really Tests

A strong Customer-Facing AI Engineer can:

- turn messy customer goals into a scoped AI workflow
- prototype fast in Python 3
- explain AI trade-offs to executives, engineers, legal, security, and operators
- design RAG, agents, evals, and human-in-the-loop systems
- integrate with customer data, APIs, identity, and deployment environments
- debug model quality, retrieval failures, latency, cost, and reliability
- know when not to use AI
- earn customer trust while staying technically precise

You are not preparing to be only a LeetCode engineer, only a prompt engineer, or only a solutions consultant. You are preparing to be the person who can sit with a customer on Monday, understand the operational pain, build a credible prototype by Wednesday, explain risks on Thursday, and design the path to production on Friday.

## Interview Loop Map

Most loops test some mix of:

- recruiter screen and role motivation
- technical coding in Python
- practical AI prototyping
- system design for AI products
- customer discovery or solutioning
- product sense and trade-offs
- behavioral stories
- executive communication
- debugging and incident response

Your preparation should produce evidence in each category.

## Target Company Strategy

Your target list spans several different Customer-Facing AI Engineer archetypes. Prepare one core portfolio, then tune your interview stories and projects for each company.

### OpenAI

Likely signal:

- deployment engineering for enterprise and government customers
- AI success, AI support, applied AI, Codex, agents, evals, safety, and platform usage
- ability to turn customer pilots into production systems
- strong judgment around model behavior, product constraints, privacy, and customer trust

Prep emphasis:

- build with OpenAI-style APIs conceptually: structured outputs, tool use, evals, tracing, retrieval, agentic workflows
- prepare a production deployment story: pilot, eval, rollout, monitoring, customer adoption
- know how to explain latency, cost, safety, and model selection trade-offs
- show you can work with executives and deeply technical customer teams

Portfolio project:

- Enterprise AI deployment kit: RAG assistant, eval runner, customer rollout plan, and observability dashboard spec.

### Anthropic

Likely signal:

- reliable, trustworthy, secure AI systems
- Claude, Claude Code, agents, customer support, code modernization, enterprise, financial services, healthcare, legal, government, and security use cases
- simple empirical solutions over overbuilt architectures
- thoughtful safety and communication culture

Prep emphasis:

- safety-first architecture: least privilege tools, refusal behavior, human review, audit logs
- code assistant and code modernization workflows
- prompt-injection and data exfiltration defenses
- ability to say “the simplest useful system is...” and justify it

Portfolio project:

- Permission-aware enterprise knowledge assistant with explicit refusal, citations, and prompt-injection tests.

### Cursor / Anysphere

Likely signal:

- AI developer tools
- TypeScript, editor/product engineering, code understanding, agentic coding, debugging, and developer workflows
- taste for high-quality product experience and fast iteration
- ability to reason about how engineers actually use AI while coding

Prep emphasis:

- TypeScript and JavaScript fundamentals matter more here than for many deployment-heavy roles
- build a small codebase-understanding assistant
- practice explaining developer experience trade-offs
- prepare for project-style or product-building interviews

Portfolio project:

- Local code review assistant: parses files, summarizes risks, suggests tests, and produces an eval report for code-change quality.

### SpaceX-Style Applied Engineering Signal

If you meant SpaceX separately, optimize for:

- practical engineering under real operational constraints
- reliability, ownership, debugging, and high agency
- building tools for engineers, operators, hardware teams, or mission-critical workflows

Prep emphasis:

- less hand-wavy AI, more “this tool reduces operational failure”
- incident response stories
- observability and rollback
- strong Python automation and systems thinking

Portfolio project:

- AI incident assistant that ingests logs, retrieves runbooks, proposes hypotheses, and requires human approval for remediation.

### Sierra

Likely signal:

- enterprise customer service agents
- agent architecture, agent builder, identity, enterprise platform, security, compliance, infrastructure, support engineering
- customer trust enablement and production-grade agent behavior

Prep emphasis:

- conversational agents that can complete support workflows safely
- tool-calling, permissions, identity, audit trails, and escalation
- customer service metrics: containment, resolution time, CSAT, correction rate, escalation quality
- enterprise security review readiness

Portfolio project:

- Customer service agent simulator with policy checks, tool approval, escalation, audit logs, and evals.

### ElevenLabs

Likely signal:

- voice AI, conversational agents, speech-to-text, text-to-speech, low-latency real-time systems
- deployment strategy, enterprise solutions engineering, forward deployed software engineering
- ethical awareness and human impact

Prep emphasis:

- voice agent architecture: turn-taking, latency, barge-in, streaming, fallback, transcripts, consent
- API integration and enterprise deployment
- safety around voice cloning, impersonation, consent, and regulated workflows
- async documentation and remote collaboration

Portfolio project:

- Voice support agent design: call flow, transcript summarizer, retrieval, safety policy, latency budget, and eval plan.

### Other Similar Companies

Also prepare for:

- Perplexity-style answer/search systems: retrieval quality, citations, freshness, ranking, user trust
- Harvey-style legal AI: accuracy, confidentiality, workflow-specific review, citation rigor
- Glean-style enterprise search: permissions, connectors, freshness, identity, knowledge graph
- Scale/Surge-style data/evals roles: benchmark design, human labeling, model quality measurement
- Palantir-style FDE roles: customer embeddedness, data integration, operational workflows, rapid deployment
- Notion/GitHub/Microsoft AI product roles: user workflows, product craft, platform integration, enterprise readiness

## Company-to-Skill Matrix

| Company archetype | Highest signal | Must-show project |
| --- | --- | --- |
| OpenAI | deployment, evals, enterprise trust, production AI | AI deployment kit with RAG, evals, rollout, observability |
| Anthropic | safety, reliability, secure agents, simple empirical design | permission-aware RAG with refusal and injection tests |
| Cursor | developer tools, TypeScript, code agents, product taste | code review or codebase-understanding assistant |
| SpaceX-style applied engineering | reliability, automation, ownership, incidents | AI incident/runbook assistant |
| Sierra | customer service agents, tool use, enterprise platform | support agent with policy, tools, escalation, audit logs |
| ElevenLabs | voice agents, real-time UX, deployment, safety | voice agent architecture and eval plan |
| Other enterprise AI | integrations, permissions, ROI, adoption | customer-specific AI pilot with metrics |

## The Core Skill Stack

### 1. Python 3 Engineering

Must know:

- data structures: `list`, `dict`, `set`, `tuple`
- functions, classes, dataclasses, enums
- type hints and clean interfaces
- JSON, CSV, files, `pathlib`
- CLI tools with `argparse`
- HTTP/API concepts
- error handling
- logging
- testing
- simple performance analysis

Why it matters:

- Most customer-facing AI prototypes start as Python scripts, notebooks, CLIs, or small services.
- Interviewers want to see that your code can survive ambiguity and messy input.

Practice:

```bash
python3 python_foundations_drills.py
python3 customer_ticket_triage.py --demo
python3 ai_support_assistant_eval.py --demo
```

### 2. AI Application Architecture

Must know:

- LLM basics: context windows, tokens, temperature, latency, cost
- prompting: instructions, examples, structured output, refusal behavior
- RAG: chunking, embedding, retrieval, reranking, citation, freshness
- agents: tools, planning limits, permissions, audit logs
- evals: golden datasets, regression tests, quality rubrics, human review
- safety: PII, prompt injection, data exfiltration, unsafe automation
- observability: traces, model input/output logs, retrieval logs, cost and latency metrics

Customer-facing framing:

- Do not say “the model is smart.” Say what data it sees, what tools it can call, what it is allowed to decide, how you evaluate it, and what happens when confidence is low.

### 3. Integration and Deployment

Must know:

- REST APIs, auth, pagination, webhooks
- customer data ingestion
- identity and permissions
- tenancy and data isolation
- cloud deployment basics
- monitoring and alerting
- rollout and rollback
- security review workflows

Customer-facing framing:

- The AI feature is usually only 30-50% of the real work. The rest is data access, trust, permissions, evaluation, adoption, and operational fit.

### 4. Product and Customer Judgment

Must know:

- discovery questions
- user segmentation
- success metrics
- MVP scoping
- build vs buy vs configure
- risk-based prioritization
- ROI narrative
- change management

Customer-facing framing:

- A perfect demo that does not map to the customer’s workflow is not a solution.

### 5. Communication

Must know:

- explain a technical design in 2 minutes
- explain the same design to an executive
- push back without sounding dismissive
- ask clarifying questions under pressure
- narrate coding decisions
- summarize trade-offs crisply

## 12-Week Study Plan

### Week 1: Role Baseline and Foundations

Outcomes:

- Understand the Customer-Facing AI Engineer role.
- Set up a Python-first practice repo.
- Build your first story bank.

Study:

- Role comparison: Forward Deployed AI Engineer, Field Engineer, Solutions Architect, Product Engineer.
- Python 3 syntax, functions, collections, dataclasses.
- AI application vocabulary: RAG, agents, evals, guardrails, latency, cost.

Deliverables:

- `story_bank.md` with 10 STAR stories.
- `role_matrix.md` comparing target roles.
- Run the included Python foundation drill.

### Week 2: Python for AI Prototyping

Outcomes:

- Write clean Python scripts that parse, transform, validate, and summarize data.

Study:

- `json`, `csv`, `pathlib`, `argparse`
- `dataclass`, `Enum`, `typing`
- pure functions and testable design
- error handling

Build:

- Customer ticket triage CLI.
- Usage analytics summary.
- Payload validator.

Interview signal:

- You can code a practical customer workflow, not just solve isolated puzzles.

### Week 3: JavaScript and TypeScript Foundations

Outcomes:

- Understand enough frontend and API client code to collaborate across the stack.

JavaScript must know:

- `let`, `const`, functions, arrays, objects
- destructuring and spread
- promises and `async` / `await`
- `fetch`
- modules
- browser form validation basics

TypeScript must know:

- interfaces and type aliases
- union types
- narrowing
- generics
- typed API responses
- `unknown` vs `any`
- discriminated unions

Practice:

```typescript
type AiCaseStatus = "draft" | "needs_review" | "approved" | "blocked";

interface AiWorkflowRequest {
  customerId: string;
  useCase: string;
  dataSources: string[];
  riskLevel: "low" | "medium" | "high";
}

type ApiResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string; retryable: boolean };
```

Interview signal:

- You can reason about typed product surfaces and frontend/backend contracts.

### Week 4: DSA for Practical AI Engineering

Outcomes:

- Build enough algorithm skill for coding interviews and real integration problems.

Focus patterns:

- hash maps and counting
- sliding window
- two pointers
- stack
- BFS and DFS
- heap / priority queue
- intervals
- topological sort
- binary search

AI/customer examples:

- top-k retrieval results with a heap
- dependency ordering for workflow tools
- interval merging for maintenance windows
- graph traversal for document permissions
- hash maps for event aggregation

Weekly target:

- 12 focused problems.
- 2 timed mocks.
- Re-solve every missed problem after 48 hours.

### Week 5: Retrieval-Augmented Generation

Outcomes:

- Design and explain RAG systems with clarity.

Study:

- document ingestion
- chunking strategies
- metadata filters
- embedding and vector search concepts
- reranking
- citations
- freshness
- permission-aware retrieval

Build:

- A simple local retrieval prototype using keyword scoring or lightweight similarity.
- Add citations and confidence scoring.
- Add “I do not know” behavior when confidence is low.

Interview prompts:

- How would you reduce hallucination?
- How would you handle stale docs?
- How would you respect document permissions?
- How would you evaluate answer quality?

### Week 6: Agents and Tool-Calling

Outcomes:

- Know when agentic workflows are useful and when they are dangerous.

Study:

- tool definitions
- planner vs executor patterns
- permission boundaries
- idempotency
- approval steps
- audit logs
- timeouts and retries
- human escalation

Build:

- A support assistant that can classify a ticket, retrieve context, propose an answer, and escalate low-confidence cases.

Design rule:

- The model can recommend. Production systems decide through permissions, policies, and checks.

### Week 7: Evals and Quality Engineering

Outcomes:

- Treat AI quality as an engineering problem.

Study:

- golden datasets
- assertion-based evals
- rubric-based evals
- regression testing
- hallucination tests
- jailbreak and prompt-injection tests
- customer-specific acceptance criteria

Build:

- A small eval runner for support answers.
- Track precision, recall, pass rate, escalation rate, citation coverage, and latency budget.

Interview signal:

- You do not ship an AI system because a demo looked good once.

### Week 8: AI System Design

Outcomes:

- Design production-ready AI features.

Core design template:

1. Clarify user and workflow.
2. Define source of truth.
3. Define model responsibility.
4. Define non-model responsibility.
5. Design data flow.
6. Add permissions and privacy.
7. Add evals.
8. Add observability.
9. Add rollout and rollback.
10. Define success metrics.

Practice cases:

- enterprise support assistant
- internal knowledge assistant
- sales call summarizer
- compliance document reviewer
- AI workflow builder
- customer onboarding copilot

### Week 9: Security, Privacy, and Enterprise Readiness

Outcomes:

- Handle the questions that enterprise customers always ask.

Study:

- PII handling
- data retention
- encryption
- access control
- tenant isolation
- audit logging
- SOC 2 style concerns
- prompt injection
- data exfiltration
- model provider risk

Customer answer pattern:

- State the risk.
- State the control.
- State the remaining trade-off.
- State how it is monitored.

### Week 10: Product Strategy and ROI

Outcomes:

- Connect AI capability to customer value.

Study:

- ROI estimation
- build vs configure
- MVP scoping
- adoption risk
- workflow redesign
- success metrics
- change management

Practice prompts:

- A customer wants an AI assistant for every employee. How do you scope v1?
- A customer asks for full automation. Where do you require human review?
- The model is 85% accurate. Is that good enough?
- The demo is impressive but usage is low. What do you investigate?

### Week 11: Full Mock Loops

Run 2 full mock loops:

- 45 min Python coding
- 45 min AI prototype
- 60 min AI system design
- 45 min customer discovery
- 45 min behavioral
- 30 min executive readout

Score yourself on:

- correctness
- code clarity
- AI architecture
- eval thinking
- security awareness
- customer empathy
- product judgment
- communication

### Week 12: Portfolio and Final Polish

Outcomes:

- Have proof that you can do the job.

Portfolio artifacts:

- Python AI support assistant prototype.
- RAG design document.
- eval plan with golden examples.
- enterprise security FAQ.
- product spec for an AI feature.
- 10 behavioral stories.
- 3 executive-style project summaries.

Final readiness questions:

- Can you explain why AI is the right solution here?
- Can you explain when AI is not the right solution?
- Can you write Python that handles messy customer data?
- Can you design evals before shipping?
- Can you discuss privacy and safety without hand-waving?
- Can you communicate risk without killing momentum?

## Practical Python Projects

### Project 1: AI Support Assistant

Build a Python CLI that:

- reads support tickets
- classifies customer intent
- retrieves relevant help articles
- drafts a response
- assigns confidence
- escalates low-confidence or high-risk tickets
- reports eval metrics

Starter:

```bash
python3 ai_support_assistant_eval.py --demo
```

Extensions:

- add real embeddings
- add vector database storage
- add model API calls
- add citation checking
- add prompt-injection detection
- add test fixtures

### Project 2: Permission-Aware RAG

Build a retrieval system that:

- indexes documents with `customer_id`, `team`, `classification`, and `updated_at`
- filters retrieval by user permissions
- refuses to answer without enough evidence
- includes citations

Interview deep dives:

- How do permissions affect retrieval?
- How do you handle stale documents?
- How do you evaluate citation correctness?
- What gets logged?

### Project 3: AI Workflow Tool Runner

Build a tool-calling prototype that:

- parses a user request
- selects allowed tools
- validates parameters
- requires approval for risky actions
- logs every tool call
- supports retry and rollback for safe operations

Interview deep dives:

- How do you prevent unsafe tool calls?
- How do you make actions idempotent?
- What should be human-approved?
- How do you debug bad agent behavior?

### Project 4: AI Feature Rollout Plan

Write a product and engineering plan for:

- target user
- workflow
- model behavior
- eval criteria
- failure modes
- customer-facing controls
- metrics
- rollout phases
- rollback trigger

## Customer Discovery Questions

Ask:

- What workflow are you trying to improve?
- Who performs it today?
- What does success look like?
- What is the cost of a wrong answer?
- What data sources are trusted?
- Who can access each data source?
- What must the AI never do?
- When should a human approve the result?
- What latency is acceptable?
- What audit trail is required?
- How will users adopt this?
- What existing system must this integrate with?

Avoid starting with:

- Which model do you want?
- Do you want an agent?
- Should we use RAG?

Those are implementation choices, not discovery questions.

## AI System Design Checklist

Use this in every design interview:

- user and workflow
- business outcome
- source of truth
- input data and permissions
- retrieval strategy
- model prompt and structured output
- tool calls and side effects
- human review path
- eval dataset
- quality metrics
- safety controls
- latency and cost budget
- observability
- rollout and rollback
- customer success plan

## Evals Checklist

A good eval plan includes:

- representative examples
- customer-specific edge cases
- expected answer or rubric
- unacceptable answer definition
- citation requirements
- safety requirements
- regression suite
- manual review process
- pass/fail threshold
- owner and review cadence

Metrics to discuss:

- answer accuracy
- citation precision
- refusal quality
- escalation rate
- hallucination rate
- latency
- cost per task
- user acceptance rate
- correction rate

## Behavioral Story Bank

Prepare stories for:

- handling ambiguity with a customer
- building a prototype quickly
- saying no to unsafe automation
- recovering trust after a failure
- debugging a production issue
- making a product trade-off
- influencing security/legal/product/engineering
- learning a new domain quickly
- simplifying an overbuilt solution
- measuring impact after launch

Each story should include:

- situation
- customer or user pain
- technical challenge
- action
- result
- metric
- lesson learned

## Executive Communication Template

Use this for customer readouts:

```text
We found that [workflow/user] is blocked by [specific pain].
The fastest safe path is [proposal].
The AI should handle [bounded task], while humans approve [risky task].
Success means [metric].
The main risks are [risk 1] and [risk 2].
We will reduce those risks through [eval/control/rollout].
The next step is [concrete action].
```

## What “Perfect” Looks Like

You are ready when you can:

- code a Python AI prototype in under 60 minutes
- explain RAG, agents, evals, and safety clearly
- design a customer-specific AI system with permissions and observability
- ask discovery questions that reveal the real workflow
- connect technical choices to customer value
- push back on risky AI use cases
- show a portfolio of practical work
- communicate like an engineer, product thinker, and trusted customer advisor
