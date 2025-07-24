# Tumor vs. Fetal Mitosis

**Hypothesis:** Primary human tumors reactivate fetal developmental mitotic programs to drive uncontrolled proliferation.

---

## 🚀 Project Overview

This analysis tests whether mitotic gene expression programs in adult tumors mirror those active during human fetal development. We focus on a curated set of 31 canonical mitotic regulators (e.g. AURKA, CDK1, PLK1, MKI67) converted to Ensembl IDs, then compare:

1. **Fetal TPM data** (E-MATB-6814, Expression Atlas) across 597 mitotic genes and 120 samples spanning 4 weeks post-conception to elderly adult.  
2. **TCGA primary tumor TPM data** for the same 597 genes across ~9 185 samples.

Key steps:  
- **Dimensionality reduction (PCA)** to visualize overlap of tumor and fetal samples.  
- **Euclidean‐distance matching** to identify each tumor’s nearest fetal “stage–tissue” centroid (119 unique combinations).  
- **Hierarchical clustering** of the 9 185 × 119 distance matrix to uncover tumor subgroups reflecting discrete developmental windows.  
- **Differential expression (Welch’s t-test)** to identify marker mitotic genes for each tumor cluster.

---

## 📁 Repository Structure

tumor_vs_fetal_mitosis/
├── data/
│ ├── fetal/
│ │ └── fetal_mitotic_tpm.tsv # Filtered fetal TPM (597 genes × 120 samples)
│ ├── mitosis/
│ │ └── mitosis_ensembl_ids.txt # Curated mitotic gene Ensembl IDs
│ └── tcga/
│ └── primary_tumor_only_mitotic_tpm.csv # Filtered TCGA TPM (597 genes × ~9 185 tumors) MUST BE DOWNLOADED FROM RELEASES DUE TO SIZE
├── notebooks/
│ └── 01_expression_analysis.ipynb # Fully annotated analysis pipeline
├── results/
│ ├── closest_fetal_match_per_tumor.csv # Each tumor’s nearest fetal sample & distance
│ ├── fetal_tissue_match_frequencies.csv # Frequency of nearest‐tissue matches
│ └── cluster_markers/
│ └── cluster_<n>_top_markers.csv # Top-10 marker mitotic genes per tumor cluster
├── .gitignore # Exclude raw downloads, caches, checkpoints
└── README.md # This file


---

## 🛠️ Quickstart

1. **Clone this repository**  
    ```bash
    git clone git@github.com:<your-username>/bioinformatics-portfolio.git
    cd bioinformatics-portfolio/tumor_vs_fetal_mitosis
    ```

2. **Create a Python environment**  
   - **Conda**  
     ```bash
     conda create -n tumor-fetal python=3.9 pandas numpy scikit-learn seaborn scipy matplotlib mygene
     conda activate tumor-fetal
     ```
   - **Pip**  
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     pip install pandas numpy scikit-learn seaborn scipy matplotlib mygene
     ```

3. **Launch the notebook**  
    ```bash
    jupyter lab notebooks/01_expression_analysis.ipynb
    ```

4. **Inspect results**  
   - Figures generated inline in the notebook  
   - CSV outputs under `results/`

---

### Download the Large TCGA TPM Matrix

The primary tumor TPM file is too large to store in GitHub.  
You can download it from our latest release:

[Download primary_tumor_only_mitotic_tpm.csv](https://github.com/Skylars300/bioinformatics-portfolio/releases/download/v1.0-data/primary_tumor_only_mitotic_tpm.csv)

---

## ⚙️ Methods Summary

1. **Gene Curation & Mapping**  
   - Milestones: 31 key mitotic regulators chosen from GO:0007067.  
   - Mapping: mygene API used to convert symbols → Ensembl gene IDs, handle multiple transcript mappings, deduplicate.

2. **Data Preparation**  
   - Fetal data: Expression Atlas TPM, skip metadata rows, retain only the 597 mitotic genes, impute missing values to zero.  
   - TCGA data: Raw Xena transcript-level TPMs (~27 GB) were chunk-read, mapped transcripts → genes, filtered to mitotic IDs, concatenated into a 597 × ~9 185 matrix.

3. **Exploratory Analysis**  
   - Boxplots: Compare mean TPM of mitotic genes across fetal tissues to identify high-proliferation contexts.  
   - PCA (fetal only): Z-score standardize → project to PC1/PC2, colored by tissue to visualize developmental trajectories and outliers (e.g. testis).

4. **Tumor vs. Fetal Comparison**  
   - PCA (tumor only): Same pipeline to view tumor heterogeneity.  
   - Joint PCA: Separate scaling for fetal and tumor, then combined projection to demonstrate shared transcriptional space.

5. **Distance‐Based Matching**  
   - Stage–tissue centroids: Average fetal TPM per (stage, tissue) → 119 centroids.  
   - Euclidean distances: Compute distance from each tumor sample to each centroid → nearest-neighbor matching.  
   - Barplot: Frequency of tumors matched to each fetal profile and broad tissue summarization.

6. **Hierarchical Clustering**  
   - Clustermap: Heatmap of the 9 185 × 119 distance matrix, columns clustered, annotated by organ via color bar—reveals discrete developmental windows that tumors recapitulate.

7. **Tumor Subgroup Identification**  
   - Agglomerative Clustering: Partition tumors into 5 clusters based on their fetal‐distance profiles.  
   - Centroid heatmap: Average distance profiles (5 clusters × 119 centroids) to characterize each tumor subgroup’s developmental affinity.

8. **Differential Marker Gene Analysis**  
   - Welch’s t-test: For each cluster vs. all other tumors on the 597 genes.  
   - Top markers: Report top 10 genes (Ensembl ID + gene symbol) per cluster driving the fetal similarity.

---

## 📈 Key Findings

- **Tumors occupy fetal proliferative space:**  
  Tumor PCA points overlap with fetal samples, confirming shared mitotic program usage.

- **Nearest‐tissue barplot:**  
  Most tumors map to highly proliferative fetal organs—liver, heart, kidney—supporting the reactivation hypothesis.

- **Hierarchical clustering:**  
  Tumors cluster around specific developmental windows (e.g. 5–9 wk heart, neonate liver, adolescent testis), not a generic “fetal” signature.

- **Tumor subgroups (n=5):**  
  Each subgroup defined by its closest fetal stage–tissue profiles and unique mitotic marker genes (available under `results/cluster_markers/`).

---

## 📂 Results & Figures

- **Figures:** All plots (PCA, boxplots, barplots, clustermap, heatmaps) are embedded in the notebook.  
- **Tables:**  
  - `closest_fetal_match_per_tumor.csv`  
  - `fetal_tissue_match_frequencies.csv`  
  - `cluster_<n>_top_markers.csv`

---

## 🚫 .gitignore Highlights

```
# Raw, large downloads
data/fetal/ematb6814_fetal_tpm.tsv
data/tcga/xena_tcga_target_gtex_tpm.tsv

# Python environments & caches
.env/
env/
venv/
__pycache__/
*.pyc

# Jupyter checkpoints
**/.ipynb_checkpoints/

# macOS files
.DS_Store
```

---

## 📑 Citation & License

Please cite this work as:

```
Skylar S., 2025. “Tumor vs. Fetal Mitosis: Comparative Transcriptomic Analysis of Mitotic Gene Reactivation in Cancer.” GitHub Repository.
```

Licensed under the MIT License.
