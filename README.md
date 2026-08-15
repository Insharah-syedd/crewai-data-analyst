# 📊 CrewAI Data Analyst

An AI-powered **Data Analyst Agent** built with **CrewAI, Python, and Pandas**. The project uses AI agents and custom tools to analyze CSV datasets, identify important patterns and trends, and generate a professional business report.

## 🚀 Overview

The CrewAI Data Analyst is designed to automate the process of exploring and understanding sales data.

Instead of manually inspecting a CSV file, the system uses an AI-powered data analyst workflow to:

* Read and inspect CSV datasets
* Identify rows and columns
* Detect data types
* Check missing values
* Check duplicate records
* Generate descriptive statistics
* Identify important sales patterns and trends
* Compare products and locations
* Generate business insights
* Produce a structured sales performance report

The project demonstrates how **Agentic AI** can be used to automate real-world data analysis tasks.

---

## ✨ Features

* 🤖 AI-powered data analysis
* 📁 CSV dataset processing
* 🐼 Pandas-based data analysis
* 🔍 Automatic dataset inspection
* 📊 Sales performance analysis
* 📈 Trend and pattern identification
* 🏙️ Location-based analysis
* 📦 Product performance comparison
* 💡 Business recommendations
* 📝 Automated report generation
* 🛠️ Custom CrewAI tools
* ⚙️ Configurable AI agents and tasks

---

## 🧠 How It Works

The project follows an agent-based workflow:

```text
                User
                  │
                  ▼
            CSV Dataset
                  │
                  ▼
          ┌───────────────┐
          │    CrewAI     │
          └───────┬───────┘
                  │
                  ▼
        ┌───────────────────┐
        │ Data Analyst Agent│
        └─────────┬─────────┘
                  │
                  ▼
          CSV Analysis Tool
                  │
                  ▼
             Pandas
                  │
                  ▼
       Data Analysis & Insights
                  │
                  ▼
        Sales Performance Report
```

The agent receives the dataset, uses available tools to inspect and analyze it, and then produces meaningful insights that can help understand business performance.

---

## 🛠️ Technologies Used

| Technology | Purpose                           |
| ---------- | --------------------------------- |
| Python     | Core programming language         |
| CrewAI     | AI agent orchestration            |
| Pandas     | Data analysis and processing      |
| YAML       | Agent and task configuration      |
| UV         | Python dependency management      |
| CSV        | Dataset format                    |
| LLM        | AI-powered reasoning and analysis |
| Markdown   | Report generation                 |

---

## 📂 Project Structure

```text
data_analyst/
│
├── knowledge/
│   └── user_preference.txt
│
├── src/
│   └── data_analyst/
│       │
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       │
│       ├── tools/
│       │   ├── csv_info_tool.py
│       │   └── custom_tool.py
│       │
│       ├── __init__.py
│       ├── crew.py
│       └── main.py
│
├── tests/
│
├── sales.csv
├── report2.md
├── AGENTS.md
├── pyproject.toml
├── README.md
├── uv.lock
└── .gitignore
```

---

## 🔧 Custom Tool

The project includes a custom **CSV Info Tool** that uses Pandas to inspect a dataset.

The tool can provide information such as:

* Number of rows
* Number of columns
* Column names
* Data types
* Missing values
* Duplicate rows

This allows the AI agent to access structured information about the dataset before performing deeper analysis.

---

## 📊 Example Dataset

The project includes a sample sales dataset containing information about:

* Products
* Cities
* Sales quantities
* Prices
* Revenue
* Daily transactions

The sample dataset can be replaced with another compatible CSV dataset for analysis.

---

## 📈 Example Analysis

The system can generate insights such as:

* Which product has the highest sales volume
* Which product generates the most revenue
* Which city performs best
* Average product prices
* Revenue comparisons
* Sales trends
* Potential business opportunities

For example, the generated report can identify that **Phone** products have high sales volume while **Laptop** products have a higher average selling price.

---

## 📝 Generated Report

The project generates a Markdown-based sales performance report.

An example output is available in:

```text
report2.md
```

The report contains:

* Executive Summary
* Key Takeaways
* Product Performance
* Location Performance
* Business Impact
* Recommendations

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Insharah-syedd/crewai-data-analyst.git
```

### 2. Navigate to the project

```bash
cd crewai-data-analyst
```

### 3. Install dependencies

If you are using UV:

```bash
uv sync
```

You can also use the project's dependency configuration in `pyproject.toml`.

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

Add your own API configuration there.

Example:

```env
OPENAI_API_KEY=your_api_key_here
```

**Do not commit your `.env` file or API keys to GitHub.**

The `.gitignore` file is configured to keep sensitive environment files out of the repository.

---

## ▶️ Running the Project

After installing the dependencies and configuring your environment variables, run the CrewAI project with:

```bash
crewai run
```

The project will start the configured CrewAI workflow and execute the data analysis tasks.

---

## 🧪 Testing

The project contains a `tests` directory for testing project functionality.

Run tests according to the configured Python testing environment.

---

## 🎯 Use Cases

This project can be useful for:

* Sales analysis
* Business reporting
* CSV data exploration
* Automated reporting
* Product performance analysis
* Regional sales analysis
* Business decision support

The same architecture can also be extended to other datasets such as:

* Customer data
* Marketing data
* Financial data
* Inventory data
* E-commerce data

---

## 🔮 Future Improvements

Possible future improvements include:

* Interactive data visualization
* Automatic charts and graphs
* Excel file support
* Database integration
* Web-based dashboard
* Email report automation
* Multiple specialized AI agents
* Automated PDF report generation
* Real-time data analysis
* Natural-language questions about datasets

---

## 💡 What This Project Demonstrates

This project demonstrates practical use of **Agentic AI** by combining:

```text
AI Agents
   +
Custom Tools
   +
Python
   +
Pandas
   +
Data Analysis
   +
Automated Reporting
```

Instead of simply generating text, the AI agent interacts with tools and processes real data to produce useful business insights.

---

## 👩‍💻 Author

**Insharah Syed**

GitHub: [Insharah-syedd](https://github.com/Insharah-syedd)
