## Hackathon Context

This project was developed during participation in the HackerRank Orchestrate Competition.

The objective was to build a multimodal insurance claim verification system capable of analyzing customer conversations and image evidence to determine claim validity and generate structured review outputs.

During development, AI-assisted tools (including ChatGPT) were used for brainstorming, debugging, documentation, prompt refinement, and code review. The overall project design, implementation, testing, integration, and deployment workflow were completed by the author.

The project demonstrates practical applications of:

* Generative AI
* Computer Vision
* Prompt Engineering
* Data Processing
* Automated Decision Support Systems
* Python Development
* Git and GitHub Workflow

This repository is shared for educational and portfolio purposes.

## How to Use the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/darshansaini9/insurance-claim-verification-system.git

cd insurance-claim-verification-system
```

### Step 2: Create a Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Gemini API

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get a Gemini API key from Google AI Studio.

### Step 5: Prepare Dataset

Place the required files inside the `dataset/` directory:

```text
dataset/
├── claims.csv
├── sample_claims.csv
├── user_history.csv
├── evidence_requirements.csv
└── images/
```

### Step 6: Run Claim Analysis

Execute:

```bash
python code/main.py
```

The system will:

* Read claim conversations
* Load associated images
* Analyze evidence using Gemini Vision
* Generate structured JSON responses
* Save intermediate results to:

```text
dataset/output_debug.csv
```

### Step 7: Generate Final Report

Execute:

```bash
python build_output.py
```

This converts the raw AI responses into a structured insurance review report.

Generated file:

```text
output.csv
```

### Step 8: Review Results

Open the final report:

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

### Example Workflow

```text
Customer Claim + Images
          │
          ▼
      main.py
          │
          ▼
  output_debug.csv
          │
          ▼
   build_output.py
          │
          ▼
      output.csv
```

The final report contains:

* Damage type
* Affected object part
* Claim status
* Severity assessment
* Risk indicators
* Evidence evaluation
* Supporting image references
