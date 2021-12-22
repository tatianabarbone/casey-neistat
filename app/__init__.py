from flask import Flask, render_template
from app.vid_generator import *

app = Flask(__name__)

@app.route("/")
def homepage():

    vid = get_random_video()
    url = get_url(vid)
    title = get_title(vid)
    thumbnail = get_thumbnail(vid)

    return render_template("index.html", url=url, title=title, thumbnail=thumbnail)

if __name__ == '__main__':
    app.run(debug=True)