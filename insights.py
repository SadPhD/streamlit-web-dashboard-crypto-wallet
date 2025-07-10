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
def generate_insight(headlines, openai_api_key=None, prompt_type=1, coins=None):
    if not headlines:
        return "No news headlines available."
    if coins is None:
        coins = []
    coin_list = ', '.join(coins)
    if prompt_type == 1:
        prompt = PromptTemplate(
            input_variables=["headlines"],
            template="""
            Given the following recent crypto news headlines:
            {headlines}
            
            Summarize the overall sentiment and mention any important events or trends relevant to a crypto investor.
            """
        )
    elif prompt_type == 2:
        prompt = PromptTemplate(
            input_variables=["headlines", "coins"],
            template="""
            Analyze these news headlines for the following coins: {coins}.
            What are the key risks and opportunities for each coin based on the latest news?
            Headlines:
            {headlines}
            """
        )
    elif prompt_type == 3:
        prompt = PromptTemplate(
            input_variables=["headlines", "coins"],
            template="""
            Based on the news below, what is the likely short-term market movement for the following cryptocurrencies: {coins}?
            Provide reasoning for your prediction.
            Headlines:
            {headlines}
            """
        )
    else:
        return "Invalid prompt type."
    llm = OpenAI(openai_api_key=openai_api_key, temperature=0.3)
    if prompt_type == 1:
        response = llm(prompt.format(headlines="\n".join(headlines)))
    else:
        response = llm(prompt.format(headlines="\n".join(headlines), coins=coin_list))
    return response 