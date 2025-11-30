# 📦 SAP RPT-1 Supply Chain Benchmark  
**Stockout Prediction on 600 Materials Across 3 Plants — Using SAP’s Tabular Foundation Model (RPT-1)**

This repository contains the notebook and resources used to reproduce my benchmark of **SAP RPT-1** on a realistic supply chain scenario: predicting which materials will run out in the next 14 days.

RPT-1 is a Relational Pre-trained Transformer that understands SAP tables out-of-the-box (BOMs, MRP logic, lead times, P2P flows, GL determination, etc.).  
This benchmark demonstrates how RPT-1 performs on **realistic SAP MM/PP data** without fine-tuning.

---

## 🚀 Run the Notebook in Google Colab

The notebook **must be executed in Google Colab** because it requires:

- a **T4 GPU runtime**
- preinstalled CUDA drivers
- a clean reproducible environment

👉 **Open in Google Colab:**  
PUT-YOUR-COLAB-LINK-HERE

notebooks/rpt1_supplychain_stockout_prediction.ipynb

🔑 **Setting your Hugging Face token securely**

The notebook requires a Hugging Face token (READ role only).
To set it in Google Colab, run:

```
import os
os.environ["HF_TOKEN"] = "your_token_here"

```

---

## 📘 Contents


The notebook includes:

- Loading the 600-material dataset  
- 80 few-shot labeled examples (13%)  
- RPT-1 inference  
- Accuracy, precision, recall  
- Risk ranking  
- Timing (1.2 seconds)  
- Discussion of hyperparameters and errors  

---

## 📊 Benchmark Overview

**Dataset**
- 600 materials  
- 3 plants  
- 25 features  
- 80 labeled examples  

**Results (RPT-1 OSS Small)**  
- ⏱ **1.2 seconds** inference  
- 🎯 **75.8% accuracy**  
- 🔥 **95.3% precision (HIGH risk)**  
- 🎣 **84.3% recall (critical cases)**  
- ⚡ **425 materials/second throughput**

---

## 🧠 Why RPT-1 Works Well

RPT-1 is trained on **3.1M real relational tables** with embedded SAP logic:

- Lead time patterns  
- Consumption volatility  
- Supplier reliability  
- Coverage thresholds  
- MRP & BOM cascades  

It performs **in-context learning** on your data — no fine-tuning required.

---

## 🛠 Local Execution (Optional)

Requires:

- GPU with ≥8GB VRAM  
- CUDA 12  
- Python 3.10  
- PyTorch (CUDA)  
- Hugging Face `transformers`

⚠️ **Colab remains the recommended environment**.

---

## 📂 Repository Structure
```
rpt1-sap-playground/
│
├── notebooks/
│ └── MRP_StockOut_Prediction.ipynb
│
├── data/
│ └── sample_materials.csv # Optional
│
├── src/
│ └── utils.py # Optional
│
├── LICENSE
└── README.md

``` 
---

## 📜 License

Recommended: **Apache 2.0**.

---

## 🤝 Contributions

PRs welcome — especially on:

- alternative datasets  
- SAP-focused benchmarks  
- hyperparameter tuning  
- causal extensions  

---

## ⭐ Star the Repo

If this was helpful, please consider **starring** the repo.

