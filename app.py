from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    # Simple list of posts
    posts = ['post1.html', 'post2.html']  # Add your posts here
    return render_template('index.html', posts=posts)

@app.route('/posts/<post_name>')
def post(post_name):
    return send_from_directory('posts', post_name)

if __name__ == '__main__':
    app.run(debug=True)
