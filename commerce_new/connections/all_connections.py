import psycopg2

def postgres_local():
    host = "localhost"
    port = 5432
    database = "powder_intelligence"
    user = "postgres"
    password = "postgres2"

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


def postgres_prd():
    host = "35.247.250.163"
    port = 5432
    database = "powder_intelligence"
    user = "postgres"
    password = "vS@L_iAUgHJa^[8-"

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