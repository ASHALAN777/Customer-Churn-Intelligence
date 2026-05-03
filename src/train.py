import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# ==============================
# 📥 LOAD DATA
# ==============================

df = pd.read_csv("data/processed.csv")

# ==============================
# 🎯 SELECT ONLY REQUIRED FEATURES
# ==============================

features = [
    "tenure",
    "MonthlyCharges",
    "Contract",
    "InternetService",
    "Dependents"
]

X = df[features]
y = df["Churn"]

# ==============================
# 🔀 TRAIN TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# 🔄 PREPROCESSING
# ==============================

categorical_cols = ["Contract", "InternetService", "Dependents"]
numeric_cols = ["tenure", "MonthlyCharges"]

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
    ("num", "passthrough", numeric_cols)
])

# ==============================
# 🤖 MODEL PIPELINE
# ==============================

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(
        n_estimators=100,
        class_weight="balanced",
        random_state=42
    ))
])

# ==============================
# 🏋️ TRAIN
# ==============================

model.fit(X_train, y_train)

# ==============================
# 💾 SAVE MODEL
# ==============================

joblib.dump(model, "models/pipeline_model.pkl")

print("✅ Model trained and saved successfully!")