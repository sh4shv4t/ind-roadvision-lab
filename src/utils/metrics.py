"""Metric computation stubs for experiment-level evaluation summaries."""

from typing import Any


def compute_map(predictions: Any, targets: Any) -> float:
    """Compute placeholder mean Average Precision value."""
    pass


def compute_classwise_recall(predictions: Any, targets: Any) -> dict[str, float]:
    """Compute placeholder class-wise recall values."""
    pass


def summarize_experiment_metrics(metrics: dict[str, Any]) -> dict[str, Any]:
    """Return a normalized summary mapping for report generation."""
    pass
