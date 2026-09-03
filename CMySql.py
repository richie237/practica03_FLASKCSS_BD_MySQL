import mysql.connector
import os

def f_conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "comercio"),
        port=int(os.getenv("DB_PORT", 3306))
    )

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
        conexion.commit()  # Confirma y guarda los datos en la base de datos
        conexion.close()
    except Exception as e:
        print(f"Error al guardar registro: {e}")

def f_listar_clientes():
    try:
        conexion = f_conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes")
        registros = cursor.fetchall()
        conexion.close()
        return registros
    except Exception as e:
        print(f"Error al consultar clientes: {e}")
        return []