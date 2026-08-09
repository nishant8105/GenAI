import streamlit as st

# Title and description
st.title("📊 Simple Sales Dashboard")
st.write("Select a month to view its sales.")

# Months
months = ["January", "February", "March", "April"]

# Monthly sales
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

# Selectbox
selected_month = st.selectbox(
    "Select Month",
    months
)

# Display selected month's sales
st.metric(
    label=f"Sales for {selected_month}",
    value=f"₹{sales[selected_month]}"
)

# Bar chart
st.subheader("Monthly Sales")

st.bar_chart(list(sales.values()))