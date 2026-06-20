# AI-Powered Insurance Claim Verification System

## Overview

This project is a multimodal insurance claim verification system that analyzes customer claim conversations and uploaded images to determine whether a damage claim is supported by visual evidence.

The system uses Google's Gemini Vision model to inspect images, understand claim descriptions, identify visible damage, estimate severity, and generate structured insurance review reports.

---

## Features

* Analyze car, laptop, and package damage claims
* Process single and multiple image submissions
* Extract damage claims from customer conversations
* Verify claims using image evidence
* Identify damaged object parts
* Estimate damage severity
* Generate structured insurance review reports
* Retry handling for API failures and timeouts
* Batch processing for multiple claims
* Automated CSV report generation

---

## System Architecture

```text
Claims CSV + Images
        │
        ▼
 Image Preprocessing
        │
        ▼
 Gemini Vision Analysis
        │
        ▼
 JSON Damage Assessment
        │
        ▼
 Structured Report Generator
        │
        ▼
      output.csv
```

---

## Project Workflow

```text
Claims CSV + Images
        │
        ▼
   code/main.py
        │
        ├── Read claim text
        ├── Load images
        ├── Send to Gemini Vision
        └── Generate JSON assessment
        │
        ▼
output_debug.csv
        │
        ▼
 build_output.py
        │
        └── Create final structured report
        │
        ▼
    output.csv
```

---

## Technologies Used

* Python
* Google Gemini API
* Pandas
* Pillow (PIL)
* Python-dotenv
* Git
* GitHub

---

## Dataset

The dataset contains:

* Insurance claims
* User claim conversations
* Uploaded images
* User history information
* Evidence requirement rules

Supported object categories:

* Car
* Laptop
* Package

---

## Output Fields

The final report contains:

| Column                       |
| ---------------------------- |
| user_id                      |
| image_paths                  |
| user_claim                   |
| claim_object                 |
| evidence_standard_met        |
| evidence_standard_met_reason |
| risk_flags                   |
| issue_type                   |
| object_part                  |
| claim_status                 |
| claim_status_justification   |
| supporting_image_ids         |
| valid_image                  |
| severity                     |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/darshansaini9/insurance-claim-verification-system.git

cd insurance-claim-verification-system
```

### Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Gemini API

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your API key from Google AI Studio.

---

## How to Use the Project

### Step 1: Prepare Dataset

Ensure the following files exist:

```text
dataset/
├── claims.csv
├── sample_claims.csv
├── user_history.csv
├── evidence_requirements.csv
└── images/
```

### Step 2: Run Claim Analysis

```bash
python code/main.py
```

The system will:

* Read customer claim conversations
* Load uploaded images
* Analyze visual evidence using Gemini Vision
* Generate structured JSON damage assessments
* Save intermediate results to:

```text
dataset/output_debug.csv
```

### Step 3: Generate Final Report

```bash
python build_output.py
```

This converts the raw AI responses into a structured insurance review report.

Generated file:

```text
output.csv
```

### Step 4: Review Results

```bash
head output.csv
```

or

```bash
python -c "
import pandas as pd
print(pd.read_csv('output.csv').head())
"
```

---

## Example Output

Gemini Response:

```json
{
  "issue_type": "dent",
  "object_part": "door",
  "claim_status": "supported",
  "severity": "medium"
}
```

Generated Report:

```text
user_005
issue_type = dent
object_part = door
claim_status = supported
severity = medium
```

---

## Project Statistics

* Claims Processed: 44
* Supported Object Types: Car, Laptop, Package
* AI Model: Gemini 2.5 Flash
* Programming Language: Python
* Output Fields: 14
* Images Processed: 80+ (Approx.)

---

## Evaluation

Evaluation details are available in:

```text
evaluation/evaluation_report.md
```

The evaluation includes:

* Model call estimation
* Token usage estimation
* Runtime considerations
* Cost estimation
* Rate-limit handling strategy

---

## Hackathon Context

This project was developed as part of the HackerRank Orchestrate Challenge.

The challenge required participants to build a multimodal insurance claim verification system capable of analyzing customer conversations and image evidence to determine claim validity and generate structured outputs.

During development, AI-assisted tools (including ChatGPT) were used for brainstorming, debugging, documentation, prompt refinement, and code review. The overall project design, implementation, testing, integration, and deployment workflow were completed by the author.

The project demonstrates practical applications of:

* Generative AI
* Computer Vision
* Prompt Engineering
* Data Processing
* Automated Decision Support Systems
* Python Development
* Git & GitHub Workflow

This repository is shared for educational and portfolio purposes.

---

## Future Improvements

* Confidence scoring
* Advanced fraud-risk analysis
* Damage localization
* Object detection integration
* Human review workflow
* Database support
* REST API integration
* Web dashboard
* Real-time claim processing

---

## Author

**Darshan Saini**

B.Tech CSE (Cyber Security)
Poornima College of Engineering, Jaipur

GitHub: https://github.com/darshansaini9
