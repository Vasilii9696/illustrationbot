import asyncio
from dribble import dribble
from behance import send_message_withv

async def run_periodically(interval):
    while True:
        await dribble()

        await send_message_withv()
        print('o0')
        await asyncio.sleep(interval)
        print('o1')

# Основная асинхронная функция, которая запускает цикл
async def main():
    print('st')
    interval = 30 * 30  # 30 минут в секундах
    await run_periodically(interval)
    print('over')

# Запуск основного цикла событий
if __name__ == "__main__":
    print('fsdfsfd')
    asyncio.run(main())