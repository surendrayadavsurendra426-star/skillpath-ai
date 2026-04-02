import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="SkillPath AI - Surendra Yadav", page_icon="🚀")

# --- 2. API SETUP ---
if "MY_API_KEY" not in st.secrets:
    st.error("Secrets mein 'MY_API_KEY' add karein!")
    st.stop()

genai.configure(api_key=st.secrets["MY_API_KEY"])

# --- 3. SIDEBAR (Updated Name) ---
with st.sidebar:
    st.title("🎯 SkillPath AI")
    st.success("Built by **Surendra Yadav**")
    st.info("AI Roadmap Engine v4.0")
    if st.button("Reset App 🔄"):
        st.rerun()

# --- 4. MAIN UI ---
st.title("🚀 SkillPath: AI Roadmap Generator")
user_goal = st.text_input("Aap kya banna chahte hain?", placeholder="e.g., Video Creator")

# GENERATE BUTTON
if st.button("Generate My Roadmap ✨"):
    if user_goal:
        with st.spinner("Surendra's AI rasta dhoond raha hai..."):
            
            # YAHAN ERROR FIX KIYA HAI: Multiple models try karenge
            success = False
            models_to_try = ['gemini-1.5-flash', 'gemini-pro', 'gemini-1.0-pro']
            
            for model_name in models_to_try:
                try:
                    model = genai.GenerativeModel(model_name)
                    response = model.generate_content(f"Give a 3-step roadmap to become {user_goal}. Be concise.")
                    
                    # Agar response mil gaya toh display karein
                    st.markdown(f"### 📍 Roadmap for: {user_goal}")
                    st.divider()
                    st.markdown(response.text)
                    
                    # YouTube Link
                    st.subheader("📺 Learning Resources")
                    q = user_goal.replace(" ", "+")
                    st.info(f"👉 [Click here for {user_goal} Tutorials on YouTube](https://www.youtube.com/results?search_query={q}+course)")
                    
                    # Download Button
                    st.download_button("Download Roadmap 📄", response.text, file_name="roadmap.txt")
                    st.balloons()
                    
                    success = True
                    break # Loop se bahar nikal jayein agar chal gaya toh
                except:
                    continue # Dusra model try karein
            
            if not success:
                st.error("Galti: AI connect nahi ho pa raha. Kripya naya API Key generate karein Google AI Studio se.")
    else:
        st.warning("Pehle apna goal likhein!")

st.caption("© 2026 SkillPath | Developed by Surendra Yadav")
