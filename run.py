from app import create_app
from app.routes import mail

app = create_app()
mail.init_app(app)

if __name__ == "__main__":
    # Local development settings
    app.run(host='0.0.0.0', port=5000, debug=True)