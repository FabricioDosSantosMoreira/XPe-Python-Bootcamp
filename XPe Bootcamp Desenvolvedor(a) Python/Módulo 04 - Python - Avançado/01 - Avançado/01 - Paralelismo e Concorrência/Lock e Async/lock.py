from threading import Lock, Thread
from time import sleep


class Loja():

    def __init__(self, estoque: int) -> None:
        self.estoque: int = estoque 

        # Inicializa o Lock
        self.lock: Lock = Lock() 


    def comprar(self, quantidade: int) -> None:

        # Bloqueia a trava para evitar acesso concorrente
        self.lock.acquire()  

        # Verifica se há estoque suficiente
        if self.estoque < quantidade:  
            self.lock.release() # Libera a trava

            print("Não temos estoque suficiente!")
            return None
        
        sleep(1)  # Simula o tempo de processamento da compra
        self.estoque -= quantidade  
        
        print(f"Você comprou {quantidade} item. Ainda temos {self.estoque} em estoque.")
        self.lock.release() # Libera a trava após a conclusão da compra


loja: Loja = Loja(10)
threads = []

# Criando e iniciando as threads
for i in range(1, 20):
    t: Thread = Thread(target=loja.comprar, args=(i,))
    t.start()

    threads.append(t) # Adiciona a thread à lista para aguardar mais tarde


# Aguardando todas as threads terminarem
for t in threads:
    t.join()

print("\nTodas as compras foram processadas!")
