from fastapi import FastAPI, WebSocket
import asyncio
import redis
import time
from agents.conversation import handle_message
from utils.latency import log_latency

app = FastAPI()

# Redis connection
redis_client = redis.Redis(host="localhost", port=6379, db=0)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        start_time = time.time()
        data = await websocket.receive_text()

        # Process message through agent pipeline
        response = await handle_message(data, redis_client)

        # Measure latency
        log_latency(start_time)

        await websocket.send_text(response)
