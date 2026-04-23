# ind-roadvision-labs

This repository is a template for a Deep Learning for Computer Vision (DLCV) research project focused on Indian road obstacle detection. The project studies detection behavior across five road-obstacle classes using YOLO-style bounding-box annotations and approximately 200 images per class, then compares model behavior across three targeted experiments on receptive fields, Siamese embedding sensitivity under corruptions, and transfer-learning freezing strategies.

## Dataset Classes

| Class | Approx. Images | Annotation Format |
|---|---:|---|
| potholes | ~200 | YOLO (`class_id cx cy w h`, normalized) |
| thelas (handcarts) | ~200 | YOLO (`class_id cx cy w h`, normalized) |
| animals | ~200 | YOLO (`class_id cx cy w h`, normalized) |
| barricades | ~200 | YOLO (`class_id cx cy w h`, normalized) |
| rickshaws | ~200 | YOLO (`class_id cx cy w h`, normalized) |

## Experiment Tracks

- [Unit I - Receptive Field Archaeology](experiments/unit1_receptive_field/README.md)
- [Unit II - Problem 7: Siamese Sensitivity](experiments/unit2_siamese_sensitivity/README.md)
- [Unit III - Freezing Strategy](experiments/unit3_freezing_strategy/README.md)

## Setup Instructions

TODO: Add environment setup, dependency installation, and experiment execution commands.

## Course and Citation Info

- Course: Deep Learning for Computer Vision (DLCV)
- Term/Batch Reference: March 2026
- Citation: TODO: Add citation format for this repository and related report.
