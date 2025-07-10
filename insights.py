import requests
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os
import dotenv
dotenv.load_dotenv("dev.env")

# --- News Fetching ---
NEWS_API_KEY = os.getenv("NEWSAPI_KEY")
if not NEWS_API_KEY:
    raise ValueError("NEWSAPI_KEY is not set. Please add it to your dev.env file.")
NEWS_API_URL = "https://newsapi.org/v2/everything"

# Fetch recent news headlines for a list of crypto symbols
def fetch_news(symbols, max_articles=5):
    headlines = []
    for symbol in symbols:
        params = {
            "q": symbol.replace("-USD", ""),
            "apiKey": NEWS_API_KEY,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": max_articles,
        }
        resp = requests.get(NEWS_API_URL, params=params)
        if resp.status_code == 200:
            articles = resp.json().get("articles", [])
            for article in articles:
                headlines.append(f"{article['title']} ({article['source']['name']})")
        else:
            headlines.append(f"No news found for {symbol}")
    return headlines

# --- AI Insights Generation ---
def generate_insight(headlines, openai_api_key=None):
    if not headlines:
        return "No news headlines available."
    prompt = PromptTemplate(
        input_variables=["headlines"],
        template="""
        Given the following recent crypto news headlines:
        {headlines}
        
        Summarize the overall sentiment and mention any important events or trends relevant to a crypto investor.
        """
    )
    llm = OpenAI(openai_api_key=openai_api_key, temperature=0.3)
    response = llm(prompt.format(headlines="\n".join(headlines)))
    return response 