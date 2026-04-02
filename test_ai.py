import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="SkillPath AI - Surendra Yadav", page_icon="🚀")

# --- 2. API SETUP & DEBUG ---
# Hum check kar rahe hain ki key mil rahi hai ya nahi
if "MY_API_KEY" not in st.secrets:
    st.error("❌ Error: API Key 'Secrets' mein nahi mili! Dashboard par ja kar MY_API_KEY add karein.")
    st.stop()
else:
    try:
        api_val = st.secrets["MY_API_KEY"]
        genai.configure(api_key=api_val)
        # Latest model use kar rahe hain
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"❌ Setup Error: {e}")
        st.stop()

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
        with st.spinner("AI Generating..."):
            try:
                # Simple prompt to avoid complex errors
                response = model.generate_content(f"Give a 3-step roadmap to become {user_goal}")
                
                st.markdown(f"### 📍 Roadmap: {user_goal}")
                st.write(response.text)
                
                # VIDEO LINK
                st.divider()
                q = user_goal.replace(" ", "+")
                st.info(f"👉 [Click here to watch {user_goal} Tutorials](https://www.youtube.com/results?search_query={q}+course)")
                
                # DOWNLOAD
                st.download_button("Download Roadmap 📄", response.text, file_name="roadmap.txt")
                st.balloons()
                
            except Exception as e:
                st.error(f"❌ AI Response Fail: {str(e)}")
                st.info("Tip: Check karein ki aapki API Key 'Google AI Studio' se valid hai.")
    else:
        st.warning("Pehle apna goal likhein!")

st.caption("© 2026 SkillPath | Developed by Surendra Yadav")
