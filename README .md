# Welcome to *SciGlass+*

*SciGlass+* is an enhanced SciGlass database constructing by large language model (LLM) and manual cross-validation. Due to the large size of the database files, you can download the **original database file on Figshare**. All script files (.py, .ipynb) can be found in this GitHub repository, while all data files (.json, .csv, .xlsx), due to size limitations, can be downloaded from Figshare.This README is organized into three main sections:

1. **Database Construction Tutorial** – Step-by-step guide on how the glass database was automatically built using LLM models.  
2. **Application Demo** – Example notebooks to demonstrate how to load the database, filter glasses based on specific compositions and properties, and use machine learning models to predict glass properties.  
3. **API Reference** – Python functions to access and manipulate the SciGlass+ database.

---

## 1. Database Construction Tutorial

We used LLM models to construct the glass database. The tutorial consists of six steps:

### Step 1: Literature Search and Metadata Collection
1. Log in to [Web of Science](https://www.webofscience.com/wos/).  
2. Select **Advanced Search**.  
3. Enter keywords in the **Query Preview** field (based on SciGlass, including glass systems, compositions, and properties of interest). Example query:  
4. Set the **data range** (custom: 2019-01-01 to 2025-01-01) and click **Search**.  
5. Refine results: select **Article** under "Document Types" and **English** under "Languages".  
6. Export metadata (Excel format) including title, authors, journal, year, DOI, and abstract. Merge multiple exports into `savedrecs-total.xls`.

### Step 2: Literature Filtering
1. Copy the **DOI** and **Abstract** columns to a new sheet for the file `savedrecs-total.xls`. Label articles of interest as `1` and irrelevant ones as `0`. This helps filter unrelated articles using NLP models (e.g., BERT).  
2. Prepare datasets using `./src/mkAbsClsDataset-manual.ipynb` to generate training data (`sample.json`) and inference data (`abstr.json`).  
3. Train and predict on the server with GPU acceleration:  
   - Train model: `python ./src/abstract_classification.py`  
   - Predict classifications: `python ./src/pred.py` → `pred.json`.

### Step 3: Article Download and Paragraph/Table Parsing
1. Use `./src/SelectDoi-manual.ipynb` to get DOIs of articles to download.  
2. Download articles (It requires you to have subscribed to the relevant publishers or journals):  
   - Elsevier XML: `python ./src/elsevier_xml_download.py`  
   - Springer/MDPI HTML: `python ./src/html_download.py`  
   - Wiley HTML: `python ./src/html_download_selenium.py` (requires Chrome)  
3. Extract paragraph and table data:  
   - Elsevier XML: `python ./src/xml_parse_struct_table.py` → `data_strcut_els_20241010.json`  
   - Wiley/MDPI HTML: `python ./src/html_paser_struct_table_mdpi_wiley.py` → `wiley_data_strcut_20241010.json` / `mdpi_data_strcut_20241010.json`  
   - Springer HTML: `python ./src/html_download_table_springer.py` + `python ./src/html_parse_struct_table_springer.py` → `springer_data_strcut_20241010.json`.

### Step 4: Paragraph/Table Filtering
1. Paragraphs filtered by section titles; tables filtered using BERT-trained classifiers.  
2. Use `./src/mkTableClsDatSet.ipynb` to label sample tables and generate training/validation datasets  → `sample_tables.json`, `val_tables.json`.  
3. Train table classifier on server: `python ./src/tables_cls.py`, then validate with `python ./src/table_val_pred.py` → `pred_val_tables.json`.  
4. Apply classifiers to filter paragraphs/tables: `./src/ParseParaTable-html-xml-sel-tables.ipynb` → `data_xml.json`, `data_html.json`.

### Step 5: Data Extraction and Database Construction
1. Extract data from filtered paragraphs/tables using `python ./src/gpt_extract_method_glass.py` → `result_20241010.json`, `result_html_20241013.json`.  
2. Convert JSON to Excel and merge batches: `./src/jsonR2Excel&metaD-manual.ipynb` → `glass-rawdata-2019-2025.xlsx`.  
3. Manual cross-validation is used to improve data quality.

### Step 6: Database Verification and Error Correction
1. Download PDFs of articles to verify extracted data:  
   - `./src/checkPDFlist.ipynb` → DOI lists `els_pdf.txt`, `other_pdf.txt`. 
   - `python ./src/elsevier_pdf_download_custom.py` / `python ./src/pdf_download.py` → download PDF files into `pdf_list` folder (need your API key and subscribe to the relevant publishers or journals)
2. Cross-check each row in `glass-rawdata-2019-2025.xlsx` with the corresponding PDF.  
3. After 12 volunteers working 4 hours/day for 10 months (total cost ~40,000 RMB), the verified database `SciGlass_Plus_properties.xlsx` was produced.

---

## 2. Jupyter Notebook Examples

Example notebooks include:  
- Loading the database  
- Filtering glasses by compositions and properties  
- Using machine learning models to predict glass properties

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

