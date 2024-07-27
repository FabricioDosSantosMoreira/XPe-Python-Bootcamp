from util.generics import categorize_contents
from logic import logic

class Interface():

    def __init__(self, app) -> None:
        from main import Main
        
        self.app: Main = app


    def quit(self) -> None:
        self.app.quit()


    def menu(self) -> None:
        while True:
            print("\n", end='')

            self.app.interface_handler.display_msg_box(msg=self.app.CSV_NAME)

            headers = ["OPTIONS", "MENU"]
            contents = categorize_contents(
                contents=[
                    "Visualizar o tamanho do dataset", 
                    "Visualizar a média de uma coluna", 
                    "Visualizar a quantidade de registros",
                    "Visualizar a quantidade de locações",
                    "Visualizar locações de cada estação",
                    "Visualizar a estação com menor e maior média de locações",
                    "Visualizar o horário com menor e maior média de locações",
                    "Visualizar o dia da semana com menor e maior média de locações",
                    "Visualizar as médias de locações por horários de um dia da semana",
                    "Sair"
                ]
            )

            option = self.app.interface_handler.display_and_select(
                headers=headers, 
                contents=contents
            )
            match int(option):
                case 1:
                    logic.visualizar_tamanho_dataset(df=self.app.df)
                
                    continue
                case 2:
                    headers = ["OPTIONS", "COLUNA"]
                    contents = categorize_contents(contents=["windspeed", "temp"])

                    coluna: str = self.app.interface_handler.display_and_select(
                        headers=headers, 
                        contents=contents, 
                        index=1
                    )

                    logic.visualizar_media_coluna(df=self.app.df, coluna=coluna)
                    
                    continue
                case 3:
                    headers = ["OPTIONS", "ANO"]
                    contents = categorize_contents(contents=["2011", "2012"])

                    ano: str = self.app.interface_handler.display_and_select(
                        headers=headers, 
                        contents=contents, 
                        index=1
                    )

                    logic.visualizar_qtd_registros(df=self.app.df, ano=ano)

                    continue
                case 4:
                    headers = ["OPTIONS", "ANO"]
                    contents = categorize_contents(contents=["2011", "2012"])

                    ano: str = self.app.interface_handler.display_and_select(
                        headers=headers, 
                        contents=contents, 
                        index=1
                    )

                    logic.visualizar_qtd_locacoes(df=self.app.df, ano=ano)

                    continue
                case 5:

                    logic.visualizar_locacoes_e_registros_das_estacoes(app=self.app, df=self.app.df)

                    continue
                case 6:

                    logic.visualizar_maior_e_menor_media_por_estacao(df=self.app.df)

                    continue
                case 7:

                    logic.visualizar_maior_e_menor_media_por_horario(df=self.app.df)

                    continue
                case 8:

                    logic.visualizar_medias_de_locacoes_por_dia(app=self.app, df=self.app.df)

                    continue
                case 9:
                    
                    logic.visualizar_medias_de_locacoes_por_horarios_de_um_dia(app=self.app, df=self.app.df)

                    continue
                case 10:
                    self.quit()
