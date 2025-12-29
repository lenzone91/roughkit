import asyncio
import websockets
import json
from pathlib import Path

msg = \
{"id":1,"jsonrpc":"2.0","method":"public/get_instruments","params":{"currency":"BTC","kind":"option"}}

OUTPUT_PATH = Path(__file__).with_name("data.json")

async def call_api(msg):
    async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
        await websocket.send(msg)
        # RPC call returns a single payload; grab it, decode JSON, and persist nicely formatted.
        response = await websocket.recv()
        decoded = json.loads(response)
        OUTPUT_PATH.write_text(json.dumps(decoded, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Ecriture de la reponse dans {OUTPUT_PATH}")

asyncio.run(call_api(json.dumps(msg)))
