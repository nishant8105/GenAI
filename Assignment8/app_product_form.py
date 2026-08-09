import streamlit as st

st.title("🛍️ Product Manager")

# Sidebar
st.sidebar.header("Add Product")

product_name = st.sidebar.text_input("Product Name")

category = st.sidebar.selectbox(
    "Category",
    ["Electronics", "Clothing", "Food", "Books", "Home"]
)

price = st.sidebar.number_input(
    "Price",
    min_value=0.0,
    step=100.0
)

add_product = st.sidebar.button("Add Product")

# When button is clicked
if add_product:
    st.success("✅ Product added successfully!")

    st.subheader("Product Details")

    st.write(f"**Product Name:** {product_name}")
    st.write(f"**Category:** {category}")
    st.write(f"**Price:** ₹{price:,.2f}")