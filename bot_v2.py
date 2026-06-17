
import asyncio
import websockets
import json

# --- AI CONFIGURATION ---
AI_SCORES = {
    "PATTERN_FIVE": 100000000,
    "PATTERN_FIVE_BLOCKED": 10000000,  # FIX: 5 quan o bien van la thang
    "PATTERN_OPEN_FOUR": 5000000,
    "PATTERN_BLOCKED_FOUR": 1000000,
    "PATTERN_OPEN_THREE": 800000,
    "PATTERN_OPEN_TWO": 100,
    "DEFENSE_MULTIPLIER": 1.5
}

class HandingerCaroBot:
    def __init__(self):
        self.board = {}
        self.loss_streak = 0
        self.defense_mult = 1.0

    async def handle_message(self, message):
        try:
            data = json.loads(message)
            # Xử lý logic nước đi ở đây...
        except Exception as e:
            print(f"Error handling message: {e}")

    async def run_with_reconnect(self):
        uri = "wss://api.handinger.com/caro" # Giả định URI
        while True:
            try:
                async with websockets.connect(uri) as ws:
                    print("Bot connected to server.")
                    self.ws = ws
                    async for msg in ws:
                        await self.handle_message(msg)
            except (websockets.ConnectionClosed, Exception) as e:
                print(f"Connection lost: {e}. Reconnecting in 5s...")
                await asyncio.sleep(5)
            except asyncio.CancelledError:
                # Tránh lỗi CancelledError khi loop bị dừng
                break

async def main():
    bot = HandingerCaroBot()
    await bot.run_with_reconnect()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped by user.")
