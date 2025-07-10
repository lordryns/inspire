from flask import Blueprint, render_template, request, jsonify, Response
import os, dotenv
from pantry_wrapper import get_contents
from typing import Union
import requests

views = Blueprint("views", __name__)

dotenv.load_dotenv()
PANTRY_ID = os.environ.get("PANTRY_ID")

def fetch_all_metadata() -> Union[dict[str, dict], None]:
    content = get_contents(PANTRY_ID, "metadata", return_type='body')
    return content if type(content) == dict else None

@views.route("/")
def home():
    content = fetch_all_metadata()
    
    return render_template("index.html", all_metadata=content)


@views.route("/download")
def download():
    file_link = request.args.get("url")
    if not file_link:
        return Response(None, type="text/plain")

    query = requests.get(file_link, stream=True)

    return Response(
            query.iter_content(chunk_size=8192),
            headers={
                "Content-Disposition": 'attachment; filename="video.mp4"',
                "Content-Type": "application/octet-stream"
            }
        )