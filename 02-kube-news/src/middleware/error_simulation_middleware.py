import os
import random
from flask import Response, request
import json

def error_simulation_middleware():
    """
    Middleware para simular erros baseado na variável de ambiente ERROR_RATE_PERCENT.
    Retorna erro 500 baseado na porcentagem definida na variável.
    Ignora o endpoint /metrics para não afetar o monitoramento.
    """
    # Ignora a simulação de erro para o endpoint /metrics
    if request.path == '/metrics':
        return None
        
    error_rate = os.getenv('ERROR_RATE_PERCENT', '0')
    
    try:
        error_rate = float(error_rate)
        if error_rate <= 0:
            return None
            
        # Gera um número aleatório entre 0 e 100
        random_number = random.uniform(0, 100)
        
        # Se o número gerado for menor que a taxa de erro, retorna erro 500
        if random_number < error_rate:
            error_response = {
                'error': 'Error simulated by middleware',
                'error_rate': f'{error_rate}%'
            }
            return Response(
                response=json.dumps(error_response),
                status=500,
                mimetype='application/json'
            )
            
        return None
        
    except ValueError:
        # Se a variável não for um número válido, não simula erro
        return None 