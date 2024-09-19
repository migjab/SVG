from flask import Flask
from controllers.formas_controller import formas_bp
from controllers.config_controller import config_bp
from controllers.mapa_controller import mapa_bp

app = Flask(__name__)
app.secret_key = '123'
# Registra os blueprints (módulos de rotas)
app.register_blueprint(formas_bp)
app.register_blueprint(config_bp)
app.register_blueprint(mapa_bp)

if __name__ == '__main__':
    app.run(debug=True)
