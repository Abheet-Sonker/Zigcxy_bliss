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
st.markdown("""
### ✨ Handmade Candles & Wax Sachets

🌸 Custom Colors  
🌸 Premium Fragrances  
🌸 Personalized Designs  

Create your own aesthetic product and order directly through WhatsApp.
""")
st.subheader("Customize & Order Your Handmade Products")

# ==========================================
# SESSION STATE
# ==========================================

if "cart" not in st.session_state:
    st.session_state.cart = []

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
    "Orange",
    "Custom Color"
]

fragrances = [
    "Amber",
    "Cinnamon",
    "Coffee",
    "Lavender",
    "Vanilla"
]

# ==========================================
# COLOR PICKER FUNCTION
# ==========================================

def get_color_input(label, key_prefix=""):

    color_mode = st.radio(
        f"{label} Selection Method",
        ["Preset Colors", "Custom Color Name"],
        horizontal=True,
        key=f"{key_prefix}_mode"
    )

    if color_mode == "Preset Colors":

        selected_color = st.selectbox(
            label,
            colors,
            key=f"{key_prefix}_select"
        )

        if selected_color == "Custom Color":

            color = st.text_input(
                "Enter Custom Color",
                placeholder="Example: Sky Blue, Mint Green, Peach",
                key=f"{key_prefix}_custom"
            )

        else:
            color = selected_color

    else:

        color = st.text_input(
            f"Enter {label}",
            placeholder="Example: Pastel Pink, Ivory, Navy Blue",
            key=f"{key_prefix}_manual"
        )

    return color

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

price = 0

# ==========================================
# PRODUCT CUSTOMIZATION
# ==========================================

if product == "Mess Glow Candle":

    st.image("images/Mess Glow.png", width=250)

    color = get_color_input(
        "Choose Jar Color",
        "mess"
    )

    fragrance = st.selectbox(
        "Choose Fragrance",
        fragrances
    )

    price = 199

elif product == "Terracotta Glow Candle":

    st.image("images/Terracota Glow.png", width=250)

    color = get_color_input(
        "Choose Jar Color",
        "terra"
    )

    fragrance = st.selectbox(
        "Choose Fragrance",
        fragrances
    )

    price = 299

elif product == "Wax Sachet":

    st.subheader("Choose Shape")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "images/Rectangular.png",
            caption="Rectangular"
        )

    with col2:
        st.image(
            "images/Rhombus.png",
            caption="Rhombus"
        )

    with col3:
        st.image(
            "images/Oval.png",
            caption="Oval"
        )

    shape = st.radio(
        "Select Shape",
        ["Rectangular", "Rhombus", "Oval"],
        horizontal=True
    )

    color_bg = get_color_input(
        "Choose Background Color",
        "bg"
    )

    color_flr = get_color_input(
        "Choose Flower Color",
        "flower"
    )

    fragrance = st.selectbox(
        "Choose Fragrance",
        fragrances
    )

    price = 99

# ==========================================
# QUANTITY
# ==========================================

qty = st.number_input(
    "Quantity",
    min_value=1,
    value=1,
    step=1
)

# ==========================================
# PRICE CALCULATION
# ==========================================

item_total = price * qty

st.subheader(f"💰 Item Total: ₹{item_total}")

if delivery_charge > 0:
    st.warning(
        "₹40 delivery charge applied because Wax Sachet quantity is less than 2."
    )

# ==========================================
# ADD TO CART
# ==========================================

if st.button("➕ Add To Cart"):

    item = {
        "product": product,
        "qty": qty,
        "price": price,
        "total": item_total
    }

    if product == "Wax Sachet":

        item.update({
            "shape": shape,
            "bg_color": color_bg,
            "flower_color": color_flr,
            "fragrance": fragrance
        })

    else:

        item.update({
            "color": color,
            "fragrance": fragrance
        })

    st.session_state.cart.append(item)

    st.success("✅ Product added to cart!")

# ==========================================
# CART
# ==========================================

st.header("🛒 Your Cart")

grand_total = 0

if not st.session_state.cart:

    st.info("Cart is empty.")

else:

    for idx, item in enumerate(st.session_state.cart):

        with st.expander(
            f"{item['product']} | Qty: {item['qty']} | ₹{item['total']}"
        ):

            if item["product"] == "Wax Sachet":

                st.write(f"Shape: {item['shape']}")
                st.write(
                    f"Background Color: {item['bg_color']}"
                )
                st.write(
                    f"Flower Color: {item['flower_color']}"
                )

            else:

                st.write(
                    f"Color: {item['color']}"
                )

            st.write(
                f"Fragrance: {item['fragrance']}"
            )

            st.write(
                f"Quantity: {item['qty']}"
            )

            st.write(
                f"Subtotal: ₹{item['total']}"
            )

            if st.button(
                f"❌ Remove Item {idx+1}",
                key=f"remove_{idx}"
            ):
                st.session_state.cart.pop(idx)
                st.rerun()

        grand_total += item["total"]

    delivery_charge = 40 if grand_total < 198 else 0
    final_total = grand_total + delivery_charge
    
    st.subheader(f"Subtotal: ₹{grand_total}")
    
    if delivery_charge:
        st.warning(
            "₹40 delivery charge applied because order value is below ₹198."
        )
    
    st.subheader(f"💰 Final Total: ₹{final_total}")

# ==========================================
# CUSTOMER DETAILS
# ==========================================

st.header("📋 Customer Details")

name = st.text_input("Name")
mobile = st.text_input("Mobile Number")
address = st.text_input(
    "Address (Hall No, Room No)"
)

# ==========================================
# WHATSAPP NUMBER
# ==========================================

YOUR_NUMBER = "916394996857"

# ==========================================
# GENERATE ORDER
# ==========================================

if st.button("🛍️ Generate WhatsApp Order"):

    if len(st.session_state.cart) == 0:

        st.warning(
            "Please add at least one product."
        )

    elif not name or not mobile or not address:

        st.warning(
            "Please fill Name, Mobile Number and Address."
        )

    else:

        order_details = f"""
🕯️ *Zigcxy Bliss Order*

👤 Name: {name}
📱 Mobile: {mobile}
🏠 Address: {address}

----------------------------------
"""

        total = 0

        for i, item in enumerate(
            st.session_state.cart,
            start=1
        ):

            order_details += f"""

📦 Item {i}

Product: {item['product']}
Quantity: {item['qty']}
"""

            if item["product"] == "Wax Sachet":

                order_details += f"""
Shape: {item['shape']}
Background Color: {item['bg_color']}
Flower Color: {item['flower_color']}
Fragrance: {item['fragrance']}
"""

            else:

                order_details += f"""
Color: {item['color']}
Fragrance: {item['fragrance']}
"""

            order_details += f"""
Subtotal: ₹{item['total']}
----------------------------------
"""

            total += item["total"]

        order_details += f"""
delivery_charge = 40 if total < 198 else 0
grand_total = total + delivery_charge
Subtotal: ₹{total}
Delivery Charge: ₹{delivery_charge}

💰 GRAND TOTAL: ₹{grand_total}

Thank you for shopping with Zigcxy Bliss ✨

"""

        encoded_message = urllib.parse.quote(
            order_details
        )

        whatsapp_url = (
            f"https://wa.me/{YOUR_NUMBER}?text={encoded_message}"
        )

        st.link_button(
            "📲 Confirm Order on WhatsApp",
            whatsapp_url
        )

        st.success(
            "✅ Order generated successfully. Click the WhatsApp button above."
        )
