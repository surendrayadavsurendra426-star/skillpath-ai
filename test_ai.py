import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="SkillPath AI - Surendra Yadav", page_icon="🚀")

# Sidebar
with st.sidebar:
    st.success("Built by **Surendra Yadav**")
    if st.button("Reset App 🔄"):
        st.rerun()

# API Key Connection Check
if "MY_API_KEY" not in st.secrets:
    st.error("Secrets mein API Key nahi mili! Settings > Secrets check karein.")
    st.stop()

genai.configure(api_key=st.secrets["MY_API_KEY"])

# Main Interface
st.title("🚀 SkillPath: AI Roadmap Generator")
user_goal = st.text_input("Aap kya banna chahte hain?", placeholder="e.g., Video Creator")

if st.button("Generate My Roadmap ✨"):
    if user_goal:
        with st.spinner("Surendra's AI rasta dhoond raha hai..."):
            try:
                # Latest Model
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"3-step roadmap for {user_goal}")
                
                st.markdown(f"### 📍 Roadmap for: {user_goal}")
                st.markdown(response.text)
                
                # YouTube & Download
                st.divider()
                q = user_goal.replace(" ", "+")
                st.info(f"👉 [Click here for {user_goal} Videos](https://www.youtube.com/results?search_query={q}+course)")
                st.download_button("Download 📄", response.text, file_name="roadmap.txt")
                st.balloons()
                
            except Exception as e:
                st.error(f"Asli Error: {e}")
    else:
        st.warning("Pehle apna goal likhein!")
