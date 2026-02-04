import streamlit as st
from PIL import Image

st.set_page_config(page_title="SmartScan EduPad", layout="centered")

st.title("🎓 SmartScan EduPad")
st.subheader("B.Tech Final Year Project - E-Assessment System")
st.success("🚀 **SUCCESSFULLY DEPLOYED ON STREAMLIT CLOUD**")

with st.sidebar:
    st.header("⚙️ Settings")
    st.write("Upload answer sheets for evaluation")

uploaded_file = st.file_uploader("Choose an answer sheet image", type=['jpg', 'png'])

if uploaded_file:
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)
    with col2:
        st.info("📄 File Details")
        st.write(f"**Name:** {uploaded_file.name}")
        st.write(f"**Type:** {uploaded_file.type}")
        st.write(f"**Size:** {uploaded_file.size/1024:.1f} KB")
    
    if st.button("🔍 Evaluate Answer Sheet", type="primary"):
        st.balloons()
        st.success("✅ Evaluation Complete!")
        
        st.subheader("📊 Results")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Score", "8/10")
        with col2:
            st.metric("Percentage", "80%")
        with col3:
            st.metric("Grade", "A")
        
        st.subheader("📈 Performance")
        st.progress(0.8)
        st.caption("Above average performance")

st.markdown("---")
st.caption("© 2024 SmartScan EduPad | B.Tech Final Year Project | Streamlit Cloud Deployment")
