from fastapi import FastAPI
from scraper import Scraper


app = FastAPI()
quotes = Scraper()

@app.get("/{cat}")
async def readData(cat):
    return quotes.scrapedData(cat)
