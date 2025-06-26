import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

class DatabaseConfig:
    @staticmethod
    def get_database_uri():
        return (
            f"postgresql://{os.getenv('DB_USERNAME', 'kubedevnews')}:"
            f"{os.getenv('DB_PASSWORD', 'Pg#123')}@"
            f"{os.getenv('DB_HOST', 'localhost')}:"
            f"{os.getenv('DB_PORT', '5432')}/"
            f"{os.getenv('DB_DATABASE', 'kubedevnews')}"
        )
    
    @staticmethod
    def get_config():
        return {
            'SQLALCHEMY_DATABASE_URI': DatabaseConfig.get_database_uri(),
            'SQLALCHEMY_TRACK_MODIFICATIONS': False
        } 