import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="SkillPath AI - Surendra Yadav", page_icon="🚀")

# --- 2. API SETUP ---
# Secrets check
if "MY_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["MY_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Secrets mein API Key (MY_API_KEY) nahi mili!")
    st.stop()

# --- 3. SIDEBAR (Aapka Naam) ---
with st.sidebar:
    st.title("🎯 SkillPath AI")
    st.success("Built by **Surendra Yadav**") # <--- Aapka naam
    st.info("Personal Career Roadmap Generator")
    if st.button("Reset App 🔄"):
        st.rerun()

# --- 4. MAIN UI ---
st.title("🚀 SkillPath: AI Roadmap Generator")
user_goal = st.text_input("Aap kya banna chahte hain?", placeholder="e.g., Video Creator, Developer...")

# GENERATE BUTTON (Jo aapne manga tha)
if st.button("Generate My Roadmap ✨"):
    if user_goal:
        with st.spinner(f"Surendra's AI aapka '{user_goal}' roadmap taiyar kar raha hai..."):
            try:
                # AI Response
                prompt = f"Create a clear 3-step professional roadmap for {user_goal}. List 4 key skills for each step."
                response = model.generate_content(prompt)
                roadmap_text = response.text
                
                st.markdown(f"### 📍 Roadmap for: {user_goal}")
                st.divider()
                st.markdown(roadmap_text)
                
                # VIDEO LINK (Jo aapne manga tha)
                st.subheader("📺 Learning Resources")
                search_query = user_goal.replace(" ", "+")
                video_url = f"https://www.youtube.com/results?search_query={search_query}+full+course"
                st.info(f"👉 [Click here to watch {user_goal} Tutorials on YouTube]({video_url})")
                
                # DOWNLOAD BUTTON (Extra Feature)
                st.download_button(
                    label="Download Roadmap 📄",
                    data=roadmap_text,
                    file_name=f"{user_goal}_roadmap.txt",
                    mime="text/plain"
                )
                
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle apna goal likhein!")

# Footer
st.markdown("---")
st.caption("© 2026 SkillPath | Developed by Surendra Yadav")
