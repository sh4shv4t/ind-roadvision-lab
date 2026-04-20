# Data Directory Guide

This project expects datasets in YOLO detection format and keeps all dataset payloads out of git history.

## Expected Layout

Inside `raw/` (original dataset exports):

- `raw/images/` for original image files
- `raw/labels/` for corresponding YOLO text annotations

Inside `processed/` (cleaned/transformed assets used by experiments):

- `processed/images/` for resized/normalized/filtered images
- `processed/labels/` for transformed labels aligned to processed images

Inside `splits/`:

- train/validation/test split manifests or index files

## YOLO Annotation Format

Each annotation line in a label file must follow:

`class_id cx cy w h`

Where:

- `class_id` is an integer class index
- `cx`, `cy` are normalized box center coordinates in `[0, 1]`
- `w`, `h` are normalized box width/height in `[0, 1]`

A single image can have multiple lines (one object per line).

## Git Policy

All dataset payloads under `data/raw/`, `data/processed/`, and `data/splits/` are gitignored by design.
