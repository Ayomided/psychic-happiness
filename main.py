from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/index")
def send_message():
    html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>HTML Response</title>
        </head>
        <body>
            <h1>Hello, HTMX!</h1>
            <p>This is HTML content not returned from FastAPI.</p>
        </body>
        </html>
        """
    return HTMLResponse(content=html_content, status_code=200)
