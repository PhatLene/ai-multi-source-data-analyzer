# AI-Powered Multi-Source Data Analyzer

## Overview
This project integrates public profile data from multiple sources and adds an LLM layer to generate structured insights.

The current AI-ready version uses:
- Wikipedia / Wikidata
- YouTube Data API
- Instagram data collected via Apify
- Google Knowledge Graph

It then transforms the unified dataset into business-style outputs such as:
- profile summaries
- key strengths
- potential risks
- data observations

## Project Structure
```text
multi-source-ai-analyzer/
│── data/
│   ├── DatasetOfUnifiedProfiles.csv
│   ├── llm_profile_insights.csv
│
│── notebooks/
│   ├── data_collection.ipynb
│   ├── data_processing.ipynb
│   ├── llm_analysis.ipynb
│
│── src/
│   ├── data_pipeline.py
│   ├── llm_module.py
│
│── main.py
│── requirements.txt
│── .env.example
│── README.md
```

## What Each File Does
- `src/data_pipeline.py`: loads the dataset, handles missing values, and builds clean LLM payloads
- `src/llm_module.py`: sends profile payloads to the OpenAI API and returns structured JSON
- `main.py`: runs the workflow end to end and saves the AI-generated output to CSV

## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your API key:
```bash
export OPENAI_API_KEY="your_key_here"
```

On Windows PowerShell:
```powershell
$env:OPENAI_API_KEY="your_key_here"
```

3. Run the app:
```bash
python main.py
```

## Why This Structure
This split makes the project easier to maintain and easier to explain in interviews:
- data prep is separate from AI logic
- the LLM module can be replaced or upgraded later
- `main.py` stays clean and focused on workflow orchestration
