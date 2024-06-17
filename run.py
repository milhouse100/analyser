import os
from dotenv import load_dotenv
from app import create_app

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

app = create_app()
port = os.getenv("PORT")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
