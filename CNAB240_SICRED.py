from typing import TypedDict
from typing import cast
import requests

class CepInfo(TypedDict):
    cep : str
    logradouro : str
    complemento : str
    unidade : str
    bairro : str
    localidade : str
    uf : str
    estado : str
    regiao : str
    ibge : str
    gia : str
    ddd : str
    siafi : str

def get_info_from_cep(cep : str) -> CepInfo:

    # region FUNCTION DESCRIPTION
    """
    Consulta a API ViaCEP e retorna informações do endereço.

    Retorna:
        CepInfo: Dicionário com os seguintes campos:
            - cep (str)
            - logradouro (str)
            - complemento (str)
            - unidade (str)
            - bairro (str)
            - localidade (str)
            - uf (str)
            - estado (str)
            - regiao (str)
            - ibge (str)
            - gia (str)
            - ddd (str)
            - siafi (str)
    """
    # endregion

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url).json()
    return cast(CepInfo, response)

def shorten_logradouro(logradouro : str) -> str:
    short_logradouros = {
        "1ª Avenida": "1ª Av",
        "1ª Travessa": "1ª Tv",
        "Avenida": "Av",
        "Conjunto": "Cj",
        "Complexo Viário": "Cmp Vr",
        "Praça": "Pç",
        "Rua": "R",
        "Viela": "Vla",
        "Terminal": "Ter",
        "Quadra": "Q",
        "Aeroporto": "Aer",
        "Estrada Municipal": "Est Mun",
        "Setor": "St",
        "2ª Travessa": "2ª Tv",
        "Estrada": "Est",
        "Estrada Velha": "Est Velha",
        "Largo": "Lrg",
        "Escadaria": "Escad",
        "Estrada Vicinal": "Est Vic",
        "Rodovia": "Rod",
        "3ª Travessa": "3ª Tv",
        "Jardinete": "Jde",
        "Passagem": "Psg",
        "Condomínio": "Cond",
        "Travessa": "Tv",
        "Condomínio Residencial": "Cond Res",
        "Passagem de Pedestres": "Psg Ped",
        "Avenida Perimetral": "Av Per",
        "Blocos": "Bls",
        "Alameda": "Al",
        "Travessa Particular": "Tv Part",
        "Servidão": "Srv",
        "Comunidade": "Com",
        "Caminho": "Cam",
        "Vila": "Vl",
        "4ª Travessa": "4ª Tv",
        "Acesso": "Ac",
        "Avenida Marginal": "Av Marg",
        "Trevo": "Trv",
        "Beco": "Bc",
        "Núcleo Rural": "Nuc Rural",
        "Ladeira": "Ld",
        "Prolongamento": "Prl",
        "Via de Pedestre": "V Ped",
        "Caminho de Servidão": "Cam Serv",
        "Servidão de Passagem": "Srv Psg",
        "Loteamento": "Lot",
        "Via": "V",
        "Ramal": "Ram",
        "Calçadão": "Calç",
        "Colônia": "Col",
        "6ª Travessa": "6ª Tv",
        "Parque": "Prq",
        "1ª Paralela": "1ª Par",
        "3ª Avenida": "3ª Av",
        "7ª Travessa": "7ª Tv",
        "2ª Avenida": "2ª Av",
        "5ª Travessa": "5ª Tv",
        "8ª Travessa": "8ª Tv",
        "9ª Travessa": "9ª Tv",
        "Avenida Marginal Norte": "Av Marg Norte",
        "Viaduto": "Vd",
        "2ª Rua": "2ª R",
        "Via de Acesso": "V Ac",
        "Via Local": "V Local",
        "Via Marginal": "V Marg",
        "Conjunto Residencial": "Cj Res",
        "Entrada Particular": "Ent Part",
        "Rampa": "Rmp",
        "11ª Travessa": "11ª Tv",
        "12ª Travessa": "12ª Tv",
        "Boulevard": "Bvd",
        "Estrada Antiga": "Est Ant",
        "Rodovia Municipal": "Rod Mun",
        "Ponte": "Pte",
        "Beco 2": "Bc 2",
        "Monte": "Mte",
        "Passeio": "Pas",
        "Rua Particular": "R Part",
        "4ª Avenida": "4ª Av",
        "Alça de Acesso": "Alc Aces",
        "Corredor": "Cor",
        "10ª Travessa": "10ª Tv",
        "Beco 3": "Bc 3",
        "Beco 1": "Bc 1",
        "Contorno": "Cont",
        "Estrada de Servidão": "Est Srv",
        "Avenida Marginal Esquerda": "Av Marg Esq",
        "Estrada Particular": "Est Part",
        "Favela": "Fav",
        "Rua Projetada": "R Proj",
        "Ruela": "Rla",
        "Via Costeira": "V Cost",
        "2ª Paralela": "2ª Par",
        "Paralela": "Par",
        "3º Alto": "3º At",
        "Anel Viário": "An Vr",
        "Recanto": "Rec",
        "Galeria": "Gal",
        "Residencial": "Res",
        "4ª Paralela": "4ª Par",
        "Parque Municipal": "Prq Munic",
        "Via Lateral": "V Lat",
        "Bloco": "Bl",
        "Estrada Vicinal Municipal": "Est Vic Mun",
        "Lagoa": "Lga",
        "3ª Rua": "3ª R",
        "Avenida Marginal Direita": "Av Marg Dir",
        "Chácara": "Ch",
        "Conjunto Habitacional": "Cj Hab",
        "4ª Rua": "4ª R",
        "Estrada Estadual": "Est Estd",
        "Rua de Ligação": "R Lig",
        "13ª Travessa": "13ª Tv",
        "Baixa": "Bx",
        "Rotatória": "Rtt",
        "5ª Avenida": "5ª Av",
        "Lago": "Lg",
        "Mercado": "Merc",
        "1ª Vila": "1ª Vl",
        "Praia": "Pr",
        "Ilha": "Ia",
        "Passarela": "Psa",
        "3ª Paralela": "3ª Par",
        "3ª Vila": "3ª Vl",
        "Terceira Avenida": "Terc Av",
        "Córrego": "Crg",
        "Jardim": "Jd",
        "16ª Travessa": "16ª Tv",
        "5ª Vila": "5ª Vl",
        "Adro": "Ad",
        "Estrada Intermunicipal": "Est Interm",
        "Marginal": "Marg",
        "Porto": "Pto",
        "Subida": "Sub",
        "Via Expressa": "V Exp",
        "1ª Subida": "1ª Sub",
        "2ª Subida": "2ª Sub",
        "Retorno": "Rtn",
        "Trincheira": "Tch",
        "2ª Vila": "2ª Vl",
        "Vereda": "Ver",
        "17ª Travessa": "17ª Tv",
        "Acampamento": "Acamp",
        "2º Beco": "2º Bc",
        "4ª Vila": "4ª Vl",
        "Escada": "Esc",
        "Escada de Pedra": "Esc Pedra",
        "1ª Rua": "1ª R",
        "Antiga Estrada": "Ant Est",
        "Canal": "Can",
        "1ª Travessa da Rodovia": "1ª Tv da",
        "Estrada Ecoturística": "Est Ecot",
        "Rua Principal": "R Princ",
        "Jardim Residencial": "Jd Res",
        "Margem": "Mrg",
        "15ª Travessa": "15ª Tv",
        "Elevada": "Evd",
        "Granja": "Gja",
        "Parada": "Pda",
        "14ª Travessa": "14ª Tv",
        "Alto": "At",
        "Campo": "Cpo",
        "26ª Travessa": "26ª Tv",
        "Estrada de Ferro": "Est Fer",
        "Circular": "Circ",
        "Eixo Industrial": "Ex Ind",
        "Sítio": "Sit",
        "6ª Vila": "6ª Vl",
        "Rua Velha": "R Velha",
        "2ª Ladeira": "2ª Ld",
        "Via Coletora": "V Colet",
        "3ª Ladeira": "3ª Ld",
        "Morro": "Mro",
        "Passagem Subterrânea": "Psg Sub",
        "Pista Lateral": "Pta Lat",
        "Unidade": "Unid",
        "Bosque": "Bsq",
        "3ª Subida": "3ª Sub",
        "Estádio": "Etd",
        "19ª Travessa": "19ª Tv",
        "20ª Travessa": "20ª Tv",
        "Balão": "Blo",
        "Variante": "Vrte",
        "22ª Travessa": "22ª Tv",
        "5ª Rua": "5ª R",
        "6ª Avenida": "6ª Av",
        "21ª Travessa": "21ª Tv",
        "Esplanada": "Esp",
        "Fazenda": "Faz",
        "18ª Travessa": "18ª Tv",
        "Feira": "Fra",
        "Rua Vicinal": "R Vic",
        "2ª Travessa da Rodovia": "2ª Tv Rod",
        "4ª Subida": "4ª Sub",
        "Colina": "Clna",
        "Ciclovia": "Cicl",
        "Orla Fluvial": "Or Fl",
        "Zigue-Zague": "Zig-Zag",
        "2º Alto": "2º At",
        "1º Alto": "1º At",
        "Descida": "Dsc",
        "Estrada de Ligação": "Est Lig",
        "5ª Subida": "5ª Sub",
        "Avenida Contorno": "Av Cont",
        "Parque Residencial": "Prq Res",
        "Belvedere": "Belv",
        "Distrito": "Dt",
        "Acesso Local": "Ac Loc",
        "Estacionamento": "Estc",
        "Variante da Estrada": "Vrte Est",
        "Praça de Esportes": "Pç Esp",
        "Via Litorânea": "V Lit",
        "Outeiro": "Out",
        "6ª Subida": "6ª Sub",
        "6ª Rua": "6ª R",
        "Acesso Estadual": "Ac Estd",
        "1º Beco": "1º Bc",
        "Estrada Nova": "Est Nv",
        "1ª Ladeira": "1ª Ld",
        "Vale": "Vle",
        "Rua de Pedestre": "R Ped",
        "Trecho": "Tr",
        "Vala": "Val",
        "7ª Avenida": "7ª Av",
        "Cais": "C",
        "10ª Avenida": "10ª Av",
        "11ª Avenida": "11ª Av",
        "Eixo": "Ex",
        "8ª Avenida": "8ª Av",
        "Bulevar": "Blv",
        "Reta": "Ret",
        "Ponta": "Pta",
        "Via de Pedestres": "V Peds",
        "Fonte": "Fnt",
        "3º Beco": "3º Bc",
        "9ª Avenida": "9ª Av",
        "Quinta": "Qta",
        "Desvio": "Dsv",
        "Atalho": "Atl",
        "Buraco": "Bco",
        "Eixo Principal": "Ex Princ",
        "Gleba": "Glb",
        "Módulo": "Mod",
        "Artéria": "Art",
        "Forte": "Fte"
    }

    shortened_logradouro = ""
    for word in logradouro.split():
        shortened_logradouro += " "
        if word in short_logradouros.keys():
            shortened_logradouro += short_logradouros[word]
            continue
        shortened_logradouro += word

    return shortened_logradouro

logradouro = get_info_from_cep("71615290")["logradouro"]
print(logradouro)
print(shorten_logradouro(logradouro))