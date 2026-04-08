import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

st.set_page_config(page_title="AI Content Generator", page_icon="✨")
st.title("✨ AI Content Generator")
st.subheader("Generate professional content for your business instantly")

with st.form("content_form"):
    business_name = st.text_input("Business Name", placeholder="e.g. Sharma Electronics")
    description = st.text_area("Product/Service Description", placeholder="e.g. We sell affordable smartphones")
    content_type = st.selectbox("Content Type", [
        "Social Media Post",
        "Product Description",
        "Marketing Email"
    ])
    submitted = st.form_submit_button("🚀 Generate Content")

if submitted:
    if not business_name or not description:
        st.error("Please fill in all fields!")
    else:
        with st.spinner("Generating your content..."):
            prompt = f"Create a {content_type} for '{business_name}'. About: {description}. Make it professional and ready to use."
            response = model.generate_content(prompt)
            st.success("✅ Content Generated!")
            st.write(response.text)
            st.download_button("📋 Download Content", response.text)
