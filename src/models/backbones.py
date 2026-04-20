"""Backbone selection stubs for CNN and graph-based experiments."""

from typing import Any


def get_resnet_backbone(model_name: str, pretrained: bool = True) -> Any:
    """Return a placeholder ResNet backbone handle by model name."""
    pass


def get_gcn_backbone(hidden_dim: int, num_layers: int) -> Any:
    """Return a placeholder graph convolutional backbone handle."""
    pass


def apply_freezing_strategy(model: Any, strategy_name: str) -> Any:
    """Apply a named freezing policy and return the updated model."""
    pass
