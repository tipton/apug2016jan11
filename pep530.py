
# PEP 530: Asynchronous Comprehensions

# Code modified from -
# https://medium.com/the-python-corner/syntax-sugar-in-python-3-6-776178ce51f4#.gb5wx6pby

import asyncio

async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)

async def main():

    mylist = [y async for y in ticker(0.1, 10)]
    print(mylist)
    mydict = {y:y async for y in ticker(0.1, 10)}
    print(mydict)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())