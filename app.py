import streamlit as st
import pandas as pd
import yfinance as yf
import os
import dotenv
dotenv.load_dotenv("dev.env")
from insights import fetch_news, generate_insight

# Sample portfolio data (coin, symbol, amount held)
portfolio_data = [
    {"coin": "Bitcoin", "symbol": "BTC-USD", "amount": 0.5},
    {"coin": "Ethereum", "symbol": "ETH-USD", "amount": 2},
    {"coin": "Solana", "symbol": "SOL-USD", "amount": 10},
]

# Convert to DataFrame
portfolio_df = pd.DataFrame(portfolio_data)

st.title("Crypto Portfolio Dashboard")
st.write("This dashboard tracks your crypto holdings and will soon provide AI-powered insights!")

st.subheader("Your Portfolio")
st.dataframe(portfolio_df)

# --- Fetch real-time prices ---
st.subheader("Current Prices and Portfolio Value")

# Helper function to fetch latest price for a symbol
def get_latest_price(symbol):
    ticker = yf.Ticker(symbol)
    # Get the most recent closing price
    price = ticker.history(period="1d")["Close"].iloc[-1]
    return price

# Fetch prices and calculate value for each holding
prices = []
values = []
for idx, row in portfolio_df.iterrows():
    price = get_latest_price(row["symbol"])
    value = price * row["amount"]
    prices.append(price)
    values.append(value)

# Add to DataFrame
portfolio_df["Current Price (USD)"] = prices
portfolio_df["Value (USD)"] = values

# Display updated portfolio
st.dataframe(portfolio_df[["coin", "amount", "Current Price (USD)", "Value (USD)"]])

# Show total portfolio value
total_value = sum(values)
st.metric("Total Portfolio Value (USD)", f"${total_value:,.2f}")

# --- End of app ---

st.subheader("AI-Powered Portfolio Insights")

# Prompt selection
prompt_type = st.selectbox(
    "Choose the type of AI insight:",
    [
        "Summarize sentiment and events",
        "Key risks and opportunities for each coin",
        "Likely short-term market movement"
    ],
    index=0
)
prompt_type_map = {
    "Summarize sentiment and events": 1,
    "Key risks and opportunities for each coin": 2,
    "Likely short-term market movement": 3
}

# Button to generate insights
if st.button("Generate AI Insight about My Portfolio"):
    # Fetch news for portfolio coins
    symbols = portfolio_df["symbol"].tolist()
    coins = portfolio_df["coin"].tolist()
    headlines = fetch_news(symbols)
    st.write("### Recent News Headlines:")
    for h in headlines:
        st.write(f"- {h}")
    # Generate AI insight using LangChain and OpenAI
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        st.error("OPENAI_API_KEY is not set. Please add it to your .env file.")
        st.stop()
    with st.spinner("Generating insight..."):
        insight = generate_insight(
            headlines,
            openai_api_key=openai_api_key,
            prompt_type=prompt_type_map[prompt_type],
            coins=coins
        )
    st.success("AI Insight:")
    st.write(insight) 