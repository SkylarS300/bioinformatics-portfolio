# 🧬 Volcano Plot + Enrichment Explorer

This tool allows users to visualize differential gene expression results via an interactive volcano plot and run GO/pathway enrichment analysis using g:Profiler.

## 🔧 Features

- Upload CSV of differential expression results
- Interactive volcano plot with threshold sliders
- Automatic highlighting of significant genes
- One-click GO and pathway enrichment (via g:Profiler)
- Results table and bar chart of enriched terms

## 📁 Input Format

Upload a CSV file with the following columns:

| gene | log2FoldChange | pvalue | padj |
|------|----------------|--------|------|
| TP53 | 2.1            | 0.00004 | 0.0003 |

Use the included [example dataset](example_data/example_de_results.csv) to test it.

## 🚀 Running the App

1. Clone or download this repository
2. Open a terminal in this folder and run:

```bash
python -m venv venv
venv\Scripts\activate      # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
streamlit run app.py

