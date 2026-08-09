import streamlit as st

num = st.number_input("Enter Product price")
discount = st.slider(
    "Slide discount: ",
    min_value=0,
    max_value= 50
)

price = num - (num * (discount/100))
data = {
    "Item": ["Original", "Discount", "Final Price"],
    "Value": [num, discount, price]
}


if st.button("Calculate"):

    st.success(price)

    st.write(f"Original : {num}")
    st.write(f"Discount: {discount}")
    st.write(f"Final price: {price}")
    st.table(data)