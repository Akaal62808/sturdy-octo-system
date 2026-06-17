import streamlit as st
import time

st.set_page_config(page_title="For Dressing queen👑", layout="centered")

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #2c003e, #4b006e);
    color: gold;
    text-align: center;
}
.title {
    font-size: 45px;
    font-weight: bold;
    text-shadow: 0 0 20px gold;
    margin-top: 40px;
}
.message {
    font-size: 22px;
    margin-top: 30px;
    background: rgba(255, 215, 0, 0.08);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 0 20px rgba(255, 215, 0, 0.4);
}
.stButton>button {
    background-color: gold;
    color: purple;
    border-radius: 30px;
    font-size: 18px;
    padding: 10px 25px;
    box-shadow: 0 0 15px gold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Session Setup ----------------
if "page" not in st.session_state:
    st.session_state.page = 1

if "animation_done" not in st.session_state:
    st.session_state.animation_done = False


# ---------------- Typewriter ----------------
def typewriter(text):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(
            '<div class="message">' + typed + '</div>',
            unsafe_allow_html=True
        )
        time.sleep(0.02)


# ================= PAGE 1 =================
if st.session_state.page == 1:

    st.markdown('<div class="title"> Enter Password🔐</div>', unsafe_allow_html=True)

    password = st.text_input("Enter Password", type="password")

    if st.button("Open🔓"):

        if password == "Guri@780":
            st.session_state.page = 2
            st.session_state.animation_done = False
            st.rerun()
        else:
            st.error("Wrong Password ❌ Try Again")
            st.rerun()


# ================= PAGE 2 (WELCOME) =================
elif st.session_state.page == 2:

    st.markdown('<div class="title">Welcome 💐</div>', unsafe_allow_html=True)

    welcome_text = """Welcome to Parveen ✨ 💜  

Good morning dear dressing queen 🌸have a nice day..."""

    if not st.session_state.animation_done:
        typewriter(welcome_text)
        st.session_state.animation_done = True
    else:
        st.markdown('<div class="message">' + welcome_text + '</div>', unsafe_allow_html=True)

    if st.button("Next ⏭️"):
        st.session_state.page = 3
        st.session_state.animation_done = False
        st.rerun()


# ================= PAGE 3 (THANK YOU) =================
elif st.session_state.page == 3:

    st.markdown('<div class="title">Thank You Parveen 😊</div>', unsafe_allow_html=True)

    thank_text = """Main dress suggestion lai puchya si,
par tusi sirf suggestion nahi
meri confusion vi door kar ditti..

Your choice and sense of style are genuinely impressive."""

    if not st.session_state.animation_done:
        typewriter(thank_text)
        st.session_state.animation_done = True
    else:
        st.markdown('<div class="message">' + thank_text + '</div>', unsafe_allow_html=True)

    if st.button("Next Page ⏭️"):
        st.session_state.page = 4
        st.session_state.animation_done = False
        st.rerun()


# ================= PAGE 4 (SORRY) =================
elif st.session_state.page == 4:

    st.markdown('<div class="title">Sorry to parveen 💜</div>', unsafe_allow_html=True)

    sorry_text = """Mein thonu morning  vich hi disturb kar lag penda haan.... Taa Sorry

But dresses di suggestion ta ik queen toh hi leni bandi aw.... 
 
 Next time thonu disturb kar sakda fashion design layi...
 ."""

    if not st.session_state.animation_done:
        typewriter(sorry_text)
        st.session_state.animation_done = True
    else:
        st.markdown('<div class="message">' + sorry_text + '</div>', unsafe_allow_html=True)

    if st.button("Next ⏭️"):
        st.session_state.page = 5
        st.session_state.animation_done = False
        st.rerun()


# ================= PAGE 5 (MISS YOU) =================
elif st.session_state.page == 5:

    st.markdown('<div class="title"> Ones again 💫</div>', unsafe_allow_html=True)

    miss_text = """Thanks again, Dressing Queen 👑

Next time jadon fashion emergency aayi,
mainu pata aa kis expert kol jana aa. 😄"""

    if not st.session_state.animation_done:
        typewriter(miss_text)
        st.session_state.animation_done = True
