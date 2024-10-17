# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from data import Post

load_dotenv()

post = Post()
blogs_data = post.data[::-1]
app = Flask(__name__)



@app.route('/')
def blogs_main():
    limit = request.args.get('limit', default=f'(0, 7)', type=str)
    limit = tuple(map(int, limit.strip('()').split(',')))
    return render_template("blogs.html", data=blogs_data, limit=limit)

@app.route('/blog/<int:post_num>')
def get_post(post_num):
    return render_template('post.html', data=blogs_data, article_no=int(post_num))


if __name__ == "__main__":
    app.run(debug=False)

