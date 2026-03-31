"""Report generator for the ClearCompliance demo.

Writes compliance evaluation results to a JSON file.
"""

from __future__ import annotations

import json
from typing import Dict, Any


def write_report(result: Dict[str, Any], path: str) -> None:
    """Write the evaluation result to a JSON file.

    Parameters
    ----------
    result: Dict[str, Any]
        Evaluation result dictionary.
    path: str
        Destination path for the report.
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)


__all__ = ["write_report"]