import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="SkillPath AI - Surendra Yadav", page_icon="🚀")

# --- 2. API SETUP ---
if "MY_API_KEY" not in st.secrets:
    st.error("Secrets mein API Key nahi mili!")
    st.stop()

genai.configure(api_key=st.secrets["MY_API_KEY"])

# --- 3. SIDEBAR ---
with st.sidebar:
    st.success("Built by **Surendra Yadav**")
    st.info("System: Updated Model")
    if st.button("Reboot App 🔄"):
        st.rerun()

# --- 4. MAIN UI ---
st.title("🚀 SkillPath: Personalized Roadmap")
user_goal = st.text_input("Aap kya banna chahte hain?", placeholder="e.g., Video Creator")

if st.button("Generate My Roadmap ✨") and user_goal:
    with st.spinner("AI Response ka intezaar karein..."):
        try:
            # FORCE USING NEW MODEL
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(f"Create a short 3-step roadmap for {user_goal}")
            
            st.subheader(f"📍 Roadmap for: {user_goal}")
            st.markdown(response.text)
            
            # YouTube Link logic
            search_url = f"https://www.youtube.com/results?search_query={user_goal.replace(' ', '+')}+course"
            st.info(f"👉 [Free course: Click here for {user_goal} tutorials]({search_url})")
            
            # Download
            st.download_button("Download Roadmap 📄", response.text, file_name="roadmap.txt")
            st.balloons()
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.warning("Surendra ji, please Streamlit Dashboard par ja kar 'Reboot' button dabayein.")

st.caption("© 2026 SkillPath | Developed by Surendra Yadav")
