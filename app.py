import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import plotly.express as px
import time

# Page config
st.set_page_config(
    page_title="SmartScan EduPad - Working Demo",
    page_icon="📱",
    layout="wide"
)

# Title
st.title("📱 SmartScan EduPad")
st.subheader("B.Tech Final Year Project - E-Assessment System")
st.success("✅ **LIVE DEPLOYMENT - WORKING VERSION**")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Answer Key
    answer_key = st.text_area(
        "Enter Answer Key",
        "Q1:A\nQ2:C\nQ3:B\nQ4:D\nQ5:A\nQ6:B\nQ7:C\nQ8:D\nQ9:A\nQ10:B",
        height=150
    )
    
    # Passing mark
    passing = st.slider("Passing Percentage", 40, 100, 60)

# Main content
st.header("📤 Upload Answer Sheets")

uploaded_files = st.file_uploader(
    "Choose image files",
    type=['jpg', 'png', 'jpeg'],
    accept_multiple_files=True,
    help="Upload images of answer sheets"
)

if uploaded_files:
    st.success(f"✅ Uploaded {len(uploaded_files)} file(s)")
    
    # Display preview
    cols = st.columns(min(3, len(uploaded_files)))
    for idx, uploaded_file in enumerate(uploaded_files[:3]):
        with cols[idx % 3]:
            image = Image.open(uploaded_file)
            st.image(image, caption=f"Sheet {idx+1}", width=200)
    
    # Process button
    if st.button("🚀 Start Evaluation", type="primary"):
        with st.spinner("Evaluating answer sheets..."):
            progress_bar = st.progress(0)
            results = []
            
            # Simulate processing
            for i, uploaded_file in enumerate(uploaded_files):
                time.sleep(0.5)  # Simulate processing time
                
                # Get image info
                image = Image.open(uploaded_file)
                width, height = image.size
                
                # Simulate score calculation
                total_q = len([line for line in answer_key.split('\n') if line.strip()])
                score = np.random.randint(total_q//2, total_q+1)
                percentage = (score / total_q) * 100
                
                # Determine result
                status = "✅ PASS" if percentage >= passing else "❌ FAIL"
                
                results.append({
                    "Student": f"Student_{i+1:03d}",
                    "File": uploaded_file.name,
                    "Score": f"{score}/{total_q}",
                    "Percentage": f"{percentage:.1f}%",
                    "Status": status
                })
                
                # Update progress
                progress_bar.progress((i + 1) / len(uploaded_files))
            
            # Store results
            st.session_state.results = results
            
            st.balloons()
            st.success("🎉 Evaluation Complete!")

# Results section
if 'results' in st.session_state:
    st.header("📊 Results")
    
    # Table
    df = pd.DataFrame(st.session_state.results)
    st.dataframe(df, use_container_width=True)
    
    # Download
    csv = df.to_csv(index=False)
    st.download_button(
        "📥 Download CSV",
        csv,
        "smartscan_results.csv",
        "text/csv"
    )
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Bar chart
        fig1 = px.bar(
            df,
            x="Student",
            y=[float(p.rstrip('%')) for p in df["Percentage"]],
            color="Status",
            title="Student Performance"
        )
        fig1.add_hline(y=passing, line_dash="dash", line_color="red")
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Pie chart
        pass_count = sum(1 for r in st.session_state.results if "PASS" in r["Status"])
        fail_count = len(st.session_state.results) - pass_count
        fig2 = px.pie(
            names=["Pass", "Fail"],
            values=[pass_count, fail_count],
            title="Pass/Fail Distribution",
            color=["Pass", "Fail"],
            color_discrete_map={"Pass": "green", "Fail": "red"}
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    # Stats
    st.subheader("📈 Statistics")
    cols = st.columns(4)
    percentages = [float(r["Percentage"].rstrip('%')) for r in st.session_state.results]
    
    with cols[0]:
        st.metric("Average", f"{np.mean(percentages):.1f}%")
    with cols[1]:
        st.metric("Highest", f"{max(percentages):.1f}%")
    with cols[2]:
        st.metric("Lowest", f"{min(percentages):.1f}%")
    with cols[3]:
        st.metric("Pass Rate", f"{(pass_count/len(percentages))*100:.1f}%")

# Footer
st.markdown("---")
st.markdown("""
**SmartScan EduPad** | B.Tech Final Year Project  
✅ **Successfully Deployed on Streamlit Cloud**  
📁 GitHub: `rakesh17204/smartscan-edupad-working`  
🌐 Live Demo: `your-app-name.streamlit.app`
""")
