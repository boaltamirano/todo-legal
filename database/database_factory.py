from .postgres import PostgresDB

def get_db_instance(db_type):
    
    if db_type == 'postgres':
        return PostgresDB()
    
    else:
        raise ValueError('Tipo de base de datos no soportado')