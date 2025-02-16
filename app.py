import streamlit as st 
import pandas as pd

st.title("Car dekho")

data = {
    "original_equipment_manufacturer": [
        "Audi", "Audi", "Audi", "BMW", "BMW", "Chevrolet", "Chevrolet"
    ],
    "car_model": [
        "Audi A4", "Audi A6", "Audi Q7", "BMW 5 Series", "BMW 3 Series GT",
        "Chevrolet Cruze", "Chevrolet Beat"
    ],
    "variant_name": [
        "35 TDI Premium", "35 TDI", "35 TDI Quattro Premium", "520d Sedan",
        "530i Sport", "LTZ", "1.0 LS"
    ]
}

# Creating DataFrame
df = pd.DataFrame(data)

grouped_df = df.groupby("original_equipment_manufacturer")[["car_model", "variant_name"]].agg(list).reset_index()

option = st.sidebar.selectbox("Select a car manufacturer",options=grouped_df['original_equipment_manufacturer'].to_list())

