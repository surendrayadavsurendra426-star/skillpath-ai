import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="SkillPath AI - Surendra Yadav", page_icon="🚀")

# --- 2. API SETUP ---
if "MY_API_KEY" not in st.secrets:
    st.error("❌ Error: API Key 'Secrets' mein nahi mili! Dashboard check karein.")
    st.stop()

# API Configuration
genai.configure(api_key=st.secrets["MY_API_KEY"])

# --- 3. SIDEBAR (Aapka Naam) ---
with st.sidebar:
    st.title("🎯 SkillPath AI")
    st.success("Built by **Surendra Yadav**")
    st.info("System: Auto-Repair Mode")
    if st.button("Reset App 🔄"):
        st.rerun()

# --- 4. MAIN UI ---
st.title("🚀 SkillPath: Personalized Roadmap")
user_goal = st.text_input("Aap kya banna chahte hain?", placeholder="e.g., Video Creator")

# GENERATE BUTTON
if st.button("Generate My Roadmap ✨"):
    if user_goal:
        with st.spinner(f"Surendra's AI rasta dhoond raha hai..."):
            
            # YAHAN MULTIPLE MODELS TRY KARENGE (Error se bachne ke liye)
            models_to_try = ['gemini-1.5-flash', 'gemini-1.5-flash-latest', 'gemini-pro']
            success = False
            
            for model_name in models_to_try:
                try:
                    model = genai.GenerativeModel(model_name)
                    response = model.generate_content(f"Create a short 3-step roadmap to become {user_goal}")
                    
                    # Agar chal gaya toh display karein
                    st.markdown(f"### 📍 Roadmap for: {user_goal}")
                    st.divider()
                    st.markdown(response.text)
                    
                    # YouTube Video Link
                    st.subheader("📺 Learning Resources")
                    q = user_goal.replace(" ", "+")
                    st.info(f"👉 [Click here for {user_goal} Tutorials on YouTube](https://www.youtube.com/results?search_query={q}+course)")
                    
                    # Download Button
                    st.download_button("Download Roadmap 📄", response.text, file_name="roadmap.txt")
                    st.balloons()
                    
                    success = True
                    break # Agar ek model chal gaya toh loop rok do
                except Exception:
                    continue # Agar 404 aaya toh agla model try karein
            
            if not success:
                st.error("❌ AI Response Fail: Sabhi models 404 error de rahe hain.")
                st.warning("Ilaaj: Google AI Studio se 'Nayi API Key' banayein aur Secrets mein update karein.")
    else:
        st.warning("Pehle apna goal likhein!")

st.caption("© 2026 Developed by Surendra Yadav")
