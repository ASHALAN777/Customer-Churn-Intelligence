import streamlit as st
import pandas as pd
import joblib
import os

# ==============================
# ✅ LOAD MODEL
# ==============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "pipeline_model.pkl")

model = joblib.load(model_path)

# ==============================
# 🎯 UI CONFIG
# ==============================

st.set_page_config(page_title="Churn Intelligence", layout="centered")

st.title("📊 Customer Churn Intelligence")
st.caption("💡 Note: Revenue values are in USD ($) based on dataset")

# ==============================
# 🧍 SINGLE CUSTOMER
# ==============================

st.subheader("🧍 Single Customer Prediction")

tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly = st.number_input("Monthly Charges ($)", 0.0, 200.0, 50.0)

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])

# ==============================
# 🔮 SINGLE PREDICTION
# ==============================

if st.button("🔍 Analyze Customer Risk"):

    input_df = pd.DataFrame([{
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "Contract": contract,
        "InternetService": internet,
        "Dependents": dependents
    }])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    # Risk level
    if probability >= 0.5:
        st.error(f"🔴 High Risk ({probability:.2%})")
    elif probability >= 0.3:
        st.warning(f"🟠 Medium Risk ({probability:.2%})")
    else:
        st.success(f"🟢 Low Risk ({probability:.2%})")

    # Revenue risk (USD)
    revenue_risk = monthly * 12 * probability
    st.write(f"💰 Estimated Revenue Risk: ${revenue_risk:.2f}")

    # Insights
    st.subheader("🔍 Insights")

    insights = []
    if tenure < 6:
        insights.append("Low tenure increases churn risk")
    if contract == "Month-to-month":
        insights.append("Month-to-month contracts are high risk")
    if internet == "Fiber optic":
        insights.append("Fiber users show higher churn")
    if dependents == "No":
        insights.append("Customers without dependents churn more")

    if not insights:
        insights.append("Customer profile looks stable")

    for i in insights:
        st.write(f"⚠️ {i}")

# ==============================
# 📂 BULK PREDICTION
# ==============================

st.subheader("📂 Bulk Prediction (Upload CSV)")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)

        st.write("### 📄 Uploaded Data")
        st.write(data.head())

        # Predictions
        preds = model.predict(data)
        probs = model.predict_proba(data)[:, 1]

        data["Churn Prediction"] = preds
        data["Churn Probability"] = probs

        st.write("### 📊 Prediction Results")
        st.write(data.head())

        # ==============================
        # 📊 DASHBOARD
        # ==============================

        st.subheader("📊 Dashboard")

        # Churn distribution
        st.write("### Churn Distribution")
        st.bar_chart(data["Churn Prediction"].value_counts())

        # Probability distribution
        st.write("### Churn Probability")
        st.line_chart(data["Churn Probability"])

        # Revenue risk (USD)
        data["Revenue Risk ($)"] = data["MonthlyCharges"] * 12 * data["Churn Probability"]

        total_risk = data["Revenue Risk ($)"].sum()

        st.write(f"💰 Total Revenue at Risk: ${total_risk:.2f}")

        # Download
        csv = data.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Results", csv, "churn_predictions.csv", "text/csv")

    except Exception as e:
        st.error(f"Error: {e}")