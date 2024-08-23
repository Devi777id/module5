import asyncio

async def delayed_hi(day: str):
    await asyncio.sleep(7)
    print(f"Monday is after {day}")

async def main():
    await asyncio.gather(
        delayed_hi('a'),
        delayed_hi('b'),
        delayed_hi('c'),
    )

asyncio.run(main())