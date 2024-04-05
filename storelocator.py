import streamlit as st
import pandas as pd

# Load data
def load_data():
    return pd.read_excel('insulin information.xlsx')

store_data = load_data()

# Streamlit app
def main():
    # HTML for gradient background
    st.markdown("""
        <style>
        .reportview-container {
            background: linear-gradient(to right, #4ca1af, #c4e0e5);
            color: black;
        }
        table.dataframe {
            width: 100%;
        }
        </style>
        """, unsafe_allow_html=True)

    # Title
    st.title('Store Information by Pincode')

    # Sidebar - Pincode input with default values
    default_pincodes = ['400602', '400808', '400601', '401107', '400091', '400086', '400022', '400014', '400042', '400079', '400053', '400050', '400054', '400052', '400056', '400055', '400013', '400008', '400011', '400012', '400004']  # Example default pincodes
    pincode = st.sidebar.selectbox("Select Store Pincode", default_pincodes)

    # Convert pincode to integer for comparison
    pincode = int(pincode)

    # Filter data based on pincode
    filtered_data = store_data[store_data['Store Pincode'] == pincode]

    # Display filtered data
    if not filtered_data.empty:
        st.subheader(f'Store Information for Pincode {pincode}:')
        # Display selected columns: Store Name, Brand Name, Insulin Name, Insulin Type, Price, and Quantity Available
        st.dataframe(filtered_data[['Shop Name', 'Brand Name', 'Brand Type', 'Division', 'Price (INR)', 'Quantity Available (Multiples Of 30Kg)']])
    else:
        st.write(f"No store found for the pincode '{pincode}'.")

if __name__ == '__main__':
    main()
