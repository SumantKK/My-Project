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
        'Ultratech': {'Insulin Name': 'Ultratech Tilefixo NT Good Bonding', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'Medium', 'Price (INR)': 740},
        'Ascolite': {'Insulin Name': 'Ascolite Fixobond Polymer Modified Tile Adhesive', 'Mumbai North': 'long-acting', 'Dosage Strength': 'High', 'Price (INR)': 630},
        'Build': {'Insulin Name': 'Build Green Tile Adhesive', 'Insulin Type': 'Mumbai Central / Eastern', 'Dosage Strength': 'Low', 'Price (INR)': 650},
        'Capaland': {'Insulin Name': 'Capaland Plus (Grey) C1T', 'Insulin Type': 'Mumbai Central / Eastern', 'Dosage Strength': 'Low', 'Price (INR)': 770},
        'DR': {'Insulin Name': 'DR Fixit Floor Tile Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'Medium', 'Price (INR)': 630},
        'Duw': {'Insulin Name': 'Duw Fix S1 252 Floor Tiling Solutions Adhesion', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'Low', 'Price (INR)': 740},
        'Fosroc': {'Insulin Name': 'Fosroc Nitotile Mpa Tile Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'Low', 'Price (INR)': 660},
        'Hawks': {'Insulin Name': 'Hawks Tile Fixing Plaster', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'Medium', 'Price (INR)': 610},
        'Indiana': {'Insulin Name': 'Indiana Colors BondEx Tile Adhesive T2 Non-Skid Tile', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'Low', 'Price (INR)': 750},
        'JK': {'Insulin Name': 'JK Cement Supreme White Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'High', 'Price (INR)': 790},
        'LATICRETE': {'Insulin Name': 'LATICRETE 335 Super Flex Multipurpose Floor And Wall Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'Low', 'Price (INR)': 720},
        'Mcon': {'Insulin Name': 'Mcon Super Add', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'Low', 'Price (INR)': 690},
        'Myk': {'Insulin Name': 'Myk Laticrete L-325 High Flex White', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'High', 'Price (INR)': 760},
        'Roff': {'Insulin Name': 'Roff Non Skid Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'Low', 'Price (INR)': 600},
        'ROKSO': {'Insulin Name': 'ROKSO Tile On Tile TTF Tile Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'Low', 'Price (INR)': 700},
        'Sika': {'Insulin Name': 'Sika Ceram 255 Large Tile Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'High', 'Price (INR)': 610},
        'TIPRO': {'Insulin Name': 'TIPRO - NSA -309 GREY TILE ON TILE Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'Low', 'Price (INR)': 760},
        'Vura': {'Insulin Name': 'Vura Fastile Plus White Tile Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'Medium', 'Price (INR)': 680},
        'Webber': {'Insulin Name': 'Webber Floor Tile Adhesive', 'Insulin Type': 'Mumbai North', 'Dosage Strength': 'Medium', 'Price (INR)': 610}
                
    }
    return insulin_details.get(brand_name, {'Insulin Name': '', 'Insulin Type': '', 'Dosage Strength': '', 'Price (INR)': ''})

store_to_brands = {
    'Colour Corner': ['Ultratech Tilefixo NT Good Bonding', 'Webber Floor Tile Adhesive', 'Mcon Super Add'],
    'National Enterprises': ['Myk Laticrete L-325 High Flex White', 'Ultratech Tile Fixo Nt', 'ROKSO Tile On Tile TTF Tile Adhesive', 'Capaland Plus (Grey) C1T'],
    'Mangalam Paints': ['Ultratech Tilefixo CT Floor Tile Adhesive', 'Ascolite Fixobond Polymer Modified Tile Adhesive', 'Duw Fix S1 252 Floor Tiling Solutions Adhesion'],
    'Shrisha Paints And Hardware': ['Fosroc Nitotile Mpa Tile Adhesive', 'Hawks Tile Fixing Plaster', 'Indiana Colors BondEx Tile Adhesive T2 Non-Skid Tile', 'Ascolite Wall Floor Tile Adhesive'],
    'Bombay Paints': ['Vura Fastile Plus White Tile Adhesive', 'JK Cement Supreme White Adhesive', 'Ultratech Tilefixo VT Tile Adhesive', 'Mcon Tile Adhesive'],
    'Bhawana Trading Company': ['DR Fixit Floor Tile Adhesive', 'Mcon Super Add', 'Ultratech Tilefixo CT Floor Tile Adhesive'],
    'Bhagyalaxmi Enterprises': ['Roff Non Skid Adhesive', 'Sika Ceram 255 Large Tile Adhesive', 'Ultratech Tilefixo VT Tile Adhesive', 'LATICRETE 335 Super Flex Multipurpose Floor And Wall Adhesive'],
    'Niranjan Paints': ['Build Green Tile Adhesive', 'Webber Floor Tile Adhesive', 'TIPRO - NSA -309 GREY TILE ON TILE Adhesive', 'Capaland Plus (Grey) C1T'],
    'Shubh Tiles - | Tile Adhesive & Waterproofing |': ['Duw Fix S1 252 Floor Tiling Solutions Adhesion', 'Ultratech Tilefixo CT Floor Tile Adhesive', 'Fosroc Nitotile Mpa Tile Adhesive', 'Ultratech Tilefixo VT Tile Adhesive'],
    'Prabhat Colour Company': ['Webber Floor Tile Adhesive', 'Myk Laticrete L-325 High Flex White', 'Mcon Super Add', 'Ultratech Tilefixo CT Floor Tile Adhesive'],
    'Arihant Paints': ['Ultratech Tilefixo Nt', 'Ascolite Wall Floor Tile Adhesive', 'Mcon Super Add', 'Mcon Tile Adhesive'],
    'Dilip Paints': ['Ultratech Tile Fixo Nt', 'Capaland Plus (Grey) C1T', 'Indiana Colors BondEx Tile Adhesive T2 Non-Skid Tile', 'Vura Fastile Plus White Tile Adhesive'],
    'New Neelam Hardware & Paints Store': ['ROKSO Tile On Tile TTF Tile Adhesive', 'Sika Ceram 255 Large Tile Adhesive', 'Ultratech Tilefixo VT Tile Adhesive', 'Hawks Tile Fixing Plaster'],
    'Colourworld - Shivkrupa Hardware & Paint Stores': ['Ultratech Tilefixo CT Floor Tile Adhesive', 'Mcon Tile Adhesive', 'Myk Laticrete L-325 High Flex White'],
    'Rainbow paints': ['Ascolite Wall Floor Tile Adhesive', 'Webber Floor Tile Adhesive', 'Ultratech Tilefixo NT Good Bonding', 'DR Fixit Floor Tile Adhesive'],
    'Everest Paints': ['TIPRO - NSA -309 GREY TILE ON TILE Adhesive', 'Fosroc Nitotile Mpa Tile Adhesive', 'Ultratech Tilefixo CT Floor Tile Adhesive', 'Roff Non Skid Adhesive', 'LATICRETE 335 Super Flex Multipurpose Floor And Wall Adhesive'],
    'Krishna Paint Centre': ['Ultratech Tilefixo VT Tile Adhesive', 'Mcon Super Add', 'JK Cement Supreme White Adhesive'],
    'Shanti Colour House': ['Hawks Tile Fixing Plaster', 'Ascolite Fixobond Polymer Modified Tile Adhesive', 'Ultratech Tilefixo CT Floor Tile Adhesive', 'Indiana Colors BondEx Tile Adhesive T2 Non-Skid Tile'],
    'Mahadev Paints': ['Ultratech Tile Fixo Nt', 'Vura Fastile Plus White Tile Adhesive', 'Webber Floor Tile Adhesive', 'Build Green Tile Adhesive'],
    'Rajput Hardware': ['Ultratech Tilefixo VT Tile Adhesive', 'Mcon Tile Adhesive', 'DR Fixit Floor Tile Adhesive'],
    'Lucky Paint Store': ['Ascolite Wall Floor Tile Adhesive', 'TIPRO - NSA -309 GREY TILE ON TILE Adhesive', 'Ultratech Tilefixo NT Good Bonding', 'Myk Laticrete L-325 High Flex White'],
    'Omkar Colour & Hardw.': ['Fosroc Nitotile Mpa Tile Adhesive', 'Capaland Plus (Grey) C1T', 'ROKSO Tile On Tile TTF Tile Adhesive'],
    'Ganesh Paint House': ['Roff Non Skid Adhesive', 'Sika Ceram 255 Large Tile Adhesive', 'Ultratech Tilefixo VT Tile Adhesive', 'Ultratech Tilefixo CT Floor Tile Adhesive'],
    'Vishwakarma Paints': ['Mcon Tile Adhesive', 'Hawks Tile Fixing Plaster', 'Ascolite Fixobond Polymer Modified Tile Adhesive', 'Ultratech Tilefixo CT Floor Tile Adhesive'],
    'Mehta Paint & Hardw.': ['DR Fixit Floor Tile Adhesive', 'Ultratech Tilefixo VT Tile Adhesive', 'Mcon Super Add'],
    'National Paint House': ['Indiana Colors BondEx Tile Adhesive T2 Non-Skid Tile', 'Ultratech Tile Fixo Nt', 'Webber Floor Tile Adhesive', 'Myk Laticrete L-325 High Flex White'],
    'Durga Paints': ['Ultratech Tilefixo CT Floor Tile Adhesive', 'Ascolite Wall Floor Tile Adhesive', 'Fosroc Nitotile Mpa Tile Adhesive'],
    'Sai Hardware': ['Capaland Plus (Grey) C1T', 'ROKSO Tile On Tile TTF Tile Adhesive', 'Ultratech Tile Fixo Nt', 'Ultratech Tilefixo VT Tile Adhesive'],
    'Amrut Hardware': ['Ultratech Tilefixo VT Tile Adhesive', 'Mcon Tile Adhesive', 'Myk Laticrete L-325 High Flex White', 'Ultratech Tilefixo CT Floor Tile Adhesive'],
    'Umiya Paint Centre': ['TIPRO - NSA -309 GREY TILE ON TILE Adhesive', 'Ascolite Fixobond Polymer Modified Tile Adhesive', 'Hawks Tile Fixing Plaster', 'Ultratech Tilefixo VT Tile Adhesive', 'Ultratech Tilefixo Nt'],
    'Royal Hardware': ['Roff Non Skid Adhesive', 'DR Fixit Floor Tile Adhesive', 'Indiana Colors BondEx Tile Adhesive T2 Non-Skid Tile', 'Ultratech Tilefixo VT Tile Adhesive'],
    'Pooja Colour & Paints': ['Mcon Super Add', 'Webber Floor Tile Adhesive', 'Ultratech Tilefixo CT Floor Tile Adhesive', 'Fosroc Nitotile Mpa Tile Adhesive'],
    'Shree Ganesh Paint Centre': ['Ultratech Tilefixo NT Good Bonding', 'Capaland Plus (Grey) C1T', 'Ultratech Tile Fixo Nt'],
    'Vishwakarma Paints & Hardware': ['Vura Fastile Plus White Tile Adhesive', 'Myk Laticrete L-325 High Flex White', 'Ultratech Tilefixo VT Tile Adhesive'],
    'Mehta Paints': ['Mcon Tile Adhesive', 'Ascolite Wall Floor Tile Adhesive', 'ROKSO Tile On Tile TTF Tile Adhesive', 'Ultratech Tilefixo CT Floor Tile Adhesive'],
    'Laxmi Colour House': ['Indiana Colors BondEx Tile Adhesive T2 Non-Skid Tile', 'Ultratech Tilefixo CT Floor Tile Adhesive', 'Webber Floor Tile Adhesive', 'Roff Non Skid Adhesive'],
    'Devaki Paints & Hardware': ['Ascolite Fixobond Polymer Modified Tile Adhesive', 'Ultratech Tilefixo CT Floor Tile Adhesive', 'Ultratech Tilefixo NT Good Bonding', 'Myk Laticrete L-325 High Flex White'],
    'Arihant Hardware': ['ROKSO Tile On Tile TTF Tile Adhesive', 'Hawks Tile Fixing Plaster', 'Fosroc Nitotile Mpa Tile Adhesive', 'Ultratech Tile Fixo Nt'],
    'Sona Ceramics & Hardware': ['Webber Floor Tile Adhesive', 'DR Fixit Floor Tile Adhesive', 'ROKSO Tile On Tile TTF Tile Adhesive', 'Sika Ceram 255 Large Tile Adhesive', 'Ascolite Fixobond Polymer Modified Tile Adhesive']


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
    brand_names = ['Ultratech', 'Webber', 'Mcon', 'Myk', 'ROKSO', 'Capaland', 'Ascolite', 'Duw', 'Fosroc', 'Hawks', 'Indiana', 'Vura', 'JK', 'DR', 'Roff', 'Sika', 'LATICRETE', 'Build', 'TIPRO']
    
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
    dosage_strengths = ['High', 'Medium','Low']
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
