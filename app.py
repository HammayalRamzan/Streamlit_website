import streamlit as st

# Set page title and fav icon
st.set_page_config(page_title="AI Rehman", page_icon="🤖", layout="wide")

# Function to Set Background Image
def set_background(image_file):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url({image_file}) no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set Background Image
set_background("logo/logo.jpg")  # Yahan apni image ka path do

# Header
st.title("✨ Welcome to AI-Rehman ✨")
st.subheader("Hi, I am Abdul-Rehman. 👋")

# Dark/Light Mode Toggle
theme = st.sidebar.selectbox("Select Theme", ["Light Mode", "Dark Mode"])
if theme == "Dark Mode":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #2c2c2c;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True
    )

# Navigation
menu = ["Home", "About", "Services", "Contact", "E-Commerce", "Testimonials", "AI Chatbot"]
choice = st.sidebar.selectbox("Navigate", menu)

# Logo Image (Top Left Corner)
st.image("logo/logo.jpg", width=150)

if choice == "Home":
    st.write("### AI Rehman is a cutting-edge brand providing all stuff collections.")
    st.write("""🚀 Welcome to **AI-Rehman**, where Pakistani craftsmanship meets modern fashion.  
    We bring you exclusive, high-quality designs that celebrate elegance, culture,  
    and contemporary trends. Whether it's timeless traditional wear or chic modern  
    outfits, our collection is designed to make you stand out.  
""")
    st.button("Learn More")

elif choice == "About":
    st.write("## About Me:")
    st.write("- Experience the artistry of Pakistan’s finest designer fashion.")
    st.write("- AI-Rehman, A Visionary Pakistani Designer Brand")
    st.write("""Welcome to AI-Rehman Brand, where style meets craftsmanship. 
    As a passionate clothing brand owner, I am dedicated to creating high-quality, 
    fashionable attire that empowers individuals to express their unique style. 
    Join us on this journey to redefine fashion with elegance and innovation.""")

elif choice == "Services":
    st.write("## Services We Offer:")
    st.write("- 👗 Ladies' & Gents' Tailoring ✂️ – Perfectly stitched suits for every occasion.")
    st.write("- 🧵 Unstitched Fabric 👕 – Premium collection for your custom designs.")
    st.write("- 👖 Alterations & Fitting Services 🔧 – Tailored adjustments for the perfect fit.")
    st.write("- Personalized Style Consultation 💬 – Expert advice to enhance your wardrobe.")

elif choice == "Contact":
    st.write("## Contact Us:")
    st.write("📧 Email: alrehmanfashions@gmail.com")
    st.write("📍 Location: Lahore, Pakistan")
    st.write("📞 Phone: 03290505319")
    st.text_input("Your Name")
    st.text_area("Your Message")
    if st.button("Send Message"):
        st.success("Your message has been sent successfully!")

elif choice == "E-Commerce":
    st.write("## Shop Our Collection:")
    st.write("### Featured Products")
    st.write("1. **Traditional Sherwani** - PKR 10,000")
    st.write("2. **Chic Modern Dress** - PKR 7,500")
    st.write("3. **Formal Suit** - PKR 15,000")
    st.write("### Add to Cart Functionality Coming Soon!")  # Placeholder for future functionality

elif choice == "Testimonials":
    st.write("## Customer Reviews:")
    st.write("⭐️⭐️⭐️⭐️⭐️ - 'Amazing quality and craftsmanship!'")
    st.write("⭐️⭐️⭐️⭐️ - 'Loved my outfit from AI-Rehman!'")
    st.write("⭐️⭐️⭐️⭐️⭐️ - 'The best tailoring service in Lahore!'")

# elif choice == "AI Chatbot":
#     st.write("## AI Chatbot:")
#     st.write("How can I assist you today?")  # Placeholder for chatbot implementation

# Footer
st.write("---")
st.write("Thanks for visiting AI Rehman! ❣ ")
st.write("---")
st.write("© 2025 AI Rehman. All rights reserved.")
st.balloons()
