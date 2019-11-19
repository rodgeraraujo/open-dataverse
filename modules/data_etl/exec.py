from .import_data import run_import
from .download_csv import run_download
import asyncio

async def teste():
    print("async task")

def run():
    # asyncio.run(teste())
    asyncio.run(run_download("aluno"))
    asyncio.run(run_import("aluno"))
    asyncio.run(run_download("servidores"))
    asyncio.run(run_import("servidores"))

run()