# 📊 Customer Churn Intelligence

> Predict customer churn, estimate revenue risk, and take data-driven retention actions.

---

## 🚀 Live Demo

👉 *(Add your Streamlit link here after deployment)*

---

## 📌 Problem Statement

Customer churn is a major challenge for subscription-based businesses.
Losing customers directly impacts revenue and growth.

This project helps:

* Identify customers likely to churn
* Estimate potential revenue loss
* Provide actionable business insights

---

## 🧠 Solution

A machine learning-powered web app that:

✔ Predicts churn probability
✔ Estimates revenue at risk
✔ Explains *why* customers churn
✔ Supports bulk prediction via CSV
✔ Visualizes churn trends with dashboards

---

## 🔥 Key Features

* 🎯 **Churn Prediction (Probability-based)**
* 💰 **Revenue Risk Estimation**
* 🔍 **Customer Insights (Explainability)**
* 📂 **Bulk CSV Prediction**
* 📊 **Interactive Dashboard**
* 📥 **Downloadable Results**

---

## 🧪 Tech Stack

* **Python**
* **Pandas**
* **scikit-learn (Pipeline + Random Forest)**
* **Streamlit**
* **Joblib**

---

## 🤖 Machine Learning

* Model: Random Forest Classifier
* Pipeline: Preprocessing + Model combined
* Features used:

  * Tenure
  * Monthly Charges
  * Contract Type
  * Internet Service
  * Dependents

---

## 💰 Business Impact

This tool helps companies:

* Reduce churn with early detection
* Prioritize high-risk customers
* Estimate financial impact before loss
* Improve retention strategy

---

## 📊 Example Output

* Churn Risk: **High / Medium / Low**
* Probability: **53%**
* Revenue Risk: **$318**
* Insights:

  * Low tenure increases churn
  * Month-to-month contracts are high risk

---

## 📂 Project Structure

```bash
churn-intelligence/
│
├── app/
│   └── app.py
├── models/
│   └── pipeline_model.pkl
├── data/
│   └── sample.csv
├── src/
│   └── train.py
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

---

## 📂 Bulk Prediction Format

CSV must include:

```text
tenure,MonthlyCharges,Contract,InternetService,Dependents
```

---

## 📸 Screenshots

 Pictures will be added soon

---

## 🚀 Future Improvements

* SHAP explainability (visual)
* Real-time data integration
* SaaS dashboard UI
* API deployment

---

## 👤 Author

**Alan**

---

## ⭐ If you like this project

Give it a star ⭐ and share feedback!
