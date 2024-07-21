from psycopg_pool import ConnectionPool, AsyncConnectionPool

DATABASE_URL = "postgresql://user:password@localhost:5432/test1-db"


pool = None


def init_db():
    global pool
    pool = ConnectionPool(DATABASE_URL, min_size=1, max_size=10)


def get_connection():
    with pool.connection() as conn:
        return conn
