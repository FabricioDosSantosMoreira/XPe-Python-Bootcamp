from typing import Dict, List

from rx import create
from rx.core.typing import Observer

STOCKS: List[Dict[str, int]] = [
    {'TCKR': 'APPL', 'PRICE': 200},
    {'TCKR': 'GOOG', 'PRICE': 90},
    {'TCKR': 'TSLA', 'PRICE': 120},
    {'TCKR': 'MSFT', 'PRICE': 150},
    {'TCKR': 'INTL', 'PRICE': 70},
]


# Método 1
class StockObserver(Observer):
    def on_next(self, value) -> None:
        print(f"Instruções recebidas para comprar a ação {value}")

    def on_completed(self) -> None:
        print("Todas as ordens de compras foram finalizadas!")

    def on_error(self, error) -> None:
        print(f"Erro identificado: {error}")

def buy_stock_events(observer: Observer, scheduler) -> None:
    for stock in STOCKS:
        if stock['PRICE'] > 100:
            observer.on_next(stock['TCKR'])

    observer.on_completed()


# Cria o observable e assina o observer
source = create(buy_stock_events)
source.subscribe(StockObserver())
