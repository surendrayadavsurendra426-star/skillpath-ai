import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="SkillPath AI - Surendra Yadav", page_icon="🚀")

# --- 2. API SETUP ---
if "MY_API_KEY" not in st.secrets:
    st.error("Secrets mein 'MY_API_KEY' add karein!")
    st.stop()

genai.configure(api_key=st.secrets["MY_API_KEY"])

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("🎯 SkillPath AI")
    st.success("Built by **Surendra Yadav**")
    if st.button("Reset App 🔄"):
        st.rerun()

# --- 4. MAIN UI ---
st.title("🚀 SkillPath: AI Roadmap Generator")
user_goal = st.text_input("Aap kya banna chahte hain?", placeholder="e.g., Video Creator")

# GENERATE BUTTON
if st.button("Generate My Roadmap ✨"):
    if user_goal:
        with st.spinner("Surendra's AI rasta dhoond raha hai..."):
            try:
                # FIXED MODEL NAME (बिना models/ के)
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Create a 3-step roadmap to become {user_goal}")
                
                st.markdown(f"### 📍 Roadmap for: {user_goal}")
                st.divider()
                st.markdown(response.text)
                
                # VIDEO LINK
                st.subheader("📺 Learning Resources")
                q = user_goal.replace(" ", "+")
                video_url = f"https://www.youtube.com/results?search_query={q}+course"
                st.info(f"👉 [Surendra Yadav ki taraf se recommendation: Watch {user_goal} Tutorials]({video_url})")
                
                # DOWNLOAD
                st.download_button("Download Roadmap 📄", response.text, file_name="roadmap.txt")
                st.balloons()
                
            except Exception as e:
                # Agar abhi bhi error aaye toh ye line asli technical wajah dikhayegi
                st.error(f"Technical Error: {str(e)}")
                st.info("Kripya Streamlit Dashboard par ja kar 'Reboot' button dabayein.")
    else:
        st.warning("Pehle apna goal likhein!")

st.caption("© 2026 SkillPath | Developed by Surendra Yadav")
