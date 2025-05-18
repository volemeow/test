import os
import socket
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = "Unknown"
    author = os.getenv("AUTHOR", "Unknown Author")

    html_content = f"""
    <html>
        <head><title>Webapp</title></head>
        <body>
            <h1>Server Info</h1>
            <p><strong>Hostname:</strong> {hostname}</p>
            <p><strong>IP Address:</strong> {ip_address}</p>
            <p><strong>Author:</strong> {author}</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    uvicorn.run("echo_server:app", host="127.0.0.1", port=8000)