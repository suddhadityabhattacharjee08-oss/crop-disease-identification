# Crop Disease Identification System

A command-line crop disease identification project built with Python, object-oriented programming, pandas, NumPy, and rule-based reasoning.

## Features

- Symptom-based disease diagnosis
- Ranked diagnosis results using symptom matching
- Rule-based leaf image analysis using RGB pixel masks
- Disease information with treatment and prevention guidance
- OOP with inheritance and polymorphism
- Disease Factory pattern
- CSV dataset management with pandas
- Diagnosis history stored in CSV
- Fully executable from a terminal

> This version intentionally does not use machine learning.

## Requirements

- Python 3.9 or newer
- pip

## Setup

1. Clone the repository.
2. Open a terminal in the project directory.
3. Create and activate a virtual environment (recommended).
4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

From the repository root:

```bash
python main.py
```

The program opens a numbered CLI menu.

## Project Structure

```text
crop-disease-identification/
├── main.py
├── requirements.txt
├── data/
├── models/
├── services/
├── utils/
├── reports/
└── sample_images/
```

## Diagnosis Logic

The symptom engine compares user-entered symptoms with the symptoms stored for each disease affecting the selected crop. Matching diseases are ranked by the proportion of their known symptoms that were observed.

The image analyzer is a simple computer-vision exercise, not an ML classifier. It uses NumPy RGB masks to estimate the percentage of brown, yellow, and dark pixels and converts those observations into symptoms.

## Important Note

The system is an educational software project. Its diagnosis and treatment information should not be treated as professional agricultural advice.
