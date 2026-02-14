import streamlit as st
import random

# --- CONFIGURATION ---
# Replace with your actual image links
BG_URL = "https://tse4.mm.bing.net/th/id/OIP.fBmaH5Nc4Qtlu-CmvYhdvgHaHa?rs=1&pid=ImgDetMain&o=7&rm=3" 
OUR_PHOTO = "https://your-image-link-here.com" 

# Define your Questions and Answers here
QUIZ_DATA = [
    {"question": "Name the person who gave me your number (first name)?", "answer": "Pooja"},
    {"question": "Where was our first ever date?", "answer": "starbucks"},
    {"question": "What is my favorite color on you?", "answer": "red"}
]

# --- CUSTOM CSS ---
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{BG_URL}");
        background-size: cover;
    }}
    .header-box {{
        background-color: #FF4B4B;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
        border: 2px solid white;
    }}
    /* --- MODIFY QUESTION STYLE HERE --- */
    .valentine-question {{
        color: #C2185B; /* Change this for Color */
        font-size: 25px; /* Change this for Size */
        font-weight: bold;
        font-family: 'Comic Sans MS', cursive;
        margin-bottom: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 'start'
if 'quiz_index' not in st.session_state:
    st.session_state.quiz_index = 0
if 'no_pos' not in st.session_state:
    st.session_state.no_pos = 1

# --- APP LAYOUT ---

# 1. START SCREEN
if st.session_state.step == 'start':
    st.markdown('<div class="header-box">Are you ready to answer this question on this Valentine?</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.image("photo.jpg", use_container_width=True)
    if st.button("Yes, I am! ❤️", use_container_width=True):
        st.session_state.step = 'quiz'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 2. QUIZ SCREEN
elif st.session_state.step == 'quiz':
    st.markdown('<div class="header-box">A Little Love Quiz...</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.image("https://tse4.mm.bing.net/th/id/OIP.fBmaH5Nc4Qtlu-CmvYhdvgHaHa?rs=1&pid=ImgDetMain&o=7&rm=3", width=250)
    
    current_q = QUIZ_DATA[st.session_state.quiz_index]
    
    # Styled Question using the CSS class defined above
    st.markdown(f'<p class="valentine-question">Question {st.session_state.quiz_index + 1}</p>', unsafe_allow_html=True)
    st.write(f"### {current_q['question']}")
    
    # Text input for answer
    user_ans = st.text_input("Your Answer:", key=f"q_input_{st.session_state.quiz_index}").lower().strip()
    
    # LOGIC FIX: Check answer immediately to show Success and Next button
    if user_ans == current_q['answer']:
        st.success("Correct! You're so precious! ✨")
        st.write("*'You have a heart of gold.'*")
        
        if st.button("Next ➡️", use_container_width=True):
            if st.session_state.quiz_index < len(QUIZ_DATA) - 1:
                st.session_state.quiz_index += 1
                st.rerun()
            else:
                st.session_state.step = 'ask'
                st.rerun()
    
    # Previous button (always visible)
    if st.session_state.quiz_index > 0:
        if st.button("⬅️ Previous Question", use_container_width=True):
            st.session_state.quiz_index -= 1
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

# 3. THE BIG QUESTION
elif st.session_state.step == 'ask':
    st.markdown('<div class="header-box">The Final Question...</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('{OUR_PHOTO}'); 
             background-size: cover; background-position: center; padding: 70px; border-radius: 25px; 
             text-align: center; border: 5px solid white; color: white;">
            <h1 style="font-size: 35px; text-shadow: 2px 2px 8px #000000;">Will you be my Valentine?</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.write(" ")
    
    cols = st.columns(4)
    with cols[0]:
        if st.button("YES! 😍", use_container_width=True):
            st.session_state.step = 'success'
            st.rerun()
            
    no_col_index = st.session_state.no_pos
    with cols[no_col_index]:
        if st.button("No 🥺", use_container_width=True):
            st.session_state.no_pos = random.choice([1, 2, 3])
            st.toast("Too slow! You can't say no! 😉")
            st.rerun()

# 4. SUCCESS SCREEN
elif st.session_state.step == 'success':
    st.balloons()
    st.markdown('<div class="header-box">I Knew It! ❤️</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.image(OUR_PHOTO, use_container_width=True)
    st.write("# I knew it! You love me a lot! 😍")
    st.write("---")
    st.write("✨ *\"You make every day feel like Valentine's Day.\"*")
    st.write("✨ *\"I'm the luckiest person to have you in my life.\"*")
    st.markdown('</div>', unsafe_allow_html=True)
