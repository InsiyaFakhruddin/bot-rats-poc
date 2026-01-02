# Reasoning-Aware Template Selection (RATS) — Proof of Concept

This repository contains a **lightweight proof-of-concept (PoC)** implementation
for **Reasoning-Aware Template Selection (RATS)**, a proposed extension to the
_Buffer of Thoughts (BoT)_ framework for Large Language Model (LLM) reasoning.

The goal of this PoC is **architectural demonstration**, not full system
implementation or benchmarking.

---

## 📌 Motivation

The original Buffer of Thoughts framework retrieves reusable reasoning templates
primarily using **semantic embedding similarity**.  
While effective, this approach can retrieve templates that are _linguistically_
similar but _reasoning-incompatible_.

RATS addresses this limitation by introducing **reasoning-aware retrieval** that
explicitly evaluates:

- Semantic similarity
- Structural reasoning compatibility
- Constraint coverage

---

## 🧠 Core Idea

Instead of selecting templates using a single similarity metric, **RATS** assigns
each candidate template a **composite score**:

<div align="center">

**Score(T) = α · SemanticSim + β · StructuralFit + γ · ConstraintCoverage**

</div>

This transforms template retrieval from static lookup into a **lightweight,
reasoning-aware evaluation step**, without increasing the number of LLM inference
calls.

---

## 🗂 Repository Structure

```text
bot-rats-poc/
│
├── README.md
├── requirements.txt
│
├── meta_buffer/
│   ├── templates.py            # Thought-template definitions
│   └── template_metadata.py    # Usage & success tracking
│
├── retrieval/
│   ├── embedding_retrieval.py  # Semantic similarity (placeholder)
│   ├── structural_matcher.py   # Reasoning structure alignment
│   └── scoring.py              # Composite scoring function
│
├── distiller/
│   └── mock_problem_distiller.py  # Simulated problem distillation
│
└── main.py  # End-to-end scoring demonstration
```


## 🔬 Scope and Limitations

- This PoC **does not include**:

  - Real LLM calls
  - Training loops
  - Dataset evaluation
  - Vector databases

- All similarity functions are **simplified placeholders**
  intended to demonstrate **control flow and system design**, not performance.

---

## 🎯 Intended Use

This repository is designed for:

- Academic coursework
- Research proposals
- Architectural validation
- Conceptual demonstrations of reasoning-centric retrieval

It is **not intended for production use**.

---

## 📚 Reference

_Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models_  
(Original paper analyzed and extended in the accompanying written report)
