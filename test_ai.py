import streamlit as st
import google.generativeai as genai
from fpdf import FPDF # PDF ke liye nayi library

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="SkillPath AI - Surendra Yadav", page_icon="🚀")

# --- 2. API SETUP ---
if "MY_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["MY_API_KEY"])
    # Jo model aapne bataya wahi use kar rahe hain
    model = genai.GenerativeModel("models/gemini-2.5-flash") 
else:
    st.error("Secrets mein API Key nahi mili!")
    st.stop()

# PDF Banane ka Function
def create_pdf(text, title):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=f"Roadmap for: {title}", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    # Text ko clean karke PDF mein daalna
    pdf.multi_cell(0, 10, txt=text.encode('latin-1', 'ignore').decode('latin-1'))
    return pdf.output(dest='S').encode('latin-1')

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("🎯 SkillPath AI")
    st.success("Built by **Surendra Yadav**")
    if st.button("Reset App 🔄"):
        st.rerun()

# --- 4. MAIN UI ---
st.title("🚀 SkillPath: AI Roadmap Generator")
user_goal = st.text_input("Aap kya banna chahte hain?", placeholder="e.g., Video Creator")

if st.button("Generate My Roadmap ✨"):
    if user_goal:
        with st.spinner(f"Surendra's AI roadmap taiyar kar raha hai..."):
            try:
                response = model.generate_content(f"Create a professional 3-step roadmap to become {user_goal}.")
                roadmap_text = response.text
                
                st.markdown(f"### 📍 Roadmap for: {user_goal}")
                st.divider()
                st.markdown(roadmap_text)
                
                # Learning Resources (Video Link)
                st.subheader("📺 Learning Resources")
                q = user_goal.replace(" ", "+")
                st.info(f"👉 [Watch {user_goal} Tutorials on YouTube](https://www.youtube.com/results?search_query={q}+full+course)")
                
                # --- PDF DOWNLOAD BUTTON ---
                pdf_data = create_pdf(roadmap_text, user_goal)
                st.download_button(
                    label="Download Roadmap as PDF 📄",
                    data=pdf_data,
                    file_name=f"{user_goal}_Roadmap.pdf",
                    mime="application/pdf"
                )
                
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle apna goal likhein!")

st.caption("© 2026 Developed by Surendra Yadav")
