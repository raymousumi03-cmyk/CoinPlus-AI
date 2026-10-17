import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

st.set_page_config(page_title="CoinPlus AI | Bitcoin Prediction", page_icon="₿", layout="wide")

# Load CSS
css_path = Path(__file__).parent / "style.css"
st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

# Load trained model
@st.cache_resource
def load_model():
    with open(Path(__file__).parent / "random_forest_model.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

# Heading
st.markdown("""
<div class="hero">
    <div class="hero-icon">₿</div>
    <div>
        <div class="hero-title">CoinPlus AI</div>
        <div class="hero-subtitle">Bitcoin Price Prediction</div>
    </div>
</div>
<p class="intro-text">Enter the market values below to estimate Bitcoin's closing price.</p>
<div class="section-heading">Market Input Details</div>
""", unsafe_allow_html=True)

# USDT and BNB inputs
usdt_col, bnb_col = st.columns(2, gap="large")

with usdt_col:
    st.markdown("""
    <div class="market-card usdt-card">
        <div class="market-symbol">₮</div>
        <div><div class="market-title">USDT Market Data</div>
        <div class="market-subtitle">Tether market values</div></div>
    </div>
    """, unsafe_allow_html=True)
    usdt_close = st.number_input("USDT Closing Price (USD)", min_value=0.0, value=1.0, format="%.4f")
    usdt_volume = st.number_input("USDT Trading Volume", min_value=0.0, value=0.0, format="%.2f")

with bnb_col:
    st.markdown("""
    <div class="market-card bnb-card">
        <div class="market-symbol">◆</div>
        <div><div class="market-title">BNB Market Data</div>
        <div class="market-subtitle">Binance Coin market values</div></div>
    </div>
    """, unsafe_allow_html=True)
    bnb_close = st.number_input("BNB Closing Price (USD)", min_value=0.0, value=250.0, format="%.2f")
    bnb_volume = st.number_input("BNB Trading Volume", min_value=0.0, value=0.0, format="%.2f")

if st.button("₿  Predict Bitcoin Closing Price", use_container_width=True):
    try:
        inputs = pd.DataFrame({
            "USDT_Close": [usdt_close],
            "USDT_Volume": [usdt_volume],
            "BNB_Close": [bnb_close],
            "BNB_Volume": [bnb_volume]
        })
        price = float(model.predict(inputs)[0])
        st.markdown(f"""
        <div class="result-card">
            <div class="result-eyebrow">PREDICTION RESULT</div>
            <div class="result-label">Estimated BTC Closing Price</div>
            <div class="result-price">${price:,.2f}</div>
            <div class="result-note">Estimate based on the supplied market inputs</div>
        </div>
        """, unsafe_allow_html=True)
        st.caption("This is an estimate, not a guaranteed market price.")
    except Exception as error:
        st.error(f"Prediction failed: {error}")
