# 🧬 Bioinformatics Portfolio

Hey. Welcome to my computational biology portfolio! Below are various projects involving real RNA-seq data, building reproducible pipelines, analyzing cancer gene expression, and automating public-data retrieval.

---

## 🔁 Circadian Gene Dysregulation in Pancreatic Cancer

📂 [Project folder](./circadian-dysregulation-tcga-paad)  
📒 [Notebook](./circadian-dysregulation-tcga-paad/CircadianGeneDisruption_InCancer.ipynb)

- **Data & Methods:**  
  - TCGA-PAAD RNA-seq TPM (n≈178 samples)  
  - 32 known circadian regulators  
  - Welch’s t-test + FDR correction  
- **Key Findings:**  
  - **RAB24** significantly downregulated  
  - **WDR75** significantly upregulated  
- **Visualization:** Publication-quality volcano plot and boxplots.

---

## 🩺 Breast Cancer Gene Expression Subtypes

📂 [Project folder](./breast-cancer-gene-expression)  
📒 [Notebook](./breast-cancer-gene-expression/Breast_Cancer_Gene_Expression.ipynb)

- **Data & Methods:**  
  - TCGA-BRCA RNA-seq counts & subtype metadata  
  - EdgeR/limma-voom for differential expression  
  - GO/KEGG enrichment via g:Profiler  
- **Highlights:**  
  - Mitotic genes enriched in Basal vs. Luminal  
  - Lipid metabolism pathways altered in HER2+  
  - ECM remodeling signatures in Luminal B  
- **Figures:** Volcano plots, heatmaps, enrichment bar charts.

---

## 🧬 Tumor vs. Fetal Mitosis

📂 [Project folder](./tumor_vs_fetal_mitosis)  
📒 [Notebook](./tumor_vs_fetal_mitosis/notebooks/01_expression_analysis.ipynb)

- **Hypothesis:** Adult tumors hijack fetal mitotic programs.  
- **Data:**  
  - **Fetal:** Expression Atlas E-MATB-6814 TPM (597 mitotic genes × 120 samples)  
  - **Tumor:** TCGA primary tumors TPM (597 genes × ~9 185 samples)  
- **Workflow:**  
  1. **PCA** of fetal and tumor mitotic expression  
  2. **Euclidean‐distance matching**: each tumor → nearest fetal stage–tissue (119 centroids)  
  3. **Hierarchical clustering** of tumors vs. fetal profiles  
  4. **Agglomerative clustering** defines 5 tumor subgroups  
  5. **Differential t-test** identifies top marker mitotic genes per cluster  
- **Key Results:**  
  - Tumors and fetal samples overlap in mitotic PCA space  
  - Most tumors match high-proliferation fetal tissues (liver, heart, kidney)  
  - Tumors subdivide into clusters resembling specific developmental windows (e.g. 5–9 wk heart, neonate liver, adolescent testis)  
  - Top marker genes (e.g. MKI67, PLK1) are available in `results/cluster_markers/`
- **Figures & Tables:**  
  - Joint PCA, barplots of nearest tissues, clustermap heatmap, cluster-centroid heatmap  
  - CSVs of per-tumor matches and cluster marker genes

---

## 🛠️ Public Data Retriever CLI (in development)

A command-line tool to **search**, **download**, and **organize** public datasets from GEO, SRA, ArrayExpress, and Expression Atlas:

```bash
# Search studies
pdr search --term "glioblastoma RNA-seq" --source GEO --limit 5

# Download data for a study
pdr download --accession GSE12345 --outdir data/GSE12345/ --files raw,metadata

# Summarize study samples
pdr summary --accession GSE12345
```

## Next Steps
- Packaging on PyPI  
- Adding alignment/QC pipeline integration  

---

## 🏁 Next Projects (Coming Soon)
- Single‐cell RNA-seq QC dashboard  
- Automated differential expression wrapper  
- Genome build version manager  
- Interactive multi-omics explorer  

---

## 📖 How to Use This Site
1. Navigate via the **Project** links above  
2. Each project contains code, data descriptions, and example outputs  
3. Clone any project with:
   ```bash
   git clone git@github.com:<username>/bioinformatics-portfolio.git
   cd <project-folder>
   ```
4. Follow each project’s README for environment setup and running instructions

Built with 💻 + 🔬. Feedback and contributions welcome!
