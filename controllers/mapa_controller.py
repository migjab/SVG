from flask import Blueprint, render_template, send_file, request, session , redirect, url_for
from io import BytesIO
from services.svg_service import gerar_svg, get_configuracao

mapa_bp = Blueprint('mapa', __name__)

setores = []
@mapa_bp.route('/')
def index():
    svg_content = renderizar_svg()  # Função para gerar o conteúdo do SVG
    return render_template('index.html', svg_content=svg_content, setores=setores)

@mapa_bp.route('/adicionar_setor', methods=['POST'])
def adicionar_setor():
    nome_setor = request.form['nomeSetor']
    nome_classe = request.form['nomeClasse']
    nome_ingresso = request.form['nomeIngresso']
    cor_setor = request.form['corSetor']

    # Criação do setor com os dados fornecidos
    setor = {
        'nome_setor': nome_setor,
        'nome_classe': nome_classe,
        'nome_ingresso': nome_ingresso,
        'cor_setor': cor_setor
    }
    setores.append(setor)
    
    return redirect(url_for('mapa.index'))

@mapa_bp.route('/remover_setor', methods=['POST'])
def remover_setor():
    if setores:
        setores.pop()  # Remove o último setor
    return redirect(url_for('mapa.index'))

def renderizar_svg():
    # Lógica para gerar o SVG com os setores e formas
    svg_output = "<svg width='910' height='800'>"  # Exemplo de SVG
    for setor in setores:
        svg_output += f"<rect width='100' height='100' fill='{setor['cor_setor']}'></rect>"
    svg_output += "</svg>"
    return svg_output

