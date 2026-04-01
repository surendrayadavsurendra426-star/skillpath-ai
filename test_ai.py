import streamlit as st
import google.generativeai as genai
import time
from streamlit_mic_recorder import speech_to_text
import urllib.parse
from fpdf import FPDF # PDF ke liye

# 1. Page Configuration
st.set_page_config(page_title="SkillPath AI Pro", page_icon="🎯", layout="wide")

# --- 🎨 CSS ---
st.markdown("""
    <style>
    .main { background: #f8f9fa; }
    .stDownloadButton > button {
        background-color: #007BFF !important;
        color: white !important;
        border-radius: 12px !important;
        width: 100% !important;
        height: 3.5em !important;
        font-weight: bold !important;
        border: none !important;
    }
    .whatsapp-btn {
        background-color: #25D366; color: white; padding: 12px;
        text-decoration: none; border-radius: 12px; font-weight: bold;
        display: block; text-align: center; margin-top: 10px;
    }
    .welcome-text { text-align: center; color: #1E3A8A; }
    </style>
    """, unsafe_allow_html=True)

# 2. API Key Setup
API_KEY = "YOUR_API_KEY_HERE" 
genai.configure(api_key="AIzaSyDsXhRYQzTYswkWOX1Fr-y3MTpCIU9gtp4")

# --- 🧠 SESSION STATE ---
if "roadmap_text" not in st.session_state:
    st.session_state.roadmap_text = ""
if "last_skill" not in st.session_state:
    st.session_state.last_skill = ""

# --- 📄 PDF GENERATOR FUNCTION ---
def create_pdf(text, skill_name):
    pdf = FPDF()
    pdf.add_page()
    # Header
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=f"SkillPath AI: {skill_name} Roadmap", ln=True, align='C')
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt="Created by Mr. Surendra Yadav", ln=True, align='C')
    pdf.ln(10)
    # Body
    pdf.set_font("Arial", size=12)
    # Text ko PDF mein sahi se fit karne ke liye formatting
    pdf.multi_cell(0, 10, txt=text.encode('latin-1', 'ignore').decode('latin-1'))
    return pdf.output(dest='S').encode('latin-1')

# --- 🚩 UI ---
st.markdown("<h1 class='welcome-text'>✨ Welcome to SkillPath AI ✨</h1>", unsafe_allow_html=True)
st.divider()

with st.sidebar:
    st.title("SkillPath Settings")
    language = st.selectbox("🌍 Select Language:", ("Hinglish", "Hindi", "English"))
    st.write("Developed by: **Mr. Surendra Yadav** 🚀")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.write("🎙️ **Bolkar batayein ya type karein:**")
    voice_input = speech_to_text(language='en', start_prompt="🎙️ Click to Speak", key='voice')
    skill = st.text_input("Skill Name:", value=voice_input if voice_input else "", placeholder="e.g. Python...")
    generate_btn = st.button("Generate My Masterplan 🚀")

if generate_btn and skill:
    bar = st.progress(0)
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        model = genai.GenerativeModel(available_models[0])
        prompt = f"Create a detailed 30-day roadmap for '{skill}' in {language}. Include weekly goals and YouTube links."
        response = model.generate_content(prompt)
        st.session_state.roadmap_text = response.text
        st.session_state.last_skill = skill
        st.balloons()
    except Exception as e:
        st.error(f"Error: {e}")

# --- 📜 DISPLAY & DOWNLOAD ---
if st.session_state.roadmap_text:
    st.markdown(f"## 🗺️ {st.session_state.last_skill} Roadmap")
    st.markdown(st.session_state.roadmap_text)
    
    # PDF Download Button
    pdf_data = create_pdf(st.session_state.roadmap_text, st.session_state.last_skill)
    st.download_button(
        label="📥 Download Professional PDF",
        data=pdf_data,
        file_name=f"{st.session_state.last_skill}_Roadmap.pdf",
        mime="application/pdf"
    )
    
    # WhatsApp Share
    encoded_msg = urllib.parse.quote(f"My {st.session_state.last_skill} Roadmap by SkillPath AI:\n\n{st.session_state.roadmap_text[:500]}...")
    st.markdown(f'<a href="https://wa.me/?text={encoded_msg}" target="_blank" class="whatsapp-btn">📲 Share on WhatsApp</a>', unsafe_allow_html=True)