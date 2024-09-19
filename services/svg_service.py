from models.forma_model import formas
from models.mapa_model import configuracao


formas_svg=()

def gerar_svg():
    svg_template = '''
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
        <rect width="100%" height="100%" fill="grey" />
        {formas_svg}
    </svg>
    '''
      
    return svg_template.format(
        width=configuracao["svg_width"],
        height=configuracao["svg_height"],
        formas_svg=formas_svg
    )

def adicionar_forma(tipo, cor):
    formas.append({"type": tipo, "color": cor})

def remover_forma():
    if formas:
        formas.pop()

def remover_todas_formas():
    formas.clear()

def atualizar_configuracao(largura, altura):
    configuracao["svg_width"] = largura
    configuracao["svg_height"] = altura

def definir_nome_projeto(nome):
    configuracao["nome_projeto"] = nome

def get_configuracao():
    return configuracao
