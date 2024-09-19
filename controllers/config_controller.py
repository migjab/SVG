from flask import Blueprint, request, redirect, url_for
from services.svg_service import atualizar_configuracao, definir_nome_projeto, gerar_svg
config_bp = Blueprint('config', __name__)

@config_bp.route('/atualizar_tamanho_svg', methods=['POST'], endpoint='atualizar_tamanho_svg_rota')
def atualizar_tamanho_svg_rota():
    largura = int(request.form.get('svgWidth', 910))
    altura = int(request.form.get('svgHeight', 800))
    atualizar_configuracao(largura, altura)
    return redirect(url_for('mapa.index'))

@config_bp.route('/definir_nome_projeto', methods=['POST'],  endpoint='definir_nome_projeto_rota')
def definir_nome_projeto_rota():
    nome_projeto = request.form.get('nomeProjeto', 'Mapa')
    definir_nome_projeto(nome_projeto)
    return redirect(url_for('mapa.index'))


@config_bp.route('/baixar_svg', methods=['POST'])
def baixar_svg():
    nome_arquivo = request.form.get('nomeArquivo', 'output.svg')
    svg_content = gerar_svg()
    return send_file(BytesIO(svg_content.encode('utf-8')), as_attachment=True, download_name=nome_arquivo, mimetype='image/svg+xml')
