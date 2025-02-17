from rx import create, disposable, of
from rx.core.typing import Observer


def push_five_strings(observer: Observer, scheduler) -> None:
    observer.on_next('Alfa')
    observer.on_next('Beta')
    observer.on_next('Gama')
    observer.on_next('Delta')
    observer.on_next('Epsilon')

    observer.on_completed()


# NOTE: Método 1 - Observable usando uma classe personalizada
class PrintObserver(disposable.Disposable):
    def on_next(self, value) -> None:
        print(f"Recebido {value}")

    def on_completed(self):
        print("Fim!\n")

    def on_error(self, error):
        print(f"Erro identificado: {error}")

# Cria um observable
source = create(push_five_strings)


# Assina o observable
source.subscribe(PrintObserver())


# NOTE: Método 2 - Observable usando 'of'
# Criando um observable usando a função 'of' com os valores especificados
source = of('Alfa', 'Beta', 'Gama', 'Delta', 'Epsilon')
# Assina o observable
source.subscribe(
    on_next= lambda value:  print(f"Recebido {value}"),

    on_completed= lambda: print("Fim!\n"),

    on_error= lambda error: print(f"Erro identificado: {error}")
)
