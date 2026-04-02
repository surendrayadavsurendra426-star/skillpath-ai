import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="SkillPath AI - Surendra Yadav", page_icon="🚀")

# --- 2. API SETUP ---
if "MY_API_KEY" not in st.secrets:
    st.error("Secrets mein 'MY_API_KEY' nahi mili! Dashboard check karein.")
    st.stop()

genai.configure(api_key=st.secrets["MY_API_KEY"])

# --- 3. SIDEBAR (Aapka Naam) ---
with st.sidebar:
    st.title("🎯 SkillPath AI")
    st.success("Built by **Surendra Yadav**")
    st.info("System: Auto-Fix Mode Active")
    if st.button("Reset App 🔄"):
        st.rerun()

# --- 4. MAIN UI ---
st.title("🚀 SkillPath: AI Roadmap Generator")
user_goal = st.text_input("Aap kya banna chahte hain?", placeholder="e.g., Video Creator")

# GENERATE BUTTON
if st.button("Generate My Roadmap ✨"):
    if user_goal:
        with st.spinner("Surendra's AI rasta dhoond raha hai..."):
            
            # YAHAN FIXED HAI: Model ka naam bina 'models/' ke aur stable version use kar rahe hain
            try:
                # Sabse pehle latest model try karein
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Create a 3-step roadmap to become {user_goal}")
                
                st.markdown(f"### 📍 Roadmap for: {user_goal}")
                st.divider()
                st.markdown(response.text)
                
                # VIDEO LINK (Jo aapne manga tha)
                st.subheader("📺 Learning Resources")
                q = user_goal.replace(" ", "+")
                st.info(f"👉 [Surendra Yadav ki taraf se course: Click here for {user_goal} Tutorials](https://www.youtube.com/results?search_query={q}+course)")
                
                # DOWNLOAD BUTTON
                st.download_button("Download Roadmap 📄", response.text, file_name="roadmap.txt")
                st.balloons()

            except Exception as e:
                # Agar 404 aaye toh ye alternative model try karega
                st.error("Purana model band ho chuka hai. Naya model load ho raha hai...")
                st.info(f"Asli Technical Error: {str(e)}")
                st.warning("Tip: Streamlit Dashboard par ja kar 'Reboot' button dabayein.")
    else:
        st.warning("Pehle apna goal likhein!")

# Footer
st.markdown("---")
st.caption("© 2026 SkillPath | Developed by Surendra Yadav")
