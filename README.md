# 🛒 Product Recommender System (Streamlit App)

This project is a **content-based product recommendation system** built using **Python and Streamlit**.  
It recommends similar products based on a **precomputed similarity matrix** and displays product images in an interactive web interface.

---

## 📌 Overview

Given a selected product, the system suggests **top 5 similar products** by comparing product features using cosine similarity.  
The app uses **Streamlit** to provide a clean and interactive UI for exploring recommendations.

---

## ✨ Features

- 🔍 Content-based product recommendations
- 🧠 Similarity-based matching using cosine similarity
- ⚡ Fast recommendations using precomputed similarity matrix
- 🖼️ Product image display
- 🎨 Simple and interactive Streamlit interface
- 📦 Lightweight and easy to run

---

## 🛠️ Tech Stack

| Category | Technology |
|--------|-----------|
| Language | Python |
| Web App | Streamlit |
| Data Handling | Pandas |
| ML / Similarity | Scikit-learn (offline) |
| Serialization | Pickle |

---

## 📂 Project Structure

```text
Product-Recommender-Streamlit/
│── app.py                  # Streamlit application
│── products_dict.pkl       # Serialized product metadata
│── similarity.pkl          # Precomputed similarity matrix
│── README.md
```

---

## ⚙️ How It Works
1. Load product data and similarity matrix from pickle files
2. User selects a product from the dropdown
3. Similar products are ranked using cosine similarity
4. Top 5 recommendations are displayed with product images

---

## 🚀 How to Run Locally
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Naman-27072004/product-recommender-system.git
cd product-recommender-streamlit
```
### 2️⃣ Install Dependencies
```bash
pip install streamlit pandas
```
### 3️⃣ Run the App
```bash
streamlit run app.py
```
The app will open in your browser at:
```bash
http://localhost:8501
```
---

## 🧪 Example Usage
- Select a product from the dropdown
- Click “Show Recommendation”
- View 5 similar products with images

---

## ⚠️ Notes
- This is a content-based recommender
- No user behavior or ratings are used
- Recommendations depend on the quality of product features

---

## 🔮 Future Improvements
- Add search functionality
- Use TF-IDF instead of CountVectorizer
- Add price and rating filters
- Deploy on Streamlit Cloud
- Improve recommendation ranking logic

---

## 🧾 License
This project is licensed under the MIT License.

---

## 📬 Author
- Naman Gupta
- MCA @ JIMS Rohini
- Full-Stack Developer | AI & ML Enthusiast


