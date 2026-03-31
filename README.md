# ClearCompliance

**AI-powered compliance automation demo with deterministic evaluation and auditable outputs.**

---

## Overview

ClearCompliance demonstrates how compliance workflows can be structured into **repeatable, explainable systems**.

This demo shows:
- document ingestion  
- deterministic rule evaluation  
- structured report generation  

while keeping production-grade logic private.

---

## Features

- Processes 1000+ transaction records with rule-based classification and deterministic validation logic
- Applies configurable compliance rules with traceable decision paths for each evaluation
- Generates structured JSON reports with pass/fail outcomes and supporting reasoning
- Provides LLM-style explanatory output with mapped rule references and confidence indicators (mocked in demo) 

---

## Demo

Run:

```bash
pip install -r requirements.txt
python demo/run_demo.py
