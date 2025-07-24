import streamlit as st
import pandas as pd
import plotly.express as px
from gprofiler import GProfiler

st.set_page_config(page_title="Volcano + Enrichment Tool", layout="wide")

st.title("🧬 Smart Volcano Plot + Enrichment Explorer")

# Upload section
st.sidebar.header("Upload Differential Expression CSV")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# Threshold controls
logfc_thresh = st.sidebar.slider("Log2 Fold Change Threshold", 0.0, 3.0, 1.0, 0.1)
fdr_thresh = st.sidebar.slider("Adjusted p-value (FDR) Threshold", 0.001, 0.2, 0.05, 0.005)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df = df.dropna(subset=["log2FoldChange", "padj"])
    df["significant"] = (abs(df["log2FoldChange"]) > logfc_thresh) & (df["padj"] < fdr_thresh)

    # Volcano Plot
    fig = px.scatter(
        df,
        x="log2FoldChange",
        y=-df["padj"].apply(lambda p: -1 * pd.np.log10(p + 1e-300)),
        color="significant",
        hover_name="gene",
        labels={"y": "-log10(FDR)", "x": "log2 Fold Change"},
        title="Volcano Plot",
        color_discrete_map={True: "red", False: "gray"},
    )
    st.plotly_chart(fig, use_container_width=True)

    # Selected genes
    sig_genes = df[df["significant"]]["gene"].tolist()
    st.markdown(f"### 🧬 {len(sig_genes)} significant genes")
    st.text(", ".join(sig_genes[:30]) + ("..." if len(sig_genes) > 30 else ""))

    if len(sig_genes) > 0:
        # Run Enrichment
        if st.button("🔍 Run Enrichment Analysis on Significant Genes"):
            gp = GProfiler(return_dataframe=True)
            enrich_results = gp.profile(organism="hsapiens", query=sig_genes)

            if not enrich_results.empty:
                st.markdown("### 📈 Top Enriched Terms")
                top_enriched = enrich_results[["name", "term_size", "p_value", "source", "description"]].head(10)
                st.dataframe(top_enriched)

                fig2 = px.bar(
                    enrich_results.head(10),
                    x="name",
                    y="-log10(p_value)",
                    title="Top Enrichment Results",
                    labels={"name": "Term", "-log10(p_value)": "-log10(p)"},
                )
                st.plotly_chart(fig2, use_container_width=True)
            else:
                st.warning("No enrichment terms found.")
else:
    st.info("Please upload a differential expression CSV to begin.")
