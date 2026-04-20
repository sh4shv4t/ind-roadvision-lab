"""Dataset stubs for loading Indian road obstacle data in YOLO format."""

from typing import Any


class RoadObstacleDataset:
    """Placeholder dataset class for obstacle detection experiments."""

    def __init__(self, root_dir: str, split: str) -> None:
        """Initialize dataset metadata for a given data split."""
        pass

    def __len__(self) -> int:
        """Return the number of samples in the dataset split."""
        pass

    def __getitem__(self, index: int) -> Any:
        """Return an item containing image and target annotation data."""
        pass


def load_yolo_annotation_file(annotation_path: str) -> list[tuple[int, float, float, float, float]]:
    """Load YOLO rows from one annotation file as typed tuples."""
    pass


def validate_yolo_record(record: tuple[int, float, float, float, float]) -> bool:
    """Validate basic shape and range expectations for a YOLO row."""
    pass
