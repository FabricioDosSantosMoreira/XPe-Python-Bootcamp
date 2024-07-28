from typing import Union

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from util.generics import categorize_contents


def visualizar_tamanho_dataset(*, df: pd.DataFrame) -> None:
    linhas, colunas = df.shape

    print(f"\nO DataFrame possui {linhas} linhas e {colunas} colunas")


def visualizar_media_coluna(*, df: pd.DataFrame, coluna: str) -> None:

    # OBS: Valores originais da coluna em m/s
    if coluna.lower() == "windspeed":
        # OBS: Valores do enunciado do desafio
        x_min = 0
        x_max = 67
        
        # Inicializa o MinMaxScaler com o intervalo desejado (0 a 67)
        scaler = MinMaxScaler(feature_range=(x_min, x_max))
        # Normaliza os valores da coluna
        dados_normalizados = scaler.fit_transform(df[["windspeed"]])
        # Calcula a média dos valores normalizados
        media_normalizada = dados_normalizados.mean()

        print(f"\nA média da coluna windspeed é: {round(media_normalizada, 2)}m/s")

    # Valores originais em Graus Celsius
    elif coluna.lower() == "temp":
        # OBS: Valores do enunciado do desafio
        x_max = 39
        x_min = -8

        # Inicializa o MinMaxScaler com o intervalo desejado (0 a 67)
        scaler = MinMaxScaler(feature_range=(x_min, x_max))
        # Normaliza os valores da coluna
        dados_normalizados = scaler.fit_transform(df[["temp"]])
        # Calcula a média dos valores normalizados
        media_normalizada = dados_normalizados.mean()
        
        print(f"\nA média da coluna temp é: {round(media_normalizada, 2)}°C")


def visualizar_qtd_registros(*, df: pd.DataFrame, ano: str) -> None:
    indice_ano: int = obter_indice_ano(ano)

    if indice_ano is not None:
        registros = df[df["year"] == indice_ano]["registered"]
        qtd_registros: int = registros.count()

        print(f"\nExistem {qtd_registros} registros em {ano}")


def visualizar_qtd_locacoes(*, df: pd.DataFrame, ano: str) -> None:
    indice_ano: int = obter_indice_ano(ano)

    if indice_ano is not None:
        # Obtem as locações de usuários registrados e casuais
        registrados = df[df["year"] == indice_ano]["registered"]
        casual = df[df["year"] == indice_ano]["casual"]

        soma_locacoes_registrados = registrados.sum()
        locacoes_registrados = "{:,}".format(soma_locacoes_registrados).replace(",", ".")

        soma_locacoes_casuais = casual.sum()
        locacoes_casuais = "{:,}".format(soma_locacoes_casuais).replace(",", ".")

        total_locacoes = soma_locacoes_registrados + soma_locacoes_casuais
        total = "{:,}".format(total_locacoes).replace(",", ".")

        print(f"\nA quantidade de locações de usuários casuais é: {locacoes_casuais}")
        print(f"A quantidade de locações de usuários registrados é: {locacoes_registrados}")
        print(f"A quantidade total de locações é: {total}")


def visualizar_locacoes_e_registros_das_estacoes(*, app, df: pd.DataFrame) -> None:

    inverno = df[df['season'] == 1]['total_count']
    inverno_max, inverno_sum = inverno.agg(["max", "sum"])

    primavera = df[df['season'] == 2]['total_count']
    primavera_max, primavera_sum = primavera.agg(["max", "sum"])

    verao = df[df['season'] == 3]['total_count']
    verao_max, verao_sum = verao.agg(["max", "sum"])

    outono = df[df['season'] == 4]['total_count']
    outono_max, outono_sum = outono.agg(["max", "sum"])

    inverno_sum = "{:,}".format(inverno_sum).replace(",", ".")
    primavera_sum = "{:,}".format(primavera_sum).replace(",", ".")
    verao_sum = "{:,}".format(verao_sum).replace(",", ".")
    outono_sum = "{:,}".format(outono_sum).replace(",", ".")


    headers = ["ESTAÇÃO", "MAIOR QTD LOCAÇÕES EM UM DIA", "TOTAL DE LOCAÇÕES"]
    contents = categorize_contents(
        contents=[
            [str(inverno_max), str(inverno_sum)],
            [str(primavera_max), str(primavera_sum)],
            [str(verao_max), str(verao_sum)],
            [str(outono_max), str(outono_sum)]
        ], 
        identifiers=[
            "Inverno", "Primavera", "Verão", "Outono"
        ])

    print("\n")
    app.interface_handler.display_interface(headers=headers, contents=contents)


def visualizar_maior_e_menor_media_por_estacao(*, df: pd.DataFrame) -> None:

    estacoes = {
        1: 'Inverno',
        2: 'Primavera',
        3: 'Verão',
        4: 'Outono'
    }

    media_locacoes_por_estacao = df.groupby('season')['total_count'].mean()

    # Retorna o índice da estação com maior e menor média
    estacao_maior_media = media_locacoes_por_estacao.idxmax()
    estacao_menor_media = media_locacoes_por_estacao.idxmin()

    print (f"\nA estação com a maior média de locações é: {estacoes[estacao_maior_media]}")
    print (f"A estação com a menor média de locações é: {estacoes[estacao_menor_media]}")
    

def visualizar_maior_e_menor_media_por_horario(*, df: pd.DataFrame) -> None:

    media_locacoes_por_horario = df.groupby('hour')['total_count'].mean()

    horario_maior_media = media_locacoes_por_horario.idxmax()
    horario_menor_media = media_locacoes_por_horario.idxmin()

    print (f"\nO horário com a maior média de locações é: {horario_maior_media}hora(s)")
    print (f"O horário com a menor média de locações é: {horario_menor_media}hora(s)")
            
    
def visualizar_medias_de_locacoes_por_dia(*, app, df: pd.DataFrame) -> None:

    dias_da_semana = {
        0: 'Domingo',
        1: 'Segunda-feira',
        2: 'Terça-feira',
        3: 'Quarta-feira',
        4: 'Quinta-feira',
        5: 'Sexta-feira',
        6: 'Sábado'
    }

    media_locacoes_por_dia = df.groupby('weekday')['total_count'].mean().values

    headers = ["DIA DA SEMANA", "MÉDIA DE LOCAÇÕES"]
    contents = categorize_contents(
        contents=media_locacoes_por_dia.round(2), 
        identifiers=list(dias_da_semana.values())
        )
    
    print("\n")
    app.interface_handler.display_interface(headers=headers, contents=contents)


def visualizar_medias_de_locacoes_por_horarios_de_um_dia(*, app, df: pd.DataFrame) -> None:

    dias_da_semana = {
        0: 'Domingo',
        1: 'Segunda-feira',
        2: 'Terça-feira',
        3: 'Quarta-feira',
        4: 'Quinta-feira',
        5: 'Sexta-feira',
        6: 'Sábado'
    }

    headers = ["OPÇÃO", "DIA DA SEMANA"]
    contents = categorize_contents(contents=list(dias_da_semana.values()))

    dia_da_semana: int = app.interface_handler.display_and_select(headers=headers, contents=contents)
    indice_dia_da_semana = int(dia_da_semana) - 1

    df_dia_da_semana = df[df["weekday"] == indice_dia_da_semana]
    media_dos_horarios = df_dia_da_semana.groupby("hour")["total_count"].mean()

    headers = ["HORÁRIO", "MÉDIA DE LOCAÇÕES"]
    contents = categorize_contents(
        contents=media_dos_horarios.values.round(2), 
        identifiers=media_dos_horarios.index.astype(str).to_list()
        )

    print("\n")
    app.interface_handler.display_interface(headers=headers, contents=contents)


def obter_indice_ano(ano: str) -> Union[int, None]:
    indice: int = None

    if ano == "2011":
        indice = 0 # ano 2011
    elif ano == "2012":
        indice = 1 # ano 2012
    
    return indice
