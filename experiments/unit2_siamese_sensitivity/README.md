# Unit II — Problem 7: Siamese Network Sensitivity Analysis

## Research question

What image perturbations break similarity structure in a frozen, pretrained embedding backbone when comparing road-obstacle patches from Indian road scenes?

## Approach

Zero-shot probing with a frozen ResNet-50 backbone (no fine-tuning): patch pairs from YOLO boxes are embedded in \(\mathbb{R}^d\), then cosine similarity and Euclidean distance are measured under rotation, blur, and occlusion at increasing severity.

## Deliverable

The runnable Colab-oriented notebook:

- `notebooks/problem7_siamese_sensitivity.ipynb`

Point the notebook’s dataset root at your folder of full-scene images and YOLO-format labels (`class_id cx cy w h` normalized). Classes: `0=potholes`, `1=thelas`, `2=animals`, `3=barricades`, `4=rickshaws`.

## Results

(To be filled after runs.)
