#!/usr/bin/env python3
"""Run a simple ClearCompliance demo.

This script reads a sample document, performs a compliance
evaluation and writes the result to a JSON file in the examples
directory.  It demonstrates the high‑level workflow of the
ClearCompliance package.
"""

from pathlib import Path
import json
import sys
from pathlib import Path

# Add the project root to sys.path so that the src package can be imported
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from src.compliance_engine import evaluate_document  # type: ignore
from src.report_generator import write_report  # type: ignore


def main() -> None:
    sample_doc = project_root / "examples" / "sample_documents" / "invoice_sample.txt"
    output_file = project_root / "examples" / "demo_outputs" / "compliance_report.json"

    result = evaluate_document(str(sample_doc))
    write_report(result, str(output_file))
    print(f"Compliance report written to {output_file}")


if __name__ == "__main__":
    main()