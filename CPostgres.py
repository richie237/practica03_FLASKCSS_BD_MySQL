import psycopg2
import os

def f_conectar():
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        return psycopg2.connect(database_url)
    else:
        return psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "postgres"),
            dbname=os.getenv("DB_NAME", "comercio"),
            port=int(os.getenv("DB_PORT", 5432))
        )

def f_crear_tabla():
    try:
        conexion = f_conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100),
                apellido_paterno VARCHAR(100),
                apellido_materno VARCHAR(100),
                fecha_nacimiento DATE,
                genero VARCHAR(20),
                correo VARCHAR(100),
                telefono VARCHAR(20),
                estado VARCHAR(50),
                ciudad VARCHAR(50),
                codigo_postal VARCHAR(10),
                tipo_cliente VARCHAR(50),
                intereses TEXT,
                limite_credito NUMERIC(10,2),
                observaciones TEXT
            );
        """)
        conexion.commit()
        conexion.close()
    except Exception as e:
        print(f"Error creando tabla: {e}")

f_crear_tabla()

def f_agregar_registro(nombre, apellido_paterno, apellido_materno, fecha_nacimiento,
                       genero, correo, telefono, estado, ciudad, codigo_postal,
                       tipo_cliente, intereses, limite_credito, observaciones):
    try:
        conexion = f_conectar()
        cursor = conexion.cursor()
        sql = """
            INSERT INTO clientes (
                nombre, apellido_paterno, apellido_materno, fecha_nacimiento,
                genero, correo, telefono, estado, ciudad, codigo_postal,
                tipo_cliente, intereses, limite_credito, observaciones
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (
            nombre, apellido_paterno, apellido_materno, fecha_nacimiento,
            genero, correo, telefono, estado, ciudad, codigo_postal,
            tipo_cliente, intereses, limite_credito, observaciones
        )
        cursor.execute(sql, valores)
        conexion.commit()
        conexion.close()
    except Exception as e:
        print(f"Error al guardar registro en Postgres: {e}")

def f_listar_clientes():
    try:
        conexion = f_conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes ORDER BY id ASC")
        registros = cursor.fetchall()
        conexion.close()
        return registros
    except Exception as e:
        print(f"Error al consultar en Postgres: {e}")
        return []