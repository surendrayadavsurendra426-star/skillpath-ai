import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="SkillPath AI - Surendra Yadav", page_icon="🚀")

# --- 2. API SETUP (Safe Connection) ---
if "MY_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["MY_API_KEY"])
        # Hamara naya model (Sabse latest)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Setup Error: {e}")
        st.stop()
else:
    st.error("Secrets mein API Key (MY_API_KEY) nahi mili!")
    st.stop()

# --- 3. SIDEBAR (Aapka Naam) ---
with st.sidebar:
    st.title("🎯 SkillPath AI")
    st.success("Built by **Surendra Yadav**") # Aapka naam yahan hai
    st.info("Personal AI Mentor")
    if st.button("Reset App 🔄"):
        st.rerun()

# --- 4. MAIN UI ---
st.title("🚀 SkillPath: AI Roadmap Generator")
user_goal = st.text_input("Aap kya banna chahte hain?", placeholder="e.g., Video Creator, Web Dev")

# GENERATE BUTTON (Jo aapne manga tha)
if st.button("Generate My Roadmap ✨"):
    if user_goal:
        with st.spinner(f"Surendra's AI '{user_goal}' ke liye best roadmap bana raha hai..."):
            try:
                # AI se roadmap mangwana
                prompt = f"Create a short and professional 3-step roadmap to become a {user_goal}. Provide title and 4 bullet points for each step."
                response = model.generate_content(prompt)
                roadmap_text = response.text
                
                # Title dikhana
                st.markdown(f"### 📍 Roadmap for: {user_goal}")
                st.divider()
                
                # Roadmap Text
                st.markdown(roadmap_text)
                
                # VIDEO LINK (Jo aapne manga tha)
                st.divider()
                st.subheader("📺 Learning Resources")
                search_query = user_goal.replace(" ", "+")
                video_url = f"https://www.youtube.com/results?search_query={search_query}+full+course"
                st.info(f"👉 [Click here to watch {user_goal} Tutorials on YouTube]({video_url})")
                
                # DOWNLOAD BUTTON
                st.download_button(
                    label="Download Roadmap 📄",
                    data=roadmap_text,
                    file_name=f"{user_goal}_roadmap.txt",
                    mime="text/plain"
                )
                
                st.balloons()
                
            except Exception as e:
                # Error handle karne ke liye naya tarika
                st.error("AI thoda busy hai ya model update ho raha hai.")
                st.info("Kripya ek baar 'Reboot' karein aur check karein API key valid hai ya nahi.")
    else:
        st.warning("Pehle apna goal likhein!")

# Footer
st.markdown("---")
st.caption("© 2026 SkillPath | Developed by Surendra Yadav")
