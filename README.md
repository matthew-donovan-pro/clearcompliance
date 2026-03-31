# ClearCompliance — AI‑Powered Compliance Analysis System

**Demonstration version only** – this package illustrates the structure and workflow of a compliance automation platform.  It omits production‑grade logic and proprietary rule sets.

## Overview

ClearCompliance ingests business documents, extracts key information and evaluates them against a simplified rules engine.  The demonstration prints a sample compliance report for illustrative purposes.

## Features

- **Document analysis** – trivial parser reads text files and extracts dummy fields.
- **Rule engine** – hard‑coded rules evaluate extracted fields and assign a pass/fail flag.
- **Report generation** – outputs a JSON report with evaluation results.

## Quick start

1.  Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2.  Run the demo:

   ```bash
   python demo/run_demo.py
   ```

   A compliance report will be written to `examples/demo_outputs/compliance_report.json`.

## Notes on IP

This repository contains a demonstration version.  The production system integrates sophisticated rule engines, regulatory databases and audit trails which are not included here.