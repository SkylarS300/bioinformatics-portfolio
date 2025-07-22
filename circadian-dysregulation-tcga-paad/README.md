# 🧬 Circadian Gene Dysregulation in Pancreatic Cancer

This project analyzes the expression of circadian genes in pancreatic adenocarcinoma (TCGA-PAAD) using RNA-seq data.

### 🔬 Key Methods
- Subset TCGA expression matrix to 32 experimentally validated circadian genes
- Match tumor vs. normal samples using phenotype metadata
- Welch’s t-test for differential expression
- FDR correction and volcano plot

### 📈 Results
- 2 significantly dysregulated genes:
  - **RAB24**: downregulated in tumors
  - **WDR75**: upregulated in tumors

---

### 📂 Files
- `CircadianGeneDisruption_InCancer.ipynb`: main notebook
- `expression_circadian_subset.tsv`: subset expression matrix
- `circadian_genes_with_ensg.csv`: gene ID mapping
- `phenotype_data.tsv`: sample metadata
