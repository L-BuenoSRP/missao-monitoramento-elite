from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from controllers.post_controller import PostController

# Criar blueprint para rotas de posts
post_bp = Blueprint('posts', __name__)

@post_bp.route('/')
def index():
    """Rota principal - listagem de posts"""
    posts = PostController.get_all_posts()
    return render_template('index.html', posts=posts)

@post_bp.route('/post')
def create_post():
    """Rota para formulário de criação"""
    post = PostController.get_empty_post()
    return render_template('edit-news.html', post=post, valido=True)

@post_bp.route('/post', methods=['POST'])
def save_post():
    """Rota para processar criação de post"""
    title = request.form.get('title', '')
    summary = request.form.get('resumo', '')
    content = request.form.get('description', '')
    
    # Validação
    valid = PostController.validate_post_data(title, summary, content)
    
    if valid:
        PostController.create_post(title, summary, content)
        return redirect(url_for('posts.index'))
    else:
        post = {'title': title, 'content': content, 'summary': summary}
        return render_template('edit-news.html', post=post, valido=False)

@post_bp.route('/api/post', methods=['POST'])
def api_create_posts():
    """API para inserção em massa"""
    data = request.get_json()
    artigos = data.get('artigos', [])
    
    PostController.create_posts_bulk(artigos)
    return jsonify(artigos)

@post_bp.route('/post/<int:id>')
def view_post(id):
    """Rota para visualizar post específico"""
    post = PostController.get_post_by_id(id)
    return render_template('view-news.html', post=post) 