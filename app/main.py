from fastapi.responses import HTMLResponse
from app_factory import create_app
from app.services.ORCID_email import ORCIDEmailService

from app_factory import create_app
import requests
import json

app = create_app()


@app.get('/', response_class=HTMLResponse)
def root():
    # return ORCIDEmailService.GetCredentialsFromORCID("0000-0003-0431-6101")
    return """
        <html>
            <head>
                <title> ORKG Email extraction API</title>
            </head>
            <body>
                Welcome to the Open Research Knowledge Graph NLP API
                <img src="https://orkg.org/og_image.png" alt="Simply Easy Learning" width="200" height="80">
            </body>
        </html>
        """
