# https://docs.python.org/3/library/asyncio-task.html
# https://docs.python.org/3/library/contextvars.html#contextvars.Context

import asyncio


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())