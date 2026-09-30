

"""
Crop Recommendation Streamlit App

Loads `crop_recommendation_model.pkl` (created in the notebook) and
provides an interactive UI for predicting the best crop from soil
and climate parameters.
"""
import os
from datetime import datetime

import joblib
import numpy as np
import pandas as pd
import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="🌾 Crop Recommendation",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown(
    """
    <style>
    .main-header {
        background: linear-gradient(135deg, #2E7D32 0%, #4CAF50 100%);
        padding: 1.5rem 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 1.5rem;
    }
    .main-header h1 { margin: 0; font-size: 2rem; }
    .main-header p  { margin: 0.4rem 0 0 0; opacity: 0.9; }

    .result-card {
        background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%);
        border-left: 6px solid #2E7D32;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .result-card h2 { margin: 0; color: #1B5E20; }
    .result-card .conf { font-size: 1.1rem; color: #2E7D32; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# CONSTANTS (must match training order)
# ============================================================
MODEL_PATH = "crop_recommendation_model.pkl"

# ============================================================
# LOAD MODEL (cached — loaded once per session)
# ============================================================
@st.cache_resource(show_spinner="🔄 Loading model…")
def load_artifacts(path: str):
    """Load the pickled dict from the notebook."""
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"❌ Model file `{path}` not found. "
            "Run the notebook and save `crop_recommendation_model.pkl` "
            "in the same folder as this app."
        )
    return joblib.load(path)


# ============================================================
# PREDICTION HELPERS
# ============================================================
def make_input_df(values: dict, feature_names: list) -> pd.DataFrame:
    """Build a single-row DataFrame in the exact training order."""
    return pd.DataFrame([{f: values[f] for f in feature_names}])


def predict(artifacts: dict, values: dict, top_k: int = 5) -> dict:
    """Return prediction + confidence + top-K probabilities."""
    model = artifacts["model"]
    scaler = artifacts["scaler"]
    le = artifacts["label_encoder"]
    features = artifacts["feature_names"]
    use_scaled = artifacts["use_scaled"]

    row = make_input_df(values, features)
    X = scaler.transform(row) if use_scaled else row.values

    pred_idx = int(model.predict(X)[0])

    # Some models (e.g. SVM without probability=True) don't support predict_proba
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(X)[0]
        confidence = float(probs[pred_idx])
        order = np.argsort(probs)[::-1][:top_k]
        top = [
            {"crop": str(le.classes_[i]), "probability": float(probs[i])}
            for i in order
        ]
    else:
        confidence = 1.0
        top = [{"crop": str(le.classes_[pred_idx]), "probability": 1.0}]

    return {
        "prediction": str(le.classes_[pred_idx]),
        "confidence": confidence,
        "top_k": top,
    }


# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("## 🌾 Crop Recommender")
    st.caption("ML-powered crop prediction")

    page = st.radio(
        "Navigation",
        ["🔮 Predict", "📊 Batch Predict", "ℹ️ Model Info", "📖 About"],
        label_visibility="collapsed",
    )

    st.divider()

    # Load model
    try:
        artifacts = load_artifacts(MODEL_PATH)
        st.success("✅ Model loaded")
    except Exception as e:
        st.error(str(e))
        st.stop()

    # Quick stats
    meta = artifacts
    st.markdown("**Model**")
    st.markdown(
        f"- **Type:** {meta.get('model_name', 'N/A')}\n"
        f"- **Accuracy:** {meta.get('accuracy', 0) * 100:.2f}%\n"
        f"- **Crops:** {len(meta.get('crop_classes', []))}\n"
        f"- **Features:** {len(meta.get('feature_names', []))}"
    )

    st.divider()
    st.caption(f"🕐 {datetime.now().strftime('%H:%M:%S')}")


# ============================================================
# HEADER
# ============================================================
st.markdown(
    """
    <div class="main-header">
        <h1>🌾 Crop Recommendation System</h1>
        <p>Enter soil &amp; climate parameters → get the best crop to grow</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PAGE — PREDICT
# ============================================================
if page == "🔮 Predict":
    st.subheader("🎛️ Enter Soil & Climate Parameters")

    with st.form("prediction_form"):
        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("**🧪 Soil Nutrients**")
            nitrogen = st.slider(
                "Nitrogen (N)", 0, 140, 90, 1,
                help="kg/ha — typical range 0–140",
            )
            phosphorus = st.slider(
                "Phosphorus (P)", 5, 145, 42, 1,
                help="kg/ha — typical range 5–145",
            )
            potassium = st.slider(
                "Potassium (K)", 5, 205, 43, 1,
                help="kg/ha — typical range 5–205",
            )

        with c2:
            st.markdown("**🌡️ Climate**")
            temperature = st.slider(
                "Temperature (°C)", 8.0, 44.0, 20.9, 0.1,
                help="Average ambient temperature",
            )
            humidity = st.slider(
                "Humidity (%)", 14.0, 100.0, 82.0, 0.1,
                help="Relative humidity",
            )
            rainfall = st.slider(
                "Rainfall (mm)", 20.0, 300.0, 202.9, 1.0,
                help="Annual rainfall",
            )

        with c3:
            st.markdown("**⚗️ Soil Chemistry**")
            ph = st.slider(
                "pH Value", 3.5, 10.0, 6.5, 0.1,
                help="Soil pH — 7 is neutral",
            )

            st.markdown("&nbsp;")
            st.markdown("**📌 Quick presets**")
            preset = st.selectbox(
                "Load a preset",
                ["— custom —", "Rice field", "Maize field", "Cotton field",
                 "Coffee plantation", "Grapes vineyard", "Banana farm"],
                label_visibility="collapsed",
            )

        # ---- Presets ----
        if preset == "Rice field":
            nitrogen, phosphorus, potassium = 90, 42, 43
            temperature, humidity, ph, rainfall = 20.9, 82.0, 6.5, 202.9
        elif preset == "Maize field":
            nitrogen, phosphorus, potassium = 71, 54, 16
            temperature, humidity, ph, rainfall = 22.6, 63.7, 5.7, 87.8
        elif preset == "Cotton field":
            nitrogen, phosphorus, potassium = 133, 47, 24
            temperature, humidity, ph, rainfall = 24.4, 79.2, 7.2, 90.8
        elif preset == "Coffee plantation":
            nitrogen, phosphorus, potassium = 91, 21, 26
            temperature, humidity, ph, rainfall = 26.3, 57.4, 7.3, 191.7
        elif preset == "Grapes vineyard":
            nitrogen, phosphorus, potassium = 24, 130, 195
            temperature, humidity, ph, rainfall = 30.0, 81.5, 6.1, 67.1
        elif preset == "Banana farm":
            nitrogen, phosphorus, potassium = 100, 82, 50
            temperature, humidity, ph, rainfall = 27.4, 80.5, 6.0, 105.0

        submitted = st.form_submit_button(
            "🔮 Predict Best Crop",
            type="primary",
            use_container_width=True,
        )

    # ---------------- Handle prediction ----------------
    if submitted:
        inputs = {
            "Nitrogen": nitrogen,
            "Phosphorus": phosphorus,
            "Potassium": potassium,
            "Temperature": temperature,
            "Humidity": humidity,
            "pH_Value": ph,
            "Rainfall": rainfall,
        }

        with st.spinner("🌱 Analyzing soil and climate…"):
            try:
                result = predict(artifacts, inputs)
            except Exception as e:
                st.error(f"❌ Prediction failed: {e}")
                st.stop()

        # Save in session so it survives reruns
        st.session_state["last_prediction"] = {**inputs, **result}

    # ---------------- Display result ----------------
    if "last_prediction" in st.session_state:
        r = st.session_state["last_prediction"]
        conf = r["confidence"]

        st.markdown(
            f"""
            <div class="result-card">
                <h2>🌱 Recommended Crop: {r['prediction'].title()}</h2>
                <div class="conf">
                    Confidence: <strong>{conf * 100:.2f}%</strong>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Metrics
        m1, m2, m3 = st.columns(3)
        m1.metric("Confidence", f"{conf * 100:.1f}%")
        m2.metric("Model", artifacts.get("model_name", "—"))
        m3.metric("Model Accuracy", f"{artifacts.get('accuracy', 0) * 100:.1f}%")

        st.divider()

        # Top-K chart
        if len(r["top_k"]) > 1:
            st.subheader("📊 Top Probable Crops")
            top_df = pd.DataFrame(r["top_k"])
            top_df = top_df.rename(
                columns={"crop": "Crop", "probability": "Probability"}
            )
            st.bar_chart(top_df.set_index("Crop")["Probability"])

            with st.expander("🔢 Full probability table"):
                tbl = top_df.copy()
                tbl["Probability"] = (
                    tbl["Probability"] * 100
                ).round(2).astype(str) + "%"
                st.dataframe(tbl, use_container_width=True, hide_index=True)

        # Input summary
        with st.expander("📥 Input parameters used"):
            inp = pd.DataFrame([
                {"Feature": k, "Value": r[k]}
                for k in artifacts["feature_names"]
            ])
            st.dataframe(inp, use_container_width=True, hide_index=True)


# ============================================================
# PAGE — BATCH PREDICT
# ============================================================
elif page == "📊 Batch Predict":
    st.subheader("📊 Batch Prediction from CSV")
    st.caption(
        f"Upload a CSV with these columns: "
        f"`{', '.join(artifacts['feature_names'])}`"
    )

    uploaded = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded is not None:
        try:
            df_in = pd.read_csv(uploaded)

            missing = [
                c for c in artifacts["feature_names"]
                if c not in df_in.columns
            ]
            if missing:
                st.error(f"❌ Missing columns: {missing}")
                st.stop()

            st.markdown(f"**Preview** — {len(df_in):,} rows")
            st.dataframe(df_in.head(), use_container_width=True, hide_index=True)

            if st.button("🚀 Run batch prediction", type="primary"):
                with st.spinner(f"Predicting {len(df_in):,} rows…"):
                    model = artifacts["model"]
                    scaler = artifacts["scaler"]
                    le = artifacts["label_encoder"]
                    features = artifacts["feature_names"]
                    use_scaled = artifacts["use_scaled"]

                    X = df_in[features].fillna(df_in[features].mean())
                    X_input = scaler.transform(X) if use_scaled else X.values

                    preds = model.predict(X_input)
                    out = df_in.copy()
                    out["Predicted_Crop"] = le.inverse_transform(preds)

                    if hasattr(model, "predict_proba"):
                        out["Confidence"] = (
                            model.predict_proba(X_input).max(axis=1).round(4)
                        )

                st.success(f"✅ Predicted {len(out):,} rows")

                st.markdown("**Predicted crop counts**")
                st.bar_chart(out["Predicted_Crop"].value_counts())

                st.markdown("**Results**")
                st.dataframe(out, use_container_width=True, hide_index=True)

                st.download_button(
                    "⬇️ Download results (CSV)",
                    data=out.to_csv(index=False).encode("utf-8"),
                    file_name="crop_predictions.csv",
                    mime="text/csv",
                    use_container_width=True,
                )

        except Exception as e:
            st.error(f"❌ Error processing CSV: {e}")

    # Sample template
    with st.expander("🧪 Download a CSV template"):
        sample = pd.DataFrame([
            [90, 42, 43, 20.9, 82.0, 6.5, 202.9],
            [71, 54, 16, 22.6, 63.7, 5.7, 87.8],
            [24, 130, 195, 30.0, 81.5, 6.1, 67.1],
        ], columns=artifacts["feature_names"])
        st.dataframe(sample, use_container_width=True, hide_index=True)
        st.download_button(
            "⬇️ Download template.csv",
            data=sample.to_csv(index=False).encode("utf-8"),
            file_name="template.csv",
            mime="text/csv",
            use_container_width=True,
        )


# ============================================================
# PAGE — MODEL INFO
# ============================================================
elif page == "ℹ️ Model Info":
    st.subheader("ℹ️ Model Information")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### 📦 Model details")
        st.markdown(
            f"""
            - **Type**: `{artifacts.get('model_name', '—')}`
            - **Features**: `{len(artifacts['feature_names'])}`
            - **Classes**: `{len(artifacts['crop_classes'])}`
            - **Scaled input**: `{artifacts['use_scaled']}`
            """
        )

    with c2:
        st.markdown("### 📈 Performance")
        st.metric(
            "Test accuracy",
            f"{artifacts.get('accuracy', 0) * 100:.2f}%",
        )

    st.divider()

    st.markdown("### 🎯 Supported crops")
    crops = sorted(artifacts["crop_classes"])
    cols = st.columns(5)
    for i, crop in enumerate(crops):
        cols[i % 5].markdown(f"- {crop}")

    st.divider()

    st.markdown("### 🔢 Feature importances")
    model = artifacts["model"]
    if hasattr(model, "feature_importances_"):
        imp = pd.DataFrame({
            "Feature": artifacts["feature_names"],
            "Importance": model.feature_importances_,
        }).sort_values("Importance", ascending=False)
        st.bar_chart(imp.set_index("Feature")["Importance"])
        st.dataframe(
            imp.assign(
                Importance=lambda d: (
                    d["Importance"] * 100
                ).round(2).astype(str) + "%"
            ),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info(
            f"`{artifacts['model_name']}` doesn't expose "
            "`feature_importances_`."
        )


# ============================================================
# PAGE — ABOUT
# ============================================================
elif page == "📖 About":
    st.subheader("📖 About This App")

    st.markdown(
        """
        ### 🌾 Crop Recommendation System

        This app uses a machine learning model trained on the
        **Crop Recommendation dataset** to suggest the best crop
        based on soil nutrients and climate conditions.

        ### 🎯 Inputs (7 features)

        | Feature | Description | Typical range |
        |---|---|---|
        | **Nitrogen (N)** | Soil nitrogen | 0 – 140 kg/ha |
        | **Phosphorus (P)** | Soil phosphorus | 5 – 145 kg/ha |
        | **Potassium (K)** | Soil potassium | 5 – 205 kg/ha |
        | **Temperature** | Ambient temperature | 8 – 44 °C |
        | **Humidity** | Relative humidity | 14 – 100 % |
        | **pH Value** | Soil acidity/alkalinity | 3.5 – 10 |
        | **Rainfall** | Annual rainfall | 20 – 300 mm |

        ### 🧠 How it works

        1. Load the trained model from `crop_recommendation_model.pkl`
        2. **Scale** inputs (only if the model was trained on scaled data)
        3. **Predict** with the classifier
        4. **Decode** the class with the saved `LabelEncoder`
        5. Return the crop + confidence + top-5 alternatives

        ### ⚙️ Tech stack

        - **Streamlit** — UI
        - **scikit-learn** — ML
        - **pandas / numpy** — data
        - **joblib** — model persistence
        """
    )


# ============================================================
# FOOTER
# ============================================================
st.divider()
st.caption(
    f"🌾 Crop Recommendation · "
    f"Model: {artifacts.get('model_name', '—')} · "
    f"Accuracy: {artifacts.get('accuracy', 0) * 100:.1f}%"
)