# Customer-Facing AI Engineer Interview Prompts

Use these prompts for weekly mocks. For each one, practice clarifying the customer workflow, proposing a scoped AI approach, identifying risks, and communicating trade-offs.

## Practical Coding

1. Build a Python script that classifies support tickets and escalates risky ones.
2. Build a simple retrieval function that returns relevant help articles with citations.
3. Write an eval runner that compares predicted labels against expected labels.
4. Implement confidence-based refusal when retrieved evidence is weak.
5. Detect prompt-injection text in customer-provided content.
6. Transform a nested CRM payload into a normalized account/contact schema.
7. Implement pagination over a mock API client used for document ingestion.
8. Given dependency edges, return a safe tool execution order for an AI workflow.
9. Write a retry wrapper that retries transient model/API failures and stops on validation errors.
10. Build an audit log record for every AI action and tool call.

## AI System Design

1. Design an enterprise support assistant that drafts answers with citations.
2. Design a permission-aware RAG system for internal company knowledge.
3. Design an AI sales engineer assistant that prepares customer demos.
4. Design a compliance document reviewer with human approval.
5. Design a webhook ingestion and document indexing pipeline for RAG.
6. Design an agent that can create tickets, update CRM fields, and send summaries safely.
7. Design eval infrastructure for an AI product used by enterprise customers.
8. Design a tenant-isolated AI platform with audit logs and data retention controls.
9. Design model observability for quality, latency, cost, and safety.
10. Design rollback for a newly launched AI feature whose answer quality regressed.

## Product Cases

1. A customer wants full AI automation for a high-risk workflow. What do you do?
2. A model is 85% accurate. Is it good enough to launch?
3. A demo performs well, but production users do not adopt it. How do you investigate?
4. A customer asks to fine-tune a model using sensitive data. What questions do you ask?
5. Sales wants an AI feature urgently for a deal. Security says it is risky. How do you decide?
6. Customers complain that the AI gives generic answers. What do you change?
7. You can improve answer quality, latency, or cost this quarter. Which do you choose?
8. A customer insists on using agents. You think RAG plus workflow automation is safer. How do you explain it?

## Customer Discovery

1. A support leader says, "We need AI to reduce ticket volume." What do you ask?
2. A legal team wants an AI contract reviewer. How do you scope safe behavior?
3. A customer success team wants automated account summaries. What data is needed?
4. A security team asks whether prompts are logged. How do you respond?
5. A VP asks for ROI before approving a pilot. What metrics do you propose?

## Behavioral

1. Tell me about a time you handled ambiguity with a customer.
2. Tell me about a time you influenced without authority.
3. Tell me about a time you recovered customer trust.
4. Tell me about a time you pushed back on unsafe automation.
5. Tell me about a time you debugged a difficult production issue.
6. Tell me about a time you learned a domain quickly.
7. Tell me about a time you made a product and engineering trade-off.
8. Tell me about a time you simplified an overcomplicated technical plan.
9. Tell me about a time you measured whether a launch actually worked.
10. Tell me about a time you explained a technical risk to non-technical stakeholders.

## Executive Readout

1. Explain RAG to a VP in 2 minutes.
2. Explain why an agent should require human approval before taking action.
3. Explain why the team should invest in evals before expanding a pilot.
4. Explain why a lower-cost model may be better for a workflow.
5. Explain why a customer-specific customization should become a platform feature.
