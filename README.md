# SciGlassPlus

SciGlassPlus is a Python library providing access to a comprehensive glass database. Due to the large size of the database files, you can download the original database file on **Figshare**. This README is organized into three main sections:

1. **Database Construction Tutorial** – Step-by-step guide on how the glass database was automatically built using GPT models.  
2. **Jupyter Notebooks** – Example notebooks to demonstrate how to load the database, filter glasses based on specific compositions and properties, and use machine learning models to predict glass properties.  
3. **API Reference** – Python functions to access and manipulate the SciGlassPlus database.

---

## 1. Database Construction Tutorial (2019–2025 Glass Data)

We used GPT models to construct the glass database. The overall framework is illustrated in **Figure 1**. This tutorial uses glass data from **2019/01/01 to 2025/01/01** (GitHub currently hosts SciGlass data updated until 2019) and explains the automatic extraction and database construction process. The tutorial consists of six steps:

### Step 1: Literature Search and Metadata Collection
1. Log in to [Web of Science](https://www.webofscience.com/wos/).  
2. Select **Advanced Search**.  
3. Enter keywords in the **Query Preview** field (based on SciGlass, including glass systems, compositions, and properties of interest). Example query:  

   ```
   (AB=((propert* OR viscosity OR "glass transition temperature" OR "melting temperature" OR ... ) AND (glass*)))
   OR (TI=...)
   OR (AK=...)
   ```
4. Set the **data range** (custom: 2019-01-01 to 2025-01-01) and click **Search**.  
5. Refine results: select **Article** under "Document Types" and **English** under "Languages".  
6. Export metadata (Excel format) including title, authors, journal, year, DOI, and abstract. Merge multiple exports into `savedrecs-total.xls`.

### Step 2: Literature Filtering
1. Copy the **DOI** and **Abstract** columns to a new sheet. Label articles of interest as `1` and irrelevant ones as `0`. This helps filter unrelated articles using NLP models (e.g., BERT).  
2. Prepare datasets using `mkAbsClsDataset-manual.ipynb` to generate training data (`sample.json`) and inference data (`abstr.json`).  
3. Train and predict on the server with GPU acceleration:  
   - Log in: `ssh zhaoyj@166.111.91.199`  
   - Activate environment: `source activate /data/home/zian/anaconda3/envs/nlp`  
   - Train model: `cd nlp-abstr-cls && python abstract_classification2.py`  
   - Predict classifications: `python pred.py` → `pred.json`.

### Step 3: Article Download and Paragraph/Table Extraction
1. Use `SelectDoi-manual.ipynb` to get DOIs of articles to download.  
2. Download articles:  
   - Elsevier XML: `elsevier_xml_download.py`  
   - Springer/MDPI HTML: `html_download.py`  
   - Wiley HTML: `html_download_selenium.py` (requires Chrome)  
3. Extract paragraph and table data:  
   - Elsevier XML: `xml_parse_struct_table.py` → `data_strcut_els_20241010.json`  
   - Wiley/MDPI HTML: `html_paser_struct_table_mdpi_wiley.py` → `wiley_data_strcut_20241010.json` / `mdpi_data_strcut_20241010.json`  
   - Springer HTML: `html_download_table_springer.py` + `html_parse_struct_table_springer.py` → `springer_data_strcut_20241010.json`.

### Step 4: Paragraph/Table Filtering
1. Paragraphs filtered by section titles; tables filtered using BERT-trained classifiers.  
2. Use `mkTableClsDatSet.ipynb` to label sample tables and generate training/validation datasets (`sample_tables.json`, `val_tables.json`).  
3. Train table classifier on server: `tables_cls.py`, then validate with `table_val_pred.py` → `pred_val_tables.json`.  
4. Apply classifiers to filter paragraphs/tables: `ParseParaTable-html-xml-sel-tables.ipynb` → `data_xml.json`, `data_html.json`.

### Step 5: Data Extraction and Database Construction
1. Extract data from filtered paragraphs/tables using `gpt_extract_method_glass.py` → `result_20241010.json`, `result_html_20241013.json`.  
2. Convert JSON to Excel and merge batches: `jsonR2Excel&metaD-manual.ipynb` → `glass-data-2019-2024.xlsx`.  
3. Manual inspection is recommended to improve data quality.

### Step 6: Database Verification and Error Correction
1. Download PDFs of articles to verify extracted data:  
   - `checkPDFlist.ipynb` → DOI lists  
   - `elsevier_pdf_download_custom.py` / `pdf_download.py` → PDF files in `pdf_list` folder  
2. Cross-check each row in `glass-data-2019-2024.xlsx` with the corresponding PDF.  
3. After 12 volunteers working 4 hours/day for 10 months (total cost ~40,000 RMB), the verified database `SciGlass_Plus_properties.xlsx` was produced.

---

## 2. Jupyter Notebook Examples

Example notebooks include:  
- Loading the database  
- Filtering glasses by compositions and properties  
- Using machine learning models to predict glass properties

*(Details of these notebooks are provided in the repository under `notebooks/`.)*

---

## 3. API Reference

### Installation
```bash
pip install SciGlassPlus
```

### Access Available Elements, Compounds, Properties, and Metadata
```python
from SciGlassPlus.load import SGP, available_columns

columnNames = available_columns()
```
Returns a dictionary with keys: `"Elements"`, `"Compounds"`, `"Properties"`, `"Metadata"`. Each key contains a list of available items.

### Load All Data
```python
df_all = SGP()
```

### Load Filtered Data
```python
elements_cfg = {"drop": ["Ca"], "keep": ["Si"]}
compounds_cfg = {"drop": ["CaO", "TiO2"], "keep": ["SiO2", "Al2O3"]}
properties_cfg = {"drop": ["T1", "T2"], "keep": ["Tg"]}
metadata_cfg = {"drop": ["Institutions"], "keep": ["Doi"]}

df_filtered = SGP(
    elements_cfg=elements_cfg,
    compounds_cfg=compounds_cfg,
    properties_cfg=properties_cfg,
    metadata_cfg=metadata_cfg
)
```
- `"drop"`: columns removed or entries with non-zero values filtered out (for elements and compounds)  
- `"keep"`: only entries with defined values are kept

