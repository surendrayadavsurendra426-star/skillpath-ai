import streamlit as st

# 1. Page Config (Emoji ke saath)
st.set_page_config(
    page_title="SkillPath",
    page_icon="🎯", 
    layout="centered"
)

# 2. Browser ko batane ke liye ki ye ek App hai (Custom CSS)
st.markdown("""
    <style>
    /* Mobile par Streamlit ka menu aur header chhupane ke liye */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Iske niche aapka baki code...
st.set_page_config(
    page_title="SkillPath",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)
import google.generativeai as genai
from fpdf import FPDF

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="SkillPath AI - Surendra Yadav", page_icon="🚀")

# --- 2. API SETUP ---
if "MY_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["MY_API_KEY"])
    model = genai.GenerativeModel("models/gemini-2.5-flash") 
else:
    st.error("Secrets mein API Key nahi mili!")
    st.stop()

# --- 3. MEMORY SETUP (Ye naya hai - Purane data ko bachane ke liye) ---
if 'roadmap_data' not in st.session_state:
    st.session_state.roadmap_data = None
if 'user_goal' not in st.session_state:
    st.session_state.user_goal = ""

# PDF Function
def create_pdf(text, title):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=f"Roadmap: {title}", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    # Cleaning text for PDF
    clean_text = text.replace('*', '').replace('•', '-')
    pdf.multi_cell(0, 10, txt=clean_text.encode('latin-1', 'ignore').decode('latin-1'))
    return pdf.output(dest='S').encode('latin-1')

# --- 4. SIDEBAR (Pahle jaisa hi) ---
with st.sidebar:
    st.title("🎯 SkillPath AI")
    st.success("Built by **Surendra Yadav**")
    if st.button("Reset App 🔄"):
        st.session_state.roadmap_data = None
        st.session_state.user_goal = ""
        st.rerun()

# --- 5. MAIN UI ---
st.title("🚀 SkillPath: AI Roadmap Generator")
# Input field memory se connect kar di hai
input_goal = st.text_input("Aap kya banna chahte hain?", value=st.session_state.user_goal)

# GENERATE BUTTON (Pahle jaisa hi)
if st.button("Generate My Roadmap ✨"):
    if input_goal:
        with st.spinner(f"Surendra's AI roadmap taiyar kar raha hai..."):
            try:
                response = model.generate_content(f"Create a 3-step roadmap to become {input_goal}")
                # Data save kar liya memory mein
                st.session_state.roadmap_data = response.text
                st.session_state.user_goal = input_goal
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle apna goal likhein!")

# --- DISPLAY AREA (Ye data ko gayab nahi hone dega) ---
if st.session_state.roadmap_data:
    st.markdown(f"### 📍 Roadmap for: {st.session_state.user_goal}")
    st.divider()
    st.markdown(st.session_state.roadmap_data)
    
    # Video Link (Pahle jaisa hi)
    st.subheader("📺 Learning Resources")
    q = st.session_state.user_goal.replace(" ", "+")
    st.info(f"👉 [Watch {st.session_state.user_goal} Tutorials on YouTube](https://www.youtube.com/results?search_query={q}+full+course)")
    
    # PDF Download Button (Naya feature)
    pdf_bytes = create_pdf(st.session_state.roadmap_data, st.session_state.user_goal)
    st.download_button(
        label="Download Roadmap as PDF 📄",
        data=pdf_bytes,
        file_name=f"{st.session_state.user_goal}_roadmap.pdf",
        mime="application/pdf"
    )
    st.balloons()

st.caption("© 2026 Developed by Surendra Yadav")
