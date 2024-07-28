from threading import Thread
from time import sleep


class MinhaThread(Thread):

    def __init__(self, nome: str, tempo: int) -> None:
        super().__init__()

        self.nome: str = nome
        self.tempo: int = tempo

        # Flag para rastrear se a thread terminou
        self.terminou: bool = False 
    

    def run(self) -> None:
        print(f"Começando a executar a {self.nome} por {self.tempo}s")
        sleep(self.tempo)

        self.terminou = True


# Criar e iniciar as threads
t1 = MinhaThread("Thread 1", 5)
t2 = MinhaThread("Thread 2", 10)
t3 = MinhaThread("Thread 3", 7)
t1.start()
t2.start()
t3.start()


for i in range(15):
    print(f"seg: {i}")

    if t1.terminou:
        print(f"A {t1.name} terminou!")
        t1.terminou = False

    if t2.terminou:
        print(f"A {t2.name} terminou!")
        t2.terminou = False

    if t3.terminou:
        print(f"A {t3.name} terminou!")
        t3.terminou = False
    
    sleep(1)


# Aguarda a conclusão das threads
t1.join()
t2.join()
t3.join()
