import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('fake_account_detector.pkl')
st.title("Fake Instagram Account Detection")
# Input fields for the features
profile_pic = st.number_input(" 📸 Profile Pic (1 for Yes, 0 for No)", 0, 1)
username_length = st.number_input(" 🔠 Length of Username", 0.0)
fullname_words = st.number_input(" 📝 Number of Words in Fullname", 0)
fullname_length = st.number_input(" 📏 Length of Fullname", 0)
name_equals_username = st.number_input(" 🆔 Name Equals Username (1 for Yes, 0 for No)", 0, 1)
description_length = st.number_input(" 🖋️ Description Length", 0)
external_url = st.number_input(" 🔗 External URL (1 for Yes, 0 for No)", 0, 1)
private = st.number_input(" 🔒 Private Account (1 for Yes, 0 for No)", 0, 1)
posts = st.number_input(" 📸 Number of Posts", 0)
followers = st.number_input(" 👥 Number of Followers", 0)
follows = st.number_input(" 👣 Number of Follows", 0)

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'profile pic': [profile_pic],
    'nums/length username': [username_length],
    'fullname words': [fullname_words],
    'nums/length fullname': [fullname_length],
    'name==username': [name_equals_username],
    'description length': [description_length],
    'external URL': [external_url],
    'private': [private],
    '#posts': [posts],
    '#followers': [followers],
    '#follows': [follows]
})

# Button to make prediction
if st.button(" 🚦 Detect Fake Account"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("🚨  This account is likely FAKE.")
    else:
        st.success(" ✅ This account is likely REAL.")