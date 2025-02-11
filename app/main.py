from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.openbb_agent import get_stock_data, get_stock_news

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/stock", response_class=HTMLResponse)  # ✅ Fixed Route
def get_stock(request: Request, symbol: str):
    data = get_stock_data(symbol)
    news = get_stock_news(symbol)
    return templates.TemplateResponse("index.html", {"request": request, "symbol": symbol, "data": data, "news": news})
