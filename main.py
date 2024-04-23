def buscar_datos(*nombres_apellidos, database):
    for key, value in database.items():
        nombres_apellidos_db = []
        for k, v in value.items():
            if k.startswith("nombre") or k.startswith("apellido"):
                nombres_apellidos_db.append(v)
        
        if set(nombres_apellidos) == set(nombres_apellidos_db):
            return key
    
    return None
