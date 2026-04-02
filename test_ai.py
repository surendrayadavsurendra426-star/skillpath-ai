import streamlit as st
import google.generativeai as genai

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="SkillPath AI - Surendra Yadav",
    page_icon="🚀",
    layout="wide"
)

# --- 2. API KEY SETUP ---
if "MY_API_KEY" not in st.secrets:
    st.error("Secrets mein 'MY_API_KEY' missing hai!")
    st.stop()

genai.configure(api_key=st.secrets["MY_API_KEY"])

# YAHAN CHANGE KIYA HAI: 'gemini-1.5-flash' use kar rahe hain jo fast aur updated hai
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("🎯 SkillPath AI")
    st.markdown("---")
    st.markdown("### 👨‍💻 Developer")
    st.success("Built by **Surendra Yadav**") 
    st.info("Aapka personal AI career guide.")
    if st.button("Reset App 🔄"):
        st.rerun()

# --- 4. MAIN INTERFACE ---
st.title("🚀 SkillPath: Personalized Roadmap")
user_goal = st.text_input("Aap kya banna chahte hain?", placeholder="e.g., Video Creator, Cooking Expert...")

# GENERATE BUTTON
generate_btn = st.button("Generate My Roadmap ✨")

if generate_btn and user_goal:
    with st.spinner(f"Surendra's AI aapka '{user_goal}' roadmap taiyar kar raha hai..."):
        try:
            # AI Prompt
            prompt = f"Create a detailed 3-step roadmap to become a {user_goal}. For each step, give a title and a list of key topics to learn."
            response = model.generate_content(prompt)
            roadmap_content = response.text
            
            st.markdown(f"### 📍 Roadmap for: **{user_goal}**")
            st.divider()
            
            # Display Roadmap
            st.markdown(roadmap_content)
            
            # YouTube Link
            st.subheader("📺 Learning Resources")
            search_query = user_goal.replace(" ", "+")
            st.info(f"👉 [Surendra ki taraf se free course: Click here for {user_goal} tutorials on YouTube](https://www.youtube.com/results?search_query={search_query}+course)")

            # --- 5. DOWNLOAD PDF/TEXT ---
            st.divider()
            download_text = f"SkillPath Roadmap for {user_goal}\nDeveloped by Surendra Yadav\n\n{roadmap_content}"
            st.download_button(
                label="Download Roadmap 📄",
                data=download_text,
                file_name=f"{user_goal}_roadmap.txt",
                mime="text/plain"
            )
            
            st.balloons()
            
        except Exception as e:
            st.error(f"AI Response Error: {e}")
elif generate_btn and not user_goal:
    st.warning("Kripya pehle apna goal likhein!")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.caption("© 2026 SkillPath | Developed by Surendra Yadav")
