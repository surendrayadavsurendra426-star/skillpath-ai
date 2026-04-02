import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="SkillPath AI - By Surendra",
    page_icon="🚀",
    layout="wide"
)

# --- 2. SAFE API KEY LOADING ---
# Is section mein error nahi aayega, ye check karega ki key maujood hai ya nahi
if "MY_API_KEY" not in st.secrets:
    st.error("⚠️ API Key nahi mili! Streamlit Cloud ki 'Settings > Secrets' mein 'MY_API_KEY' add karein.")
    st.stop()
else:
    try:
        api_key = st.secrets["MY_API_KEY"]
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
    except Exception as e:
        st.error(f"❌ AI Setup mein error: {e}")
        st.stop()

# --- 3. SIDEBAR (Aapka Naam Yahan Hai) ---
with st.sidebar:
    st.title("🎯 SkillPath AI")
    st.markdown("---")
    st.markdown("### 👨‍💻 Developer")
    st.success("Built by **Surendra**") # Aapka naam hamesha dikhega
    st.info("Aapka personal AI career guide.")
    
    if st.button("Reset App 🔄"):
        st.rerun()

# --- 4. MAIN INTERFACE ---
st.title("🚀 SkillPath: Personalized Roadmap")
st.write("Apna goal likhein aur AI aapka rasta taiyar karega.")

user_goal = st.text_input("Aap kya banna chahte hain?", placeholder="e.g., Video Creator, Web Developer...")

if user_goal:
    with st.spinner(f"Surendra's AI '{user_goal}' ke liye roadmap bana raha hai..."):
        try:
            # AI Prompt
            prompt = f"Create a professional 3-step roadmap for a beginner to become a {user_goal}. Use bullet points for skills in each step."
            
            response = model.generate_content(prompt)
            
            # Result Display
            st.markdown(f"### 📍 Roadmap for: **{user_goal}**")
            st.divider()
            st.markdown(response.text)
            
            st.balloons() # Celebration!
            
        except Exception as e:
            st.error("🤖 AI response nahi de pa raha. Kripya apni API Key check karein ya thodi der baad try karein.")

# Footer
st.markdown("---")
st.caption("© 2024 SkillPath | Developed by Surendra")
