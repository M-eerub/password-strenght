import streamlit as st
import re

def Check_Password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Weak password, try a stronger one with 8+ characters.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Please use both uppercase and lowercase letters.")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Please include at least one special character (!@#$%^&*).")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Please add at least one number.")
    
    return score, feedback

st.title("Check Your Password Strength")
user_input = st.text_input("Add your password", type="password")

if st.button("Check"):
    if user_input:
        score, feedback = Check_Password(user_input)

        if score == 4:
            st.success("✅ Your password is strong!")
        elif score == 3:
            st.warning("⚠️ Your password is decent but can be stronger.")
        else:
            st.error("❌ Your password is weak!")
        
        for message in feedback:
            st.write(f"👉 {message}")
    else:
        st.error("Please enter a password to check.")
