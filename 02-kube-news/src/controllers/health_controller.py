import socket
from datetime import datetime, timedelta

class HealthController:
    def __init__(self):
        self.is_health = True
        self.read_time = datetime.now()
    
    def get_health_status(self):
        """Retorna o status de saúde da aplicação"""
        return {
            'state': 'up',
            'machine': socket.gethostname()
        }
    
    def get_readiness_status(self):
        """Verifica se a aplicação está pronta"""
        if self.read_time < datetime.now():
            return True, 200
        else:
            return False, 500
    
    def set_unhealthy(self):
        """Define a aplicação como não saudável"""
        self.is_health = False
    
    def set_unready_for_seconds(self, seconds):
        """Define a aplicação como não pronta por X segundos"""
        self.read_time = datetime.now() + timedelta(seconds=seconds)
    
    def is_healthy(self):
        """Verifica se a aplicação está saudável"""
        return self.is_health 