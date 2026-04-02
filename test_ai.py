import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="SkillPath AI - Surendra Yadav", page_icon="🚀")

# --- 2. API SETUP ---
if "MY_API_KEY" not in st.secrets:
    st.error("Secrets mein 'MY_API_KEY' nahi mili! Dashboard par Settings > Secrets mein add karein.")
    st.stop()

# API Configuration
genai.configure(api_key=st.secrets["MY_API_KEY"])

# --- 3. SIDEBAR (Aapka Naam) ---
with st.sidebar:
    st.title("🎯 SkillPath AI")
    st.success("Built by **Surendra Yadav**")
    st.info("System: Model v4.0 (Fixed)")
    if st.button("Reset App 🔄"):
        st.rerun()

# --- 4. MAIN UI ---
st.title("🚀 SkillPath: Personalized Roadmap")
user_goal = st.text_input("Aap kya banna chahte hain?", placeholder="e.g., Video Creator")

# GENERATE BUTTON
if st.button("Generate My Roadmap ✨"):
    if user_goal:
        with st.spinner(f"Surendra's AI aapka '{user_goal}' roadmap taiyar kar raha hai..."):
            try:
                # ERROR FIX: Yahan 'gemini-1.5-flash-latest' use kiya hai bina 'models/' ke
                model = genai.GenerativeModel('gemini-1.5-flash-latest')
                response = model.generate_content(f"Create a 3-step roadmap to become {user_goal}")
                
                st.markdown(f"### 📍 Roadmap for: {user_goal}")
                st.divider()
                st.markdown(response.text)
                
                # VIDEO LINK (YouTube link with search query)
                st.subheader("📺 Learning Resources")
                search_q = user_goal.replace(" ", "+")
                video_url = f"https://www.youtube.com/results?search_query={search_q}+full+course"
                st.info(f"👉 [Surendra ki taraf se Recommendation: Watch {user_goal} Tutorials]({video_url})")
                
                # DOWNLOAD BUTTON
                st.download_button("Download Roadmap 📄", response.text, file_name=f"{user_goal}_roadmap.txt")
                st.balloons()
                
            except Exception as e:
                # Agar abhi bhi error aaye toh ye alternative model try karega
                try:
                    model = genai.GenerativeModel('gemini-1.0-pro')
                    response = model.generate_content(f"3-step roadmap for {user_goal}")
                    st.markdown(response.text)
                except:
                    st.error(f"Technical Error: {str(e)}")
                    st.info("Tip: Streamlit Dashboard par ja kar 'Reboot' button dabayein.")
    else:
        st.warning("Pehle apna goal likhein!")

st.caption("© 2026 SkillPath | Developed by Surendra Yadav")
