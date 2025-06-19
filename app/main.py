import streamlit as st
from prediction_helper import predict

# Page setup
st.set_page_config(page_title="Credit Risk Classifier", page_icon="📊", layout="wide")

st.markdown(
    "<h2 style='text-align: center; color: #4CAF50;'>Credit Risk Classifier</h2>",
    unsafe_allow_html=True
)
st.markdown("### 📋 Enter customer & loan details below")

# Input Layout
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('🎂 Age', 18, 100, value=28, help="Customer's age in years")
        delinquency_ratio = st.number_input('⚠️  Delinquency Ratio (%)', 0, 100, value=30, help="Percentage of delinquent payments")
        residence_type = st.selectbox('🏠 Residence Type', ['Owned', 'Rented', 'Mortgage'])
    with col2:
        income = st.number_input('💰 Annual Income (₹)', min_value=0, value=1200000, step=50000)
        credit_utilization_ratio = st.number_input('📈 Credit Utilization Ratio (%)', 0, 100, value=30, help="Used credit as % of total available")
        loan_purpose = st.selectbox('🎯 Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
    with col3:
        loan_amount = st.number_input('🏦 Loan Amount (₹)', min_value=0, value=2560000, step=100000)
        num_open_accounts = st.number_input('📄 Open Loan Accounts', 1, 4, value=2)
        loan_type = st.selectbox('🔒 Loan Type', ['Unsecured', 'Secured'])

# Calculated Features
loan_to_income_ratio = loan_amount / income if income > 0 else 0
credit_utilization_per_income = credit_utilization_ratio / loan_to_income_ratio if loan_to_income_ratio > 0 else 0

# Tenure and DPD in one row
col4, col5 = st.columns(2)
with col4:
    loan_tenure_months = st.number_input('⏳ Loan Tenure (months)', 0, 480, value=36)
with col5:
    avg_dpd_per_delinquency = st.number_input('📉 Average DPD per Delinquency', 0, 365, value=20)

# Display Calculated Ratios
st.markdown("### 📐 Calculated Ratios")
col6, col7 = st.columns(2)
with col6:
    st.metric("Loan-to-Income Ratio", f"{loan_to_income_ratio:.2f}")
with col7:
    st.metric("Credit Utilization per Income", f"{credit_utilization_per_income:.2f}")

# --- Predict button ---
st.markdown("---")
if st.button("🚀 Calculate Risk", use_container_width=True):
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type, credit_utilization_per_income
    )

    st.success("✅ Prediction Complete")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Default Probability", f"{probability:.2%}")
    with col2:
        st.metric("Credit Score", credit_score)
    with col3:
        st.metric("Rating", rating)


