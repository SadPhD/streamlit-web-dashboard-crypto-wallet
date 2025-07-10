# Streamlit Crypto Portfolio Dashboard with AI Insights

This project is a Streamlit web dashboard that tracks your crypto portfolio's performance and uses LangChain to generate AI-powered insights based on recent news and market data.

## Features
- Track your crypto holdings and performance in real time
- Fetch latest prices and news for your coins
- Get AI-generated insights about your portfolio using LangChain and LLMs

## Quickstart
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   streamlit run app.py
   ```
3. Add your OpenAI API key as an environment variable if you want to use GPT-based insights:
   ```bash
   export OPENAI_API_KEY=your-key-here
   ```

## Project Structure
- `app.py` - Main Streamlit app
- `portfolio.py` - Portfolio logic
- `insights.py` - AI-powered insights
- `utils.py` - Helper functions
- `data/` - (Optional) Static/sample data

---

Built with [Streamlit](https://streamlit.io/) and [LangChain](https://langchain.com/). 