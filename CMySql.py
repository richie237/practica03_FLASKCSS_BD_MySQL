import mysql.connector

def f_conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="comercio"
    )

def f_agregar_registro(nombre, apellido_paterno, apellido_materno, fecha_nacimiento,
                       genero, correo, telefono, estado, ciudad, codigo_postal,
                       tipo_cliente, intereses, limite_credito, observaciones):
    try:
        conexion = f_conectar()
        cursor = conexion.cursor()
        # Aquí va tu consulta INSERT INTO ...
        # cursor.execute(sql, valores)
        # conexion.commit()
        conexion.close()
    except Exception as e:
        print(f"No se pudo conectar a MySQL remoto: {e}")

def f_listar_clientes():
    try:
        conexion = f_conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes") # Ajusta al nombre de tu tabla
        registros = cursor.fetchall()
        conexion.close()
        return registros
    except Exception as e:
        print(f"Error al listar: {e}")
        return []