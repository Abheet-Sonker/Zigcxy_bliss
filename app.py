import streamlit as st
import urllib.parse

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Zigcxy Bliss",
    page_icon="🕯️",
    layout="centered"
)

st.title("🕯️ Zigcxy Bliss")
st.subheader("Customize & Order Your Handmade Products")

# ==========================================
# PRODUCT SELECTION
# ==========================================

product = st.selectbox(
    "Choose Product",
    [
        "Mess Glow Candle",
        "Terracotta Glow Candle",
        "Wax Sachet"
    ]
)

# ==========================================
# OPTIONS
# ==========================================

colors = [
    "White",
    "Red",
    "Blue",
    "Green",
    "Pink",
    "Yellow",
    "Orange"
]

fragrances = [
    "Amber",
    "Cinnamon",
    "Coffee",
    "Lavender",
    "Vanilla",
]

sachet_shapes = [
    "Rectangular",
    "Rhombus",
    "Oval"
]

# ==========================================
# PRODUCT CUSTOMIZATION
# ==========================================

if product == "Mess Glow Candle":

    st.image("images/Mess Glow.png", width=250)

    color = st.selectbox("Choose Jar Color", colors)
    fragrance = st.selectbox("Choose Fragrance", fragrances)

    price = 299

elif product == "Terracotta Glow Candle":

    st.image("images/Terracota Glow.png", width=250)

    color = st.selectbox("Choose Jar Color", colors)
    fragrance = st.selectbox("Choose Fragrance", fragrances)

    price = 199

elif product == "Wax Sachet":

    st.subheader("Choose Shape")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/Rectangular.png", caption="Rectangular")

    with col2:
        st.image("images/Rhombus.png", caption="Rhombus")

    with col3:
        st.image("images/Oval.png", caption="Oval")

    shape = st.radio(
        "Select Shape",
        ["Rectangular", "Rhombus", "Oval"],
        horizontal=True
    )

    color_bg = st.selectbox(
        "Choose Background Color",
        colors
    )

    color_flr = st.selectbox(
        "Choose Flower Color",
        colors
    )

    fragrance = st.selectbox(
        "Choose Fragrance",
        fragrances
    )

    price = 99

# ==========================================
# PRICE DISPLAY
# ==========================================

st.subheader(f"💰 Price: ₹{price}")

# ==========================================
# CUSTOMER DETAILS
# ==========================================

st.header("📋 Customer Details")

name = st.text_input("Name")
mobile = st.text_input("Mobile Number")
hall = st.text_input("Hall No")
room = st.text_input("Room No")

# ==========================================
# WHATSAPP NUMBER
# ==========================================

YOUR_NUMBER = "916394996857"

# ==========================================
# ORDER BUTTON
# ==========================================

if st.button("🛒 Place Order"):

    if not name or not mobile or not hall or not room:

        st.warning("Please fill Name, Mobile Number, Hall and room number.")

    else:

        if product == "Wax Sachet":

            order_details = f"""
🕯️ *Zigcxy Bliss Order*

👤 Name: {name}
📱 Mobile: {mobile}
🏠 Hall: {hall}
🚪 Room: {room}

📦 Product: {product}
⭐ Shape: {shape}
🎨 Background Color: {color_bg}
🎨 Background Color: {color_flr}
🌸 Fragrance: {fragrance}

💰 Price: ₹{price}
"""

        else:

            order_details = f"""
🕯️ *Zigcxy Bliss Order*

👤 Name: {name}
📧 Email: {email}
📱 Mobile: {mobile}
🏠 Hall: {hall}
🚪 Room: {room}

📦 Product: {product}
🎨 Color: {color}
🌸 Fragrance: {fragrance}

💰 Price: ₹{price}
"""

        encoded_message = urllib.parse.quote(order_details)

        whatsapp_url = (
            f"https://wa.me/{YOUR_NUMBER}?text={encoded_message}"
        )

        st.link_button(
            "📲 Confirm Order on WhatsApp",
            whatsapp_url
        )

        st.success(
            "Order generated successfully. Click the WhatsApp button above."
        )
