from werkzeug.security import generate_password_hash

hashed_password = generate_password_hash("yare123")
print(hashed_password)  # Úsalo en la consulta SQL