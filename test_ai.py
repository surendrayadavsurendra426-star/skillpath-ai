import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="SkillPath AI - Surendra Yadav", page_icon="🚀")

# --- 2. API SETUP (With Better Error Handling) ---
if "MY_API_KEY" not in st.secrets:
    st.error("Secrets mein API Key nahi mili! Settings > Secrets check karein.")
    st.stop()

# API Configuration
genai.configure(api_key=st.secrets["MY_API_KEY"])

# --- 3. SIDEBAR ---
with st.sidebar:
    st.success("Built by **Surendra Yadav**")
    st.info("Version: 3.0 (Fixed)")
    if st.button("Reset App 🔄"):
        st.rerun()

# --- 4. MAIN UI ---
st.title("🚀 SkillPath: Personalized Roadmap")
user_goal = st.text_input("Aap kya banna chahte hain?", placeholder="e.g., Video Creator")

if st.button("Generate My Roadmap ✨") and user_goal:
    with st.spinner("AI Response ka intezaar karein..."):
        try:
            # TRYING MULTIPLE MODELS (Agar ek fail ho toh dusra chale)
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Create a 3-step roadmap for {user_goal}")
            except:
                model = genai.GenerativeModel('gemini-pro') # Back up model
                response = model.generate_content(f"Create a 3-step roadmap for {user_goal}")
            
            st.subheader(f"📍 Roadmap for: {user_goal}")
            st.markdown(response.text)
            
            # YouTube Link
            search_url = f"https://www.youtube.com/results?search_query={user_goal.replace(' ', '+')}+course"
            st.info(f"👉 [Surendra ki taraf se free course: Click here for {user_goal} tutorials]({search_url})")
            
            # Download Button
            st.download_button("Download Roadmap 📄", response.text, file_name=f"{user_goal}_roadmap.txt")
            st.balloons()
            
        except Exception as e:
            # YE LINE ASLI ERROR DIKHAYEGI
            st.error(f"Error Message: {str(e)}")
            st.warning("Tips: 1. Nayi API Key use karein. 2. requirements.txt check karein. 3. App Reboot karein.")

# Footer
st.markdown("---")
st.caption("© 2026 SkillPath | Developed by Surendra Yadav")
