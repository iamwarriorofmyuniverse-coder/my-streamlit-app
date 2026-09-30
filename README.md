# 🎈 Streamlit & Machine Learning Interactive Apps

A comprehensive collection of interactive web applications, data visualization dashboards, form portals, machine learning model deployments, and exploratory data science Jupyter notebooks built with **Python**, **Streamlit**, and **Scikit-Learn**.

---

## 📱 Included Applications & ML Deployments

* **`mk1.py`** — Text & Markdown Elements, LaTeX rendering ($E=mc^2$), and status blocks.
* **`mk2.py`** — Interactive User Profile & Skills Builder with dynamic widgets.
* **`mk3.py`** — "Guess the Number" Game with `st.session_state` management.
* **`mk4.py`** — Customer & Course Enquiry Portal with `st.form` batching and receipt generation.
* **`mk5.py` – `mk16.py`** — Data visualization dashboards, sales analytics (`sales_data.csv`), student performance graphs, chart plotting, and interactive UI controls.
* **`mk17.py`** — **Annual Exam Marks Predictor**: Interactive ML regression app utilizing `student_annual_marks_model.pkl` to forecast student annual marks based on quarterly exams, half-yearly exams, and extra classes.
* **`mk18.py`** — **Smart Crop Recommendation Platform**: Full-stack multi-feature agricultural ML classifier predicting ideal crop types based on soil (N, P, K, pH) and environmental conditions (temperature, humidity, rainfall).

---

## 📓 Jupyter Notebooks (`notebooks/`)

* **`notebooks/Crop_Recommendation.ipynb`** — End-to-end exploratory data analysis (EDA), feature engineering, and model training for the Crop Recommendation system.
* **`notebooks/Student_Marks_Prediction.ipynb`** — Data preprocessing and regression pipeline for student marks forecasting.
* **`notebooks/Iris_Classification.ipynb`** — Multi-class classification analysis on the classic Iris dataset.

---

## 🛠️ Setup & Installation

```bash
# Clone the repository
git clone https://github.com/iamwarriorofmyuniverse-coder/my-streamlit-app.git
cd my-streamlit-app

# Install dependencies
pip install -r requirements.txt

# Run any application (e.g. mk18.py for Crop Recommendation)
streamlit run mk18.py
```
