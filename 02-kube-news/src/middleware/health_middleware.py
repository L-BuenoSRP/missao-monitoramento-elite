from controllers.health_controller import HealthController

# Instância global do controller de health
health_controller = HealthController()

def health_check_middleware():
    """Middleware para verificar saúde da aplicação"""
    if not health_controller.is_healthy():
        return '', 500
    return None 