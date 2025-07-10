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

## Deployment on Streamlit Community Cloud

1. Go to https://streamlit.io/cloud and sign in with GitHub.
2. Click “New app” and select this repo and `app.py` as the main file.
3. After deploying, go to “Settings” → “Secrets” and add your API keys:

```
OPENAI_API_KEY = "your-openai-key"
NEWSAPI_KEY = "your-newsapi-key"
```

4. Save and restart the app.

---

### 4. **(Optional) Clean Up App UI**
- Make sure your app runs locally with `streamlit run app.py`.
- Check for any hardcoded paths or local file dependencies (shouldn’t be any in your case).

---

### 5. **Push All Changes to GitHub**
- Make sure your latest code and `README.md` are pushed.

---

### 6. **Ready to Deploy!**
- Go to [Streamlit Cloud](https://streamlit.io/cloud), connect your repo, and deploy.

---

**Would you like me to update your `README.md` with the deployment instructions and secrets section?**  
Or do you want to review anything else before deploying? 