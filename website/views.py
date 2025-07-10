from flask import Blueprint, render_template, request, jsonify, Response
import os, dotenv
from pantry_wrapper import get_contents
from typing import Union
import requests
import tempfile

views = Blueprint("views", __name__)

dotenv.load_dotenv()
PANTRY_ID = os.environ.get("PANTRY_ID")

def fetch_all_metadata() -> Union[dict[str, dict], None]:
    if PANTRY_ID is None:
        return
    content = get_contents(PANTRY_ID, "metadata", return_type='body')
    return content if type(content) == dict else None

@views.route("/")
def home():
    return render_template("index.html")


@views.route("/download")
def download():
    file_link = request.args.get("url")
    if not file_link:
        return Response(None, content_type="text/plain")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    query = requests.get(file_link, stream=True, headers=headers)
    
    temp = tempfile.TemporaryFile()
    temp.write(query.content)


    return Response(
            temp,
            headers={
                "Content-Disposition": 'attachment; filename="video.mp4"',
                "Content-Type": "application/octet-stream"
            }
        )



@views.route("/admin")
def admin():
    return render_template("admin.html")


@views.route("/api/get_recent")
def get_recent_func():
    data = fetch_all_metadata() 
    return jsonify({"data": data, "status_code": 200})
