# Simple Webcrawler Backend Application
This is a simple webcrawler backend application
That takes in the argument /pages?=target_url to crawl a website for its links.
Returns a JSON with all the links it finds
Gets both href links and links to images.

Also includes a few simple tests to test the application and its utility functions.

## Python libraries
- beautifulsoup4
- fastapi
- uvicorn
- requests
- pytest
- httpx

## How to run
Suggestion set up virtual environment for the application. To minimize risks of python libraries conflicts.
Guide: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

Then install the python libraries mentioned above.

Now it should be possible to run the backend application.

1. Go into the backend folder
2. run ```uvicorn app:app --reload``` in terminal. It will state a localhost url you can go to.
3. There are two options
    - With the localhost url add "/pages?={url}" where you swap out the "{url}" to the url you want to crawl. Example "/pages?=example.com"
    - Go to ```http://127.0.0.1:8000``` or other link said in termnial, this will redirect you to the documentation of the this backend service. Where it is possible to test the functions, in a graphical interface. To test the crawl function use the function "/pages"


