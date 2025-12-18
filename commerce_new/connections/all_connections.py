import psycopg2

def postgres_local():
    host = "localhost"
    port = 5432
    database = "powder_intelligence"
    user = "postgres"
    password = "postgres"

    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=database,
            user=user,
            password=password
        )
        print("Conexão estabelecida com sucesso!")
        return conn

    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None
