import streamlit as st
import smtplib
from email.message import EmailMessage

# Set Page Configuration
st.set_page_config(page_title="AI Rehman - Clothing Brand", page_icon="👕", layout="wide")

# --- DARK/LIGHT MODE TOGGLE ---
theme = st.sidebar.radio("🌗 Choose Theme:", ["Light Mode", "Dark Mode"])
if theme == "Dark Mode":
    st.markdown(
        """
        <style>
        body {
            background-color: #2c2c2c;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True
    )

# --- HEADER ---
st.title("✨ Welcome to AI-Rehman Fashion ✨")
st.subheader("👋 Hi, I am Abdul-Rehman, the creative mind behind this brand.")

# --- NAVIGATION MENU ---
menu = ["Home", "About Us", "Services", "Contact", "Shop", "Testimonials"]
choice = st.sidebar.selectbox("📍 Navigate", menu)

# --- HOME SECTION ---
if choice == "Home":
    st.image("./logo.jpg")
    st.write("### Discover the finest collection of Pakistani fashion, where tradition meets modern elegance.")
    st.write("🚀 We bring you high-quality, exclusive designs tailored for every occasion.")
    st.button("🔍 Explore More")

# --- ABOUT US SECTION ---
elif choice == "About Us":
    st.write("## 🏆 About AI-Rehman Fashion")
    st.write("Welcome to AI-Rehman, where we redefine fashion with elegance and innovation.")
    st.write("- 🎨 Inspired by **Pakistani traditions** with a modern touch.")
    st.write("- 🧵 **Premium quality** fabric and expert craftsmanship.")
    st.write("- 🏅 Trusted by customers nationwide.")
    st.success("Our mission is to deliver **luxury fashion** that makes you stand out!")

# --- SERVICES SECTION ---
elif choice == "Services":
    st.write("## 🛠️ Our Services")
    st.write("### 👗 Tailoring & Custom Stitching")
    st.write("✅ Ladies' & Gents' Suits Tailoring")
    st.write("✅ Unstitched Fabric for Custom Designs")
    st.write("✅ Alterations & Fitting Adjustments")
    st.write("✅ Personalized Style Consultation")

# --- CONTACT SECTION ---
elif choice == "Contact":
    st.write("## 📞 Contact Us")
    st.write("📍 **Location:** Lahore, Pakistan")
    st.write("📧 **Email:** alrehmanfashions@gmail.com")
    st.write("📞 **Phone:** 03290505319")

    st.title("📩 Contact Form")

# Contact Form
    name = st.text_input("Your Name")
    message = st.text_area("Your Message")
    if st.button("📩 Send Message"):
        st.success(f"Thank you, {name}! Your message has been sent successfully.")
# --- SHOP (E-COMMERCE) SECTION ---
elif choice == "Shop":
    st.write("## 🛍️ Shop Our Collection")
    st.write("### 🏷️ Featured Products:")
    st.write("1️⃣ **Traditional Sherwani** - PKR 10,000")
    st.write("2️⃣ **Chic Modern Dress** - PKR 7,500")
    st.write("3️⃣ **Formal Suit** - PKR 15,000")
    st.warning("🛒 Add-to-cart feature coming soon!")

# --- TESTIMONIALS SECTION ---
elif choice == "Testimonials":
    st.write("## ⭐ Customer Reviews")
    st.write("🌟🌟🌟🌟🌟 - 'Amazing quality and craftsmanship!'")
    st.write("🌟🌟🌟🌟 - 'Loved my outfit from AI-Rehman!'")
    st.write("🌟🌟🌟🌟🌟 - 'Best tailoring service in Lahore!'")
    
# --- FOOTER ---
st.write("---")
st.write("👕 Thank you for visiting **AI Rehman Fashion**! We appreciate your support. ❤️")
st.write("© 2025 AI Rehman. All rights reserved.")
st.balloons()
