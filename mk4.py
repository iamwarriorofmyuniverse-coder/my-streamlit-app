import streamlit as st
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="Course & Service Enquiry Form",
    page_icon="📋",
    layout="centered"
)

# 2. Header & Introduction
st.title("📋 Customer Enquiry Form")
st.caption("Please fill in the details below. Our team will get back to you within 24 hours.")
st.divider()

# 3. Use st.form to prevent page reload on every single keystroke
with st.form(key="enquiry_form"):
    
    # Section 1: Personal & Contact Information
    st.header("1. Contact Details")
    col1, col2 = st.columns(2)
    
    with col1:
        full_name = st.text_input(
            label="Full Name *",
            placeholder="e.g. C. Dharshan",
            help="Enter your complete legal name"
        )
        email = st.text_input(
            label="Email Address *",
            placeholder="e.g. dharshan@example.com",
            help="We will send the confirmation here"
        )
        
    with col2:
        phone = st.text_input(
            label="Phone Number *",
            placeholder="e.g. +91 9876543210",
            help="Include country code"
        )
        city = st.text_input(
            label="City / Location",
            placeholder="e.g. Coimbatore",
        )

    st.divider()

    # Section 2: Enquiry Details
    st.header("2. Enquiry Information")
    
    course_interest = st.selectbox(
        label="Domain / Service of Interest *",
        options=[
            "Artificial Intelligence & Machine Learning",
            "Data Science & Analytics",
            "Python Backend & FastAPI Development",
            "Full Stack Web Development",
            "Project Guidance & Mentorship",
            "Other / General Enquiry"
        ],
        index=0
    )

    preferred_mode = st.radio(
        label="Preferred Learning / Meeting Mode",
        options=["Online (Zoom / Meet)", "In-Person (Coimbatore Campus)", "Flexible / Hybrid"],
        horizontal=True
    )

    timing_preference = st.multiselect(
        label="Preferred Batch Timings",
        options=["Weekday Morning (7 AM - 9 AM)", "Weekday Evening (6 PM - 8 PM)", "Weekend Intensive (Sat & Sun)"],
        default=["Weekend Intensive (Sat & Sun)"]
    )

    budget_range = st.slider(
        label="Expected Budget / Investment (in ₹ INR)",
        min_value=5000,
        max_value=50000,
        value=15000,
        step=2500,
        help="Select your approximate budget range"
    )

    st.divider()

    # Section 3: Message & Additional Notes
    st.header("3. Detailed Message")
    message = st.text_area(
        label="Specific Questions or Requirements",
        placeholder="Tell us what you are looking to achieve or any specific topics you want covered...",
        height=120
    )

    # Section 4: Preferences & Callback
    urgent_callback = st.checkbox("⚡ Request an urgent callback within 2 hours")
    agree_terms = st.checkbox("I agree to be contacted via WhatsApp / Email regarding this enquiry *")

    st.divider()

    # Form Submit Button
    submitted = st.form_submit_button(
        label="📩 Submit Enquiry",
        use_container_width=True,
        type="primary"
    )

# 4. Form Submission & Validation Logic
if submitted:
    # Basic Validation
    if not full_name.strip():
        st.error("❌ Please enter your Full Name.")
    elif not email.strip() or "@" not in email:
        st.error("❌ Please enter a valid Email Address.")
    elif not phone.strip():
        st.error("❌ Please enter your Phone Number.")
    elif not agree_terms:
        st.warning("⚠️ Please check the box agreeing to be contacted.")
    else:
        # Success Receipt Card
        st.balloons()
        st.success(f"🎉 Thank you, **{full_name}**! Your enquiry has been received successfully.")
        
        st.subheader("📄 Enquiry Summary Receipt")
        st.info(f"""
        * **Enquiry Reference ID**: `ENQ-{datetime.now().strftime('%Y%m%d%H%M%S')}`
        * **Domain**: {course_interest}
        * **Contact**: {email} | {phone}
        * **Mode**: {preferred_mode}
        * **Timing**: {', '.join(timing_preference)}
        * **Budget**: ₹{budget_range:,}
        * **Urgent Callback**: {'Yes ⚡' if urgent_callback else 'Standard (24 hrs)'}
        """)

        st.caption("We have logged your query and an advisor will connect with you shortly.")