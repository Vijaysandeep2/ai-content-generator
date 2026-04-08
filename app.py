import streamlit as st
import anthropic

st.set_page_config(page_title="AI Content Generator", page_icon="✨")

st.title("✨ AI Content Generator")
st.subheader("Generate professional content for your business instantly")

with st.form("content_form"):
    business_name = st.text_input("Business Name", placeholder="e.g. Sharma Electronics")
    description = st.text_area("Product/Service Description", placeholder="e.g. We sell affordable smartphones and accessories")
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
            client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
            prompt = f"Create a {content_type} for a business called '{business_name}'. About the business: {description}. Make it professional, engaging and ready to use."
            message = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            st.success("✅ Content Generated!")
            st.write(message.content[0].text)
            st.download_button("📋 Copy Content", message.content[0].text)
