from flask import Blueprint, request, redirect, url_for
import random
from services.svg_service import adicionar_forma, remover_forma, remover_todas_formas

formas_bp = Blueprint('formas', __name__)
formas_svg =()
@formas_bp.route('/adicionar_forma', methods=['POST'])
def adicionar_forma_rota():
    forma_type = request.form.get('shape')
    cor = random.choice(["red", "green", "blue"])
    adicionar_forma(forma_type, cor)
    return redirect(url_for('mapa.index'))

@formas_bp.route('/remover_forma')
def remover_forma_rota():
    remover_forma()
    return redirect(url_for('mapa.index'))

@formas_bp.route('/remover_todas_formas')
def remover_todas_formas_rota():
    remover_todas_formas()
    return redirect(url_for('mapa.index'))
