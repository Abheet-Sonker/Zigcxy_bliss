import streamlit as st
import urllib.parse

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(page_title="Zigcxy Bliss", layout="centered")

st.title("🕯️ Zigcxy Bliss - Customize Your Candle")
st.write("Create your perfect aesthetic candle ✨")

# ==========================================
# OPTIONS
# ==========================================

glass_options = ["Jar", "Cylindrical", "Wine Glass", "Bubble Candle"]
bubble_sizes = ["3x3", "2x2"]

look_options = ["Sea Theme", "Flower Theme"]
type_options = ["Water Candle", "Crystal Gel Candle", "Full Wax Shape Candle"]

color_options = ["Red", "Blue", "Green", "Orange", "Brown"]
fragrance_options = ["Sea Salt", "French Lilac", "Lavender"]

# ==========================================
# IMAGE PATHS
# ==========================================

images = {
    "Jar": "images/Jar.jpeg",
    "Cylindrical": "images/cylinder.jpeg",
    "Wine Glass": "images/Wine_glass.jpeg",
    "Bubble Candle": "images/Bubble.jpeg",
    "Sea Theme": "images/Sea_view.jpeg",
    "Flower Theme": "images/Flower_theme.jpeg",
}

# ==========================================
# SELECTIONS
# ==========================================

glass = st.selectbox("Choose Candle Type", glass_options)
st.image(images[glass], width=180)

if glass == "Bubble Candle":
    bubble_size = st.selectbox("Choose Bubble Size", bubble_sizes)
    color = st.selectbox("Choose Color", color_options)
    fragrance = st.selectbox("Choose Fragrance", fragrance_options)

    look = "N/A"
    ctype = "Bubble Candle"

else:
    look = st.selectbox("Choose Look", look_options)
    st.image(images[look], width=180)

    ctype = st.selectbox("Choose Candle Type", type_options)
    color = st.selectbox("Choose Color", color_options)
    fragrance = st.selectbox("Choose Fragrance", fragrance_options)

    bubble_size = "N/A"

# ==========================================
# PRICE
# ==========================================

price = 0

if glass == "Cylindrical":
    price = 325
elif glass == "Jar" and ctype == "Water Candle":
    price = 225
elif glass == "Wine Glass":
    price = 425
elif glass == "Jar" and ctype == "Full Wax Shape Candle":
    price = 199
elif glass == "Bubble Candle":
    price = 149 if bubble_size == "3x3" else 49

st.subheader(f"💰 Price: ₹{price}")

# ==========================================
# CUSTOMER DETAILS
# ==========================================

st.subheader("📋 Customer Details")

name = st.text_input("Name")
email = st.text_input("Email")
mobile = st.text_input("Mobile Number")
hall = st.text_input("Hall No")
room = st.text_input("Hostel Room No")

# ==========================================
# WHATSAPP BUTTON
# ==========================================

YOUR_NUMBER = "916394996857"   # 👉 Replace with your WhatsApp number

if st.button("Place Order via WhatsApp"):

    if not (name and mobile and email):
        st.warning("⚠️ Please fill required details (Name, Email & Mobile)")

    else:
        message = f"""🕯️ *Zigcxy Bliss Order*

👤 Name: {name}
📧 Email: {email}
📱 Mobile: {mobile}
🏠 Hall: {hall}
🚪 Room: {room}

🕯️ Type: {glass}
📦 Bubble Size: {bubble_size}
🎨 Look: {look}
🧾 Category: {ctype}
🎨 Color: {color}
🌸 Fragrance: {fragrance}

💰 Price: ₹{price}
"""

        encoded_message = urllib.parse.quote(message)
        whatsapp_url = f"https://wa.me/{YOUR_NUMBER}?text={encoded_message}"

        st.link_button("📲 Confirm Order on WhatsApp", whatsapp_url)

        st.success("✅ Click button above to send your order")
