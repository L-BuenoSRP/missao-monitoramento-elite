from flask import Blueprint, jsonify
from controllers.health_controller import HealthController

# Criar blueprint para rotas de health check
health_bp = Blueprint('health', __name__)

# Instância global do controller de health
health_controller = HealthController()

@health_bp.route('/health')
def health():
    """Rota de health check"""
    return jsonify(health_controller.get_health_status())

@health_bp.route('/ready')
def ready():
    """Rota de readiness check"""
    is_ready, status_code = health_controller.get_readiness_status()
    if is_ready:
        return 'Ok', status_code
    else:
        return '', status_code

@health_bp.route('/unhealth', methods=['PUT'])
def unhealth():
    """Rota para definir aplicação como não saudável"""
    health_controller.set_unhealthy()
    return 'OK'

@health_bp.route('/unreadyfor/<int:seconds>', methods=['PUT'])
def unready_for(seconds):
    """Rota para definir aplicação como não pronta por X segundos"""
    health_controller.set_unready_for_seconds(seconds)
    return 'OK' 