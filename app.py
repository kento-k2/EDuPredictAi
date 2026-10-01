import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt
from src.predict import predict_student

# Load model artifacts
model = joblib.load("models/model.pkl")
explainer = joblib.load("models/explainer.pkl")

# --- 1. PREMIUM PAGE SETUP ---
st.set_page_config(
    layout="wide", 
    page_title="EduPredictAI Dashboard",
    page_icon="🎓"
)

# Apply global dark mode chart properties uniformly across the script
plt.style.use('dark_background')
CHART_COLOR = '#0e1117'

def apply_dark_theme(fig, ax):
    fig.patch.set_facecolor(CHART_COLOR)
    ax.set_facecolor(CHART_COLOR)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#444444')
    ax.spines['bottom'].set_color('#444444')
    ax.grid(True, linestyle='--', alpha=0.1, color='#FFFFFF')

# --- 2. INJECT GLOWING MODERN CSS LAYOUT STYLES ---
st.markdown("""
    <style>
        .block-container { padding-top: 1.5rem; padding-bottom: 1.5rem; }
        h1 { font-weight: 800 !important; letter-spacing: -0.5px; margin-bottom: 0px; }
        h3 { font-weight: 700 !important; color: #E0E0E0; margin-top: 1.5rem; }
        .stButton>button { 
            background-color: #1E88E5; color: white; border-radius: 8px; 
            width: 100%; font-weight: bold; border: none; height: 2.8rem;
            transition: all 0.3s ease;
        }
        .stButton>button:hover { background-color: #1565C0; box-shadow: 0px 4px 12px rgba(30,136,229,0.3); }
        .card-container { background-color: #1e2530; border-radius: 8px; padding: 15px; border: 1px solid #2d3748; }
    </style>
""", unsafe_allow_html=True)

# --- 3. HEADER ARCHITECTURE ---
st.title("🎓 EduPredictAI")
st.caption("⚡ Advanced Machine Learning Pipeline for Academic Risk & Performance Analytics")
st.markdown("---")

# --- 4. STREAMLINED SIDEBAR CONTROLS ---
with st.sidebar:
    st.header("🎛️ Student Input")
    st.markdown("Adjust performance parameters to evaluate risk live:")
    
    with st.container(border=True):
        study_hours = st.slider("📚 Study Hours", 0.0, 10.0, 5.0, step=0.5)
        attendance = st.slider("🏫 Attendance (%)", 0.0, 100.0, 75.0, step=1.0)
        assignments = st.slider("📝 Assignments", 0.0, 100.0, 60.0, step=1.0)
        quizzes = st.slider("❓ Quizzes", 0.0, 100.0, 60.0, step=1.0)

input_data = {
    "study_hours": study_hours,
    "attendance": attendance,
    "assignments": assignments,
    "quizzes": quizzes
}

# --- 5. LIVE PREDICTION SUMMARY ---
st.subheader("📊 Live Prediction Summary")

with st.container(border=True):
    col_btn, col_metrics = st.columns([1, 3])
    
    with col_btn:
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        run_trigger = st.button("Run Prediction")
        
    with col_metrics:
        c1, c2, c3 = st.columns(3)
        if run_trigger:
            result = predict_student(input_data)
            
            # Dynamic visual coloring logic based on risk tier
            is_high_risk = result["risk_level"] == "High Risk"
            risk_color = "#EF5350" if is_high_risk else "#FFA726" if result["risk_level"] == "Medium Risk" else "#4CAF50"
            
            c1.markdown(f"<div class='card-container'><p style='margin:0;color:#888;font-size:0.9rem;'>Outcome</p><h2 style='margin:0;color:#FFF;'>{result['prediction']}</h2></div>", unsafe_allow_html=True)
            c2.markdown(f"<div class='card-container'><p style='margin:0;color:#888;font-size:0.9rem;'>Confidence Pass Prob.</p><h2 style='margin:0;color:#4FC3F7;'>{result['probability']:.2f}</h2></div>", unsafe_allow_html=True)
            c3.markdown(f"<div class='card-container'><p style='margin:0;color:#888;font-size:0.9rem;'>Calculated Status</p><h2 style='margin:0;color:{risk_color};'>{result['risk_level']}</h2></div>", unsafe_allow_html=True)
            
            st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
            
            # UPGRADE FEATURE 1: HIGH RISK ALERT BANNER
            if is_high_risk:
                st.error("🚨 **CRITICAL NOTICE:** This student profile demonstrates significant academic risk metrics. Immediate advisor counseling required.")
            
            # UPGRADE FEATURE 2: TARGET LOGIC OPTIMIZATION CALCULATOR
            st.markdown("#### 🎯 Target Improvement Planner")
            if result["prediction"] == "Fail" or is_high_risk:
                st.warning("💡 **Recovery Path:** To transition this student profile back to a secure **Pass** zone, prioritize lifting **Attendance above 75%** and scheduling target quiz review sessions.")
            else:
                st.success("✅ **Maintenance Path:** Performance metrics are stable. Ensure student maintains baseline study hours and regular attendance metrics.")

            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
            st.markdown("**⚡ Recommended Intervention Matrix:**")
            for i in result["interventions"]:
                st.markdown(f"🔹 <span style='font-size:0.95rem;color:#E0E0E0;'>{i}</span>", unsafe_allow_html=True)
        else:
            c1.metric("Prediction", "--")
            c2.metric("Probability", "--")
            c3.metric("Risk", "--")

# --- 6. ADVANCED XAI MODEL INSIGHTS (SHAP + WHAT-IF) ---
st.markdown("---")
st.subheader("🔍 Analytical Interpretability & Insights")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("<p style='font-weight:600;margin-bottom:10px;'>🧠 Feature Contribution Impact (SHAP Values)</p>", unsafe_allow_html=True)
        df = pd.DataFrame([input_data])
        shap_values = explainer(df)

        values = shap_values.values
        if len(values.shape) == 3:
            values = values[0, :, 1]
        elif len(values.shape) == 2:
            values = values[0]

        values = values.flatten()

        shap_df = pd.DataFrame({
            "Feature": df.columns,
            "Impact": values
        }).sort_values(by="Impact", key=abs)

        fig, ax = plt.subplots(figsize=(6, 3.8))
        colors = ['#EF5350' if x < 0 else '#4CAF50' for x in shap_df["Impact"]]
        ax.barh(shap_df["Feature"], shap_df["Impact"], color=colors, height=0.5)
        apply_dark_theme(fig, ax)
        ax.set_title("Feature Contribution to Pass Probability", fontsize=10, pad=10)
        ax.tick_params(labelsize=9)
        fig.tight_layout() # FIXED: Prevents left axis labels from cutting off
        st.pyplot(fig, use_container_width=True)

with col2:
    with st.container(border=True):
        st.markdown("<p style='font-weight:600;margin-bottom:10px;'>📈 Simulation Analytics: Study Hours vs Probability</p>", unsafe_allow_html=True)
        sim_hours = list(range(1, 11))
        probs = []

        for h in sim_hours:
            temp = input_data.copy()
            temp["study_hours"] = h
            res = predict_student(temp)
            probs.append(res["probability"])

        fig2, ax2 = plt.subplots(figsize=(6, 3.8))
        ax2.plot(sim_hours, probs, marker='o', color='#29B6F6', linewidth=2, markersize=6)
        apply_dark_theme(fig2, ax2)
        ax2.set_title("Sensitivity Curve (Marginal Impact Analysis)", fontsize=10, pad=10)
        ax2.set_xlabel("Weekly Study Hours Input", fontsize=8, color='#888888')
        ax2.set_ylabel("Predicted Pass Probability", fontsize=8, color='#888888')
        ax2.tick_params(labelsize=9)
        fig2.tight_layout() # FIXED: Ensures standard bounds padding inside container blocks
        st.pyplot(fig2, use_container_width=True)

# --- 7. PREMIUM BATCH CSV UPLOADER WITH STUDENT NAMES TRACKING ---
st.markdown("---")
st.subheader("📂 Batch Processing Engine")

with st.container(border=True):
    uploaded_file = st.file_uploader("Drop class roster spreadsheet file here (.CSV format)", type=["csv"])

    if uploaded_file:
        df_batch = pd.read_csv(uploaded_file)
        
        results = []
        for _, row in df_batch.iterrows():
            model_features = {
                "study_hours": row["study_hours"],
                "attendance": row["attendance"],
                "assignments": row["assignments"],
                "quizzes": row["quizzes"]
            }
            res = predict_student(model_features)
            results.append({
                "prediction": res["prediction"],
                "probability": round(res["probability"], 2),
                "risk_level": res["risk_level"],
                "interventions": ", ".join(res["interventions"])
            })

        result_df = pd.DataFrame(results)
        final_df = pd.concat([df_batch, result_df], axis=1)

        st.markdown("**📋 Evaluated Class Roster Table Output:**")
        st.dataframe(final_df, height=280, use_container_width=True)

        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        
        # Aggregated Metrics Container Layout
        bc1, bc2, bc3 = st.columns(3)
        bc1.metric("Total Students Processed", len(final_df))
        bc2.metric("High Risk Flags Triggered", (final_df["risk_level"] == "High Risk").sum(), delta="Action Needed", delta_color="inverse")
        bc3.metric("Projected Pass Rate Metric", f"{(final_df['prediction'] == 'Pass').mean()*100:.1f}%")

        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        
        # Compact Distribution Visual
        col_chart, col_dl = st.columns(2)
        with col_chart:
            risk_counts = final_df["risk_level"].value_counts()
            fig3, ax3 = plt.subplots(figsize=(5, 2.5))
            
            palette = {'Low Risk': '#4CAF50', 'Medium Risk': '#FFA726', 'High Risk': '#EF5350'}
            bar_colors = [palette.get(x, '#29B6F6') for x in risk_counts.index]
            
            ax3.bar(risk_counts.index, risk_counts.values, color=bar_colors, width=0.4)
            apply_dark_theme(fig3, ax3)
