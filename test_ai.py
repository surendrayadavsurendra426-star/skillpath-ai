import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SkillPath - Your AI Mentor",
    page_icon="🚀",
    layout="wide"
)

# --- 2. API KEY LOADING (From Streamlit Secrets) ---
try:
    # Maan ke chal raha hoon aapne Secrets mein 'MY_API_KEY' naam rakha hai
    api_key = st.secrets["MY_API_KEY"]
except KeyError:
    st.error("Error: API Key nahi mili. Streamlit Secrets mein 'MY_API_KEY' add karein.")
    st.stop()

# --- 3. SIDEBAR & PROGRESS TRACKING ---
with st.sidebar:
    st.title("🎯 SkillPath v2.0")
    st.write("Aapka personal career pathfinder.")
    st.markdown("---")
    
    if 'progress' not in st.session_state:
        st.session_state.progress = 0
    
    st.subheader("Your Progress")
    st.progress(st.session_state.progress / 100)
    st.write(f"Completed: **{st.session_state.progress}%**")
    
    if st.button("Reset Journey 🔄"):
        st.session_state.progress = 0
        st.rerun()

    st.markdown("---")
    st.markdown("### About Developer")
    st.info("Built by Surendra with ❤️ using Streamlit & AI.")

# --- 4. MAIN INTERFACE ---
st.title("🚀 Unlock Your Potential with SkillPath")
st.subheader("Bataiye aaj aap kya seekhna chahte hain?")

# Sample buttons for quick start
col_a, col_b, col_c = st.columns(3)
with col_a:
    if st.button("🌐 Web Development"):
        st.session_state.goal = "Web Development"
with col_b:
    if st.button("📊 Data Science"):
        st.session_state.goal = "Data Science"
with col_c:
    if st.button("📱 App Development"):
        st.session_state.goal = "App Development"

# Input Box
user_input = st.text_input("Apna career goal yahan likhein:", 
                          value=st.session_state.get('goal', ''),
                          placeholder="Example: Python Backend Developer...")

if user_input:
    st.divider()
    st.markdown(f"### 📍 Personalized Roadmap for: **{user_input}**")
    
    # NOTE: Yahan main dummy data de raha hoon. 
    # Aapka AI logic (OpenAI/Gemini) yahan integration karega.
    steps = [
        {"title": "Foundations", "desc": "Syntax, Logic, and Basic Environment Setup.", "link": "https://www.google.com/search?q=basics+of+" + user_input},
        {"title": "Intermediate Tools", "desc": "Frameworks, Libraries, and API Integration.", "link": "https://www.google.com/search?q=intermediate+" + user_input},
        {"title": "Advanced Projects", "desc": "Building real-world applications and deployment.", "link": "https://www.google.com/search?q=advanced+projects+" + user_input}
    ]

    for i, s in enumerate(steps):
        with st.expander(f"Step {i+1}: {s['title']}"):
            st.write(s['desc'])
            
            c1, c2 = st.columns([1, 1])
            with c1:
                st.link_button("Learn Now 🔗", s['link'])
            with c2:
                if st.checkbox(f"Done with Step {i+1}", key=f"check_{i}"):
                    # Update progress
                    new_val = int(((i + 1) / len(steps)) * 100)
                    if new_val > st.session_state.progress:
                        st.session_state.progress = new_val
                        if new_val == 100:
                            st.balloons()
                            st.success("Mubarak ho! Aapne roadmap complete kar liya!")
                        st.rerun()

# --- 5. FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.caption("© 2024 SkillPath AI | Made with Streamlit Cloud")
