import re
import streamlit as st

st.set_page_config(page_title="Password Strength Meter By UmmeFizza", page_icon="🔐", layout="centered")
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto; }
    .stButton button {width: 50%; background-color black; color: white; font-size: 20px; }
    .stButton button:hover { background-color: blue; }
</style>
""", unsafe_allow_html=True)

st.title("🔐 Password Strength Generator")
st.write("Enter your password below")

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 
    else:
        feedback.append("Password should be atleast 8 character long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append(" Password should inculde both uppar case (A-Z) and lowercase (a-z) letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should include atleast one number (0-9).")
    
    if re.search(r"[!@#$%*&^]", password):
        score += 1
    else:
        feedback.append("Include atleast one special character (!@#$%*&^).")

    if score == 4:
        st.success("<<Strong Password - Your password is strong and secure.")
    elif score == 3:
        st.info("<<Moderate Password - Consider improving security by adding more feature")
    else:
        st.error("<<Week Password - Follow the suggestion below to strength it.")

    if feedback:
        with st.expander("Improve Your Password"):
           for item in feedback:
                  st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password")

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password first!")