import secrets
secret_key = secrets.token_hex(32)

class DevelopmentConfig:
    endpoint = 'db.oljlqfiyjvrhxbglskta.supabase.co'
    username = 'postgres'
    password = 'BT7274DEPLOY'
    database_name = 'postgres'
    port = '5432'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{username}:{password}@{endpoint}:{port}/{database_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_hex(32)

    
config = DevelopmentConfig()