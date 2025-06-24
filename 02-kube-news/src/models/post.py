from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'Post'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    summary = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    publishDate = db.Column(db.Date, nullable=False)
    
    def __init__(self, title, summary, content, publish_date=None):
        self.title = title
        self.summary = summary
        self.content = content
        self.publishDate = publish_date or datetime.now().date()
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'summary': self.summary,
            'content': self.content,
            'publishDate': self.publishDate.isoformat() if self.publishDate else None
        }
    
    @staticmethod
    def get_all():
        return Post.query.all()
    
    @staticmethod
    def get_by_id(post_id):
        return Post.query.get_or_404(post_id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @staticmethod
    def create_bulk(posts_data):
        posts = []
        for post_data in posts_data:
            post = Post(
                title=post_data['title'],
                summary=post_data['resumo'],
                content=post_data['description']
            )
            posts.append(post)
        
        db.session.add_all(posts)
        db.session.commit()
        return posts 