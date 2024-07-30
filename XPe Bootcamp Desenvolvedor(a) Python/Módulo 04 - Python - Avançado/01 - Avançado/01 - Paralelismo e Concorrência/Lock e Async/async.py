import asyncio
import concurrent.futures
import multiprocessing
import time
from enum import Enum
from typing import List

import aiohttp
import nest_asyncio
import requests

nest_asyncio.apply()

BASE_URL: str = "https://api.openbrewerydb.org/breweries"

def get_ids_cervejarias() -> List[str]:
    request = requests.get(BASE_URL)
    if request.status_code == 200:
        data = request.json()

        ids: List[str] = [brewery['id'] for brewery in data]
        return ids
    

def get_cervejaria(id: str) -> None:
    request = requests.get(f"{BASE_URL}/{id}")
    if request.status_code == 200:
        print(request.json())


async def get_cervejaria_async(id: str, session: aiohttp.ClientSession) -> None:
    async with session.get(f"{BASE_URL}/{id}") as response:
        print(await response.json())


async def processar_async(ids: List[str]) -> None:
    coros: List = []

    async with aiohttp.ClientSession() as session:
        for id in ids:
            coros.append(get_cervejaria_async(id, session))
        
        await asyncio.gather(*coros)   


async def get_cervejaria_async_manual(id: str) -> None:
    loop = asyncio.get_running_loop()

    await loop.run_in_executor(None, get_cervejaria, id)


class TipoExecucao(Enum):
    UM_PROCESSO = 1
    VARIAS_THREADS = 2
    ASYNCIO_LIB_AIOHTTP = 3    
    ASYNCIO_MANUAL = 4


def main() -> None:
    started: float = time.time()
    
    tipo_execucao = TipoExecucao.ASYNCIO_MANUAL

    cores: int = multiprocessing.cpu_count()
    ids_cervejarias: List[str] = get_ids_cervejarias() 


    if TipoExecucao.UM_PROCESSO == tipo_execucao:
        # Usando somente um processo
        for id_cervejaria in ids_cervejarias:
            get_cervejaria(id_cervejaria)

    elif TipoExecucao.VARIAS_THREADS == tipo_execucao:
        # Usando várias threads
        with concurrent.futures.ThreadPoolExecutor(cores) as thp:
            thp.map(get_cervejaria, ids_cervejarias)
            
    elif TipoExecucao.ASYNCIO_LIB_AIOHTTP == tipo_execucao:
        # Usando Asyncio com aiohttp
        event_loop = asyncio.get_event_loop()

        event_loop.run_until_complete(processar_async(ids_cervejarias))

    elif TipoExecucao.ASYNCIO_MANUAL == tipo_execucao:
        # Usando Asyncio manual
        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        tasks = [event_loop.create_task(get_cervejaria_async_manual(id)) for id in ids_cervejarias]

        event_loop.run_until_complete(asyncio.wait(tasks))
        
    elapsed: float = time.time()

    print(f"\nExecutado com: {tipo_execucao}")
    print(f"\nTempo de requisição: {elapsed - started} segundos")


if __name__ == "__main__":
    main()
