from flask import Flask
from config.database import DatabaseConfig
from models.post import db
from views.post_routes import post_bp
from views.health_routes import health_bp
from middleware.health_middleware import health_check_middleware
from middleware.error_simulation_middleware import error_simulation_middleware
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics

def create_app():
    """Factory function para criar a aplicação Flask"""
    app = Flask(__name__)

    metrics = GunicornPrometheusMetrics(app)
    metrics.register_endpoint('/metrics')

    
    # Configuração do banco de dados
    app.config.update(DatabaseConfig.get_config())
    
    # Inicializar extensões
    db.init_app(app)
    
    # Registrar blueprints
    app.register_blueprint(post_bp)
    app.register_blueprint(health_bp)
    
    # Registrar middleware
    app.before_request(error_simulation_middleware)  # Registra primeiro o middleware de simulação de erros
    app.before_request(health_check_middleware)      # Depois o middleware de health check
    
    return app

def init_database(app):
    """Inicializa o banco de dados"""
    with app.app_context():
        db.create_all()
        print('Banco de dados inicializado')

# Criar aplicação
app = create_app()

# Inicializar banco de dados
init_database(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
    print('Aplicação rodando na porta 5000') 