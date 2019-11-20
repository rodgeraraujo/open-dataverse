from .import_data import run_import
from .download_csv import run_download
import asyncio

async def teste():
    print("async task")

def run():
    # asyncio.run(teste())
    # run_download("aluno")
    # run_import("aluno")
    # run_download("servidores")
    # run_import("servidores")
    asyncio.run(run_download("aluno"))
    asyncio.run(run_import("aluno"))
    asyncio.run(run_download("servidores"))
    asyncio.run(run_import("servidores"))

run()