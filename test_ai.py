import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="SkillPath AI - Surendra Yadav", page_icon="🚀")

# --- 2. API SETUP ---
if "MY_API_KEY" not in st.secrets:
    st.error("API Key missing! Secrets mein add karein.")
    st.stop()

genai.configure(api_key=st.secrets["MY_API_KEY"])

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("🎯 SkillPath AI")
    st.success("Built by **Surendra Yadav**")
    st.info("System: Model Auto-Detector")

# --- 4. MAIN UI ---
st.title("🚀 SkillPath: Personalized Roadmap")
user_goal = st.text_input("Aap kya banna chahte hain?", placeholder="e.g., Video Creator")

if st.button("Generate My Roadmap ✨"):
    if user_goal:
        with st.spinner("AI Models check ho rahe hain..."):
            try:
                # Sabse pehle "models/gemini-2.5-flash" try karein
                model = genai.GenerativeModel("models/gemini-2.5-flash")
                response = model.generate_content(f"Create a 3-step roadmap to become {user_goal}")
                
                st.markdown(f"### 📍 Roadmap for: {user_goal}")
                st.markdown(response.text)
                
                # VIDEO LINK
                st.divider()
                q = user_goal.replace(" ", "+")
                st.info(f"👉 [Watch {user_goal} Tutorials on YouTube](https://www.youtube.com/results?search_query={q}+course)")
                st.balloons()
                
            except Exception as e:
                # Agar 404 aaye, toh list dikhayega ki kaunsa model available hai
                st.error("Naya Model Connect nahi hua. Available models ki list check karein:")
                available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                st.write(available_models)
                st.info("Upar di gayi list mein se pehla model use karne ki koshish karein.")
    else:
        st.warning("Pehle kuch likhiye!")

st.caption("© 2026 Developed by Surendra Yadav")
