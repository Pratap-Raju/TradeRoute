# TradeRoute: Global Logistics & Cost Optimization Engine

**TradeRoute** is a sophisticated data analysis system designed to simulate and optimize international trade logistics. By integrating five distinct relational datasets, the engine calculates the **"True Landed Cost"** of goods — accounting for local unit pricing, real-time currency exchange rates, and regional tariff structures.

---

## 📑 Project Overview

In global commerce, the lowest sticker price rarely represents the lowest final cost. **TradeRoute** automates the complex task of comparing international suppliers by normalizing global data into a single, actionable procurement report.

### 🔑 Key Engineering Pillars

* **Relational Data Parsing:** Processes five flat-file databases (Countries, Products, Tariffs, Inventory, and Orders) into optimized in-memory structures.
* **Currency Normalization:** Converts origin-country pricing into a base currency using ISO-mapped exchange rates found in `country.txt`.
* **Tariff Logic:** Applies percentage-based trade taxes derived from regional relationships defined in `tariff.txt`.
* **Logistics Optimization:** Iterates through global inventory to identify the **"Best Value"** source for any given product by minimizing the final calculated cost.

---

## 🛠️ Technical Architecture

The system functions as a modular analytical engine, utilizing nested data structures to mimic relational database functionality (SQL-style joins) without external dependencies.

### 📂 The Data Model

* **`country.txt`** — Maps ISO codes to country names and currency exchange rates.
* **`product.txt`** — Catalog of global goods and unique product identifiers.
* **`product_country.txt`** — Relational map of which countries stock specific products and their local unit prices.
* **`tariff.txt`** — Regional tax mapping for international shipping between zones.
* **`shopping_list.txt`** — Target order containing desired products and quantities to be analyzed.

---

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/TradeRoute.git
cd TradeRoute
```

### 2️⃣ Prepare Data

Ensure all `.txt` data files remain in the root directory so the engine can parse them correctly.

### 3️⃣ Run the Analysis

```bash
python Pratap_Kolukuluri_GlobalTradeAnalysis.py
```

---

## 📊 Algorithmic Logic

The engine calculates the final landed cost per item using a structured evaluation pipeline:

```
Final Cost = (Local Unit Price × Currency Exchange Rate) × (1 + Tariff Percentage)
```

This ensures a fair **"apples-to-apples" comparison** between suppliers across different currency zones while accounting for hidden international trade costs.

---

## 👨‍💻 Developer

**Pratap Kolukuluri**

**Course:** CMPUT 175 — University of Alberta
**Core Competencies:** Data Engineering, Python Scripting, Relational Logic, Cost Optimization

---
