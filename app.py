# Import required libraries
import streamlit as st
import pickle
import pandas as pd

# Function to recommend products based on the selected product
def recommend(product):
    product_index = products[products['title'] == product].index[0]
    distances = similarity[product_index]
    products_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_product_names = []
    recommended_product_images = []
    for i in products_list:
        recommended_product_names.append(products.iloc[i[0]].title)
        recommended_product_images.append(products.iloc[i[0]].image)
    return recommended_product_names, recommended_product_images

# Title of the Streamlit app
st.title('Product Recommender System')

# Load products data and similarity matrix
products_dict = pickle.load(open('products_dict.pkl', 'rb'))
products = pd.DataFrame(products_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown menu for selecting a product
selected_product_name = st.selectbox(
    "Type or select a product from the dropdown",
    products['title'].values
)

# Show recommendations when the button is clicked
if st.button('Show Recommendation'):
    names, images = recommend(selected_product_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(images[0])
    with col2:
        st.text(names[1])
        st.image(images[1])
    with col3:
        st.text(names[2])
        st.image(images[2])
    with col4:
        st.text(names[3])
        st.image(images[3])
    with col5:
        st.text(names[4])
        st.image(images[4])
