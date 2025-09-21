# 💳 Credit Risk Classification  

A machine learning-powered tool that predicts the **credit risk category (Poor, Average, Good, Excellent)** of borrowers using customer demographics, loan details, and bureau data.  
Built with **Scikit-learn**, **Optuna**, and **Streamlit**.  

🔗 **Live Demo** – [Streamlit App](https://prajwal-glitch-credit-risk-classifier-appmain-1mzyat.streamlit.app/)  


---

## 🚀 Features  

- **🧹 Data Cleaning & Preprocessing** – Handled missing values, categorical encoding, outlier treatment, and feature scaling.  
- **🧑‍🔬 Credit Risk Models** – Logistic Regression, Random Forest, XGBoost compared with AUC, KS, and Gini metrics.  
- **⚙️ Hyperparameter Optimization** – Automated tuning with **Optuna** to maximize model performance.  
- **📊 Model Evaluation Metrics** – ROC-AUC: **0.98**, KS Statistic: **45%**, Gini Coefficient: **0.97**.  
- **🌐 Web App Deployment** – Interactive **Streamlit app** for borrower-level risk scoring.  
- **📖 Explainability** – Feature importance, WOE/IV analysis, and score distributions documented in Jupyter notebooks.  

---

## 🖼️ Screenshot  

![Screenshot Placeholder](screenshot.png)  

---



## 🛠️ Installation  

```bash
# Clone this repository
git clone https://github.com/your-username/credit-risk-classification.git
cd credit-risk-classification

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt


## 📂 Project Structure  

