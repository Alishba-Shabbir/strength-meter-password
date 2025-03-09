import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    messages = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        messages.append("❌ **Password should be at least 8 characters long.**")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ **Include both uppercase and lowercase letters.**")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("❌ **Add at least one number (0-9).**")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        messages.append("❌ **Include at least one special character (!@#$%^&*).**")

    # Strength Rating
    strength_levels = {
        4: ("✅ **Strong Password!** 🔥", "green"),
        3: ("⚠️ **Moderate Password - Consider adding more security features.**", "brown"),
        2: ("❌ **Weak Password - Needs Improvement.**", "red"),
        1: ("❌ **Very Weak Password!**", "darkred"),
        0: ("❌ **Extremely Weak Password!**", "black"),
    }

    strength_message, strength_color = strength_levels.get(score, strength_levels[0])

    return messages, strength_message, strength_color, score

# Streamlit UI Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
        }
        .password-box {
            background: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            width: 60%;
            margin: auto;
            text-align: center;
        }
        .result-box {
            padding: 15px;
            border-radius: 10px;
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit App
st.title("🔒 Password Strength Checker")

# Password input field
password = st.text_input("Enter your password:", type="password")

# Checking password strength
if password:
    messages, strength_message, strength_color, score = check_password_strength(password)

    # Progress Bar Indicator
    st.progress(score / 4)

    # Display Strength Message
    st.markdown(
        f"<div class='result-box' style='background-color:{strength_color}; color:white; padding:10px; text-align:center; border-radius:10px;'>"
        f"{strength_message}</div>",
        unsafe_allow_html=True,
    )

    # Show improvement messages
    for message in messages:
        st.markdown(f"<p style='color:red; font-size:16px;'>{message}</p>", unsafe_allow_html=True)
