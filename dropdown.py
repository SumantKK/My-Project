import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the trained Logistic Regression model
with open('log_model.pkl', 'rb') as file:
    lr_model = pickle.load(file)
    
# Function to get pincode based on store name
def get_pincode(store_name):
    pincode_dict = {
        'Colour Corner': '400602',
        'National Enterprises': '400808',
        'Mangalam Paints': '400808',
        'Shrisha Paints And Hardware': '400602',
        'Bombay Paints': '400602',
        'Bhawana Trading Company': '400808',
        'Bhagyalaxmi Enterprises': '400601',
        'Niranjan Paints': '401107',
        'Shubh Tiles - | Tile Adhesive & Waterproofing |': '400091',
        'Prabhat Colour Company': '400086',
        'Arihant Paints': '400022',
        'Dilip Paints': '400022',
        'New Neelam Hardware & Paints Store': '400086',
        'Colourworld - Shivkrupa Hardware & Paint Stores': '400014',
        'Rainbow paints': '400042',
        'Everest Paints': '400042',
        'Krishna Paint Centre': '400014',
        'Shanti Colour House': '400086',
        'Mahadev Paints': '400079',
        'Rajput Hardware': '400053',
        'Lucky Paint Store': '400050',
        'Omkar Colour & Hardw.': '400054',
        'Ganesh Paint House': '400050',
        'Vishwakarma Paints': '400053',
        'Mehta Paint & Hardw.': '400052',
        'National Paint House': '400052',
        'Durga Paints': '400056',
        'Sai Hardware': '400056',
        'Amrut Hardware': '400055',
        'Umiya Paint Centre': '400013',
        'Royal Hardware': '400008',
        'Pooja Colour & Paints': '400008',
        'Shree Ganesh Paint Centre': '400011',
        'Vishwakarma Paints & Hardware': '400013',
        'Mehta Paints': '400012',
        'National Paint House': '400004',
        'Sai Hardware': '400004',
        'Laxmi Colour House': '400004',
        'Umiya Paint Centre': '400004',
        'Devaki Paints & Hardware': '400091',
        'Arihant Hardware': '400055',
        'Sona Ceramics & Hardware': '400055'
    }
    return pincode_dict.get(store_name, '')



def get_insulin_details(brand_name):
    insulin_details = {
        'Ultratech': {'Insulin Name': 'Ultratech Tilefixo NT Good Bonding', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '30', 'Price (INR)': 740},
        'Ascolite': {'Insulin Name': 'Ascolite Fixobond Polymer Modified Tile Adhesive', 'Insulin Type':'Mumbai North', 'Dosage Strength': '50', 'Price (INR)': 630},
        'Build': {'Insulin Name': 'Build Green Tile Adhesive', 'Insulin Type': 'Mumbai Central / Eastern', 'Dosage Strength': '10', 'Price (INR)': 650},
        'Capaland': {'Insulin Name': 'Capaland Plus (Grey) C1T', 'Insulin Type': 'Mumbai Central / Eastern', 'Dosage Strength': '10', 'Price (INR)': 770},
        'DR': {'Insulin Name': 'DR Fixit Floor Tile Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '30', 'Price (INR)': 630},
        'Duw': {'Insulin Name': 'Duw Fix S1 252 Floor Tiling Solutions Adhesion', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '10', 'Price (INR)': 740},
        'Fosroc': {'Insulin Name': 'Fosroc Nitotile Mpa Tile Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '10', 'Price (INR)': 660},
        'Hawks': {'Insulin Name': 'Hawks Tile Fixing Plaster', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '30', 'Price (INR)': 610},
        'Indiana': {'Insulin Name': 'Indiana Colors BondEx Tile Adhesive T2 Non-Skid Tile', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '10', 'Price (INR)': 750},
        'JK': {'Insulin Name': 'JK Cement Supreme White Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '50', 'Price (INR)': 790},
        'LATICRETE': {'Insulin Name': 'LATICRETE 335 Super Flex Multipurpose Floor And Wall Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '10', 'Price (INR)': 720},
        'Mcon': {'Insulin Name': 'Mcon Super Add', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '10', 'Price (INR)': 690},
        'Myk': {'Insulin Name': 'Myk Laticrete L-325 High Flex White', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '10', 'Price (INR)': 760},
        'Roff': {'Insulin Name': 'Roff Non Skid Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '10', 'Price (INR)': 600},
        'ROKSO': {'Insulin Name': 'ROKSO Tile On Tile TTF Tile Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '10', 'Price (INR)': 700},
        'Sika': {'Insulin Name': 'Sika Ceram 255 Large Tile Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '50', 'Price (INR)': 610},
        'TIPRO': {'Insulin Name': 'TIPRO - NSA -309 GREY TILE ON TILE Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '10', 'Price (INR)': 760},
        'Vura': {'Insulin Name': 'Vura Fastile Plus White Tile Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '30', 'Price (INR)': 680},
        'Webber': {'Insulin Name': 'Webber Floor Tile Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': '30', 'Price (INR)': 610}
                
    }
    return insulin_details.get(brand_name, {'Insulin Name': '', 'Insulin Type': '', 'Dosage Strength': '', 'Price (INR)': ''})

store_to_brands = {
    'Colour Corner': ['Ultratech', 'Webber', 'Mcon'],
    'National Enterprises': ['Myk', 'Ultratech', 'ROKSO', 'Capaland'],
    'Mangalam Paints': ['Ultratech', 'Ascolite', 'Duw'],
    'Shrisha Paints And Hardware': ['Fosroc', 'Hawks', 'Indiana', 'Ascolite'],
    'Bombay Paints': ['Vura', 'JK', 'Ultratech', 'Mcon'],
    'Bhawana Trading Company': ['DR', 'Mcon', 'Ultratech'],
    'Bhagyalaxmi Enterprises': ['Roff', 'Sika', 'Ultratech', 'LATICRETE'],
    'Niranjan Paints': ['Build', 'Webber', 'TIPRO', 'Capaland'],
    'Shubh Tiles - | Tile Adhesive & Waterproofing |': ['Duw', 'Ultratech', 'Fosroc'],
    'Prabhat Colour Company': ['Webber', 'Myk', 'Mcon', 'Ultratech'],
    'Arihant Paints': ['Ultratech', 'Ascolite', 'Mcon'],
    'Dilip Paints': ['Ultratech', 'Capaland', 'Indiana', 'Vura'],
    'New Neelam Hardware & Paints Store': ['ROKSO', 'Sika', 'Ultratech', 'Hawks'],
    'Colourworld - Shivkrupa Hardware & Paint Stores': ['Ultratech', 'Mcon', 'Myk'],
    'Rainbow paints': ['Ascolite', 'Webber', 'Ultratech', 'DR'],
    'Everest Paints': ['TIPRO', 'Fosroc', 'Ultratech', 'Roff', 'LATICRETE'],
    'Krishna Paint Centre': ['Ultratech', 'Mcon', 'JK'],
    'Shanti Colour House': ['Hawks', 'Ascolite', 'Ultratech', 'Indiana'],
    'Mahadev Paints': ['Ultratech', 'Vura', 'Webber', 'Build'],
    'Rajput Hardware': ['Ultratech', 'Mcon', 'DR'],
    'Lucky Paint Store': ['Ascolite', 'TIPRO', 'Ultratech', 'Myk'],
    'Omkar Colour & Hardw.': ['Fosroc', 'Capaland', 'ROKSO'],
    'Ganesh Paint House': ['Roff', 'Sika', 'Ultratech'],
    'Vishwakarma Paints': ['Mcon', 'Hawks', 'Ascolite', 'Ultratech'],
    'Mehta Paint & Hardw.': ['DR', 'Ultratech', 'Mcon'],
    'National Paint House': ['Indiana', 'Ultratech', 'Webber', 'Myk', 'Hawks', 'TIPRO'],
    'Durga Paints': ['Ultratech', 'Ascolite', 'Fosroc'],
    'Sai Hardware': ['Capaland', 'ROKSO', 'Ultratech', 'Sika'],
    'Amrut Hardware': ['Ultratech', 'Mcon', 'Myk'],
    'Umiya Paint Centre': ['TIPRO', 'Ascolite', 'Hawks', 'Ultratech', 'DR'],
    'Royal Hardware': ['Roff', 'DR', 'Indiana', 'Ultratech'],
    'Pooja Colour & Paints': ['Mcon', 'Webber', 'Ultratech', 'Fosroc'],
    'Shree Ganesh Paint Centre': ['Ultratech', 'Capaland'],
    'Vishwakarma Paints & Hardware': ['Vura', 'Myk', 'Ultratech'],
    'Mehta Paints': ['Mcon', 'Ascolite', 'ROKSO', 'Ultratech'],
    'Laxmi Colour House': ['Indiana', 'Ultratech', 'Webber', 'Roff'],
    'Devaki Paints & Hardware': ['Ascolite', 'Ultratech', 'Myk'],
    'Arihant Hardware': ['ROKSO', 'Hawks', 'Fosroc', 'Ultratech'],
    'Sona Ceramics & Hardware': ['Webber', 'DR', 'ROKSO', 'Sika', 'Ascolite']

}

# Streamlit app
def main():
    # HTML for gradient background and styling
    st.markdown("""
    <style>
    .reportview-container {
        background: linear-gradient(to right, #ff99ff 0%, #99ccff 100%);
        color: white;
        font-size: 16px;
    }      
    .widget-dropdown > div[role="button"] {
        background-color: white;
        color: black;
    }
    .widget button[data-baseweb="button"] {
        background-color: #004080;
        color: white;
    }
    .stButton>button {
        background-color: #FF0000;
        color: white;
    }
    .warning-box {
        color: black !important;
        background-color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title
    st.title('Insulin Stock Prediction')

    # Input fields
    st.write('Enter the following details:')

    # Dropdown options for each feature
    store_names = [
        'Colour Corner',
        'National Enterprises',
        'Mangalam Paints',
        'Shrisha Paints And Hardware',
        'Bombay Paints',
        'Bhawana Trading Company',
        'Bhagyalaxmi Enterprises',
        'Niranjan Paints',
        'Shubh Tiles - | Tile Adhesive & Waterproofing |',
        'Prabhat Colour Company',
        'Arihant Paints',
        'Dilip Paints',
        'New Neelam Hardware & Paints Store',
        'Colourworld - Shivkrupa Hardware & Paint Stores',
        'Rainbow paints',
        'Everest Paints',
        'Krishna Paint Centre',
        'Shanti Colour House',
        'Mahadev Paints',
        'Rajput Hardware',
        'Lucky Paint Store',
        'Omkar Colour & Hardw.',
        'Ganesh Paint House',
        'Vishwakarma Paints',
        'Mehta Paint & Hardw.',
        'National Paint House',
        'Durga Paints',
        'Sai Hardware',
        'Amrut Hardware',
        'Umiya Paint Centre',
        'Royal Hardware',
        'Pooja Colour & Paints',
        'Shree Ganesh Paint Centre',
        'Vishwakarma Paints & Hardware',
        'Mehta Paints',
        'Laxmi Colour House',
        'Devaki Paints & Hardware',
        'Arihant Hardware',
        'Sona Ceramics & Hardware'
    ]

    store_name = st.selectbox('Store Name', store_names)
    pincode = get_pincode(store_name)
    st.write('Store Pincode:', pincode)

    # Dropdown options for brand name
    brand_names = [
        'Ultratech', 
        'DR', 
        'Myk', 
        'Capaland', 
        'TIPRO', 
        'Webber', 
        'Vura', 
        'Fosroc', 
        'Build', 
        'LATICRETE', 
        'JK', 
        'Hawks', 
        'Indiana', 
        'Duw', 
        'Roff', 
        'Sika', 
        'ROKSO', 
        'Mcon', 
        'Ascolite'
    ]
    
    brand_name = st.selectbox('Brand Name', brand_names)

    if brand_name not in store_to_brands.get(store_name, []):
        st.warning("Selected brand is not available in this store.")
    else:
        st.success("Selected brand is available in this store.")
        
    insulin_details = get_insulin_details(brand_name)  # Retrieve insulin details based on brand name
    insulin_name = insulin_details['Insulin Name']
    insulin_type = insulin_details['Insulin Type']
    dosage_strength = insulin_details['Dosage Strength']
    price = insulin_details['Price (INR)']

    # Display insulin details
    st.write('Insulin Name:', insulin_details.get('Insulin Name', ''))
    st.write('Insulin Type:', insulin_details.get('Insulin Type', ''))

    # Dropdown options for dosage strength
    dosage_strengths = ['10','30']
    dosage_strength = st.selectbox('Dosage Strength', dosage_strengths)

    # Display price based on selected brand name
    st.write('Price (INR):', insulin_details.get('Price (INR)', ''))
    
    # Make prediction on button click
    if st.button('Predict'):
        # If selected brand is not available in the selected store
        if brand_name not in store_to_brands.get(store_name, []):
            st.warning("Selected brand is not available in this store. Predicted Insulin Stock: 0")
        else:
            # Convert input data to DataFrame
            input_data = pd.DataFrame({
                'Store Name': [store_name],
                'Store Pincode': [pincode],
                'Brand Name': [brand_name],
                'Insulin Name': [insulin_name],
                'Insulin Type': [insulin_type],
                'Dosage Strength': [dosage_strength],
                'Price (INR)': [price]
            })

            # Perform label encoding for categorical text features
            categorical_features = ['Store Name', 'Brand Name', 'Insulin Name', 'Insulin Type']
            label_encoders = {}  # Dictionary to store label encoders for each categorical feature
            for feature in categorical_features:
                # Initialize label encoder for the feature
                label_encoders[feature] = LabelEncoder()
                # Fit label encoder and transform the feature
                input_data[feature] = label_encoders[feature].fit_transform(input_data[feature])

            # Make prediction
            prediction = lr_model.predict(input_data)
            # Display prediction
            st.write('Predicted Insulin Stock:', prediction[0])

if __name__ == '__main__':
    main()
