from openbb import obb

def get_stock_data(symbol: str):
    try:
        data = obb.equity.price.historical(symbol)
        df = data.to_dataframe()  # Convert to DataFrame
        return df.tail(5).to_dict()  # Show last 5 rows
    except Exception as e:
        print("Error:", e)
        return {"error": str(e)}

def get_stock_news(symbol: str):
    try:
        news_data = obb.equity.news(symbol)  # Fetch news data
        news_df = news_data.to_dataframe()   # Convert to DataFrame
        return news_df.head(5).to_dict(orient="records")  # Return top 5 articles as list of dictionaries
    except Exception as e:
        print("Error fetching news:", e)
        return [{"title": "No news available", "summary": "", "link": ""}]
