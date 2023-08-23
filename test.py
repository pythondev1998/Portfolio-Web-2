import os

# Valida la configuración de las variables de entorno
required_env_variables = ["GMAIL_USERNAME", "GMAIL_SENDER", "GMAIL_PASSWORD"]

for env_var in required_env_variables:
    if os.getenv(env_var) is None:
        print(f"La variable de entorno {env_var} no está configurada correctamente.")
    else:
        print(f"La variable de entorno {env_var} está configurada correctamente.")

# Luego puedes utilizar las variables de entorno en tu aplicación
GMAIL_USERNAME = os.getenv("GMAIL_USERNAME")
GMAIL_SENDER = os.getenv("GMAIL_SENDER")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
