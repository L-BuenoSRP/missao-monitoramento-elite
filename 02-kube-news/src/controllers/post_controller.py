from datetime import datetime
from models.post import Post

class PostController:
    @staticmethod
    def get_all_posts():
        """Retorna todos os posts"""
        return Post.get_all()
    
    @staticmethod
    def get_post_by_id(post_id):
        """Retorna um post específico por ID"""
        return Post.get_by_id(post_id)
    
    @staticmethod
    def validate_post_data(title, summary, content):
        """Valida os dados do post"""
        return (
            len(title) > 0 and len(title) < 30 and
            len(summary) > 0 and len(summary) < 50 and
            len(content) > 0 and len(content) < 2000
        )
    
    @staticmethod
    def create_post(title, summary, content):
        """Cria um novo post"""
        post = Post(
            title=title,
            summary=summary,
            content=content
        )
        return post.save()
    
    @staticmethod
    def create_posts_bulk(posts_data):
        """Cria múltiplos posts"""
        return Post.create_bulk(posts_data)
    
    @staticmethod
    def get_empty_post():
        """Retorna um post vazio para formulários"""
        return {
            'title': '',
            'content': '',
            'summary': ''
        } 