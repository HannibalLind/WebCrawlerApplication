from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse, RedirectResponse

from crawler.crawler import crawl_website

router = APIRouter()

@router.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

@router.get("/pages")
async def crawl_pages(target: str = Query(..., description="The URL to crawl")):
    pages = await crawl_website(target)
    return JSONResponse(content={
        "domain": f"{target}",
        "pages" : pages
    })