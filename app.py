from flask import Flask, jsonify

app = Flask(__name__)

# Dummy data for forum posts
posts_data = [
    {"id": 1, "title": "First Post", "content": "Welcome to the engineering internship!"},
    {"id": 2, "title": "Git Basics", "content": "Keep everything in one folder and commit often."},
    {"id": 3, "title": "Flask API", "content": "This is a simple REST API endpoint."}
]

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)