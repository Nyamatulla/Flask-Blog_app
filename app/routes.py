# app/routes.py
from flask import render_template
from app import app

class BlogPost:
    def __init__(self, post_id, title, content):
        self.id = post_id
        self.title = title
        self.content = content

# Sample blog posts
posts = [
    BlogPost(1, 'Introduction to AWS', 'AWS is a cloud computing platform...'),
    BlogPost(2, 'EC2 Instances', 'Amazon EC2 provides scalable computing...'),
    BlogPost(3, 'S3 Storage', 'Amazon S3 is object storage built to store and retrieve...'),
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    post = next((p for p in posts if p.id == post_id), None)
    if post:
        return render_template('blog_post.html', post=post)
    else:
        return 'Post not found', 404
