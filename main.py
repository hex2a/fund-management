#!/usr/bin/env python3
"""
kassomat-backend
"""
from logger import setup_logger
import config
import asyncio
import asyncio_redis

__version__ = "0.1.0"
__license__ = "GPL3"


logger = setup_logger(logfile=None, level=config.LOG_LEVEL)


@asyncio.coroutine
def redis_events():
    # Create connection
    connection = yield from asyncio_redis.Connection.create(
        host=config.REDIS_HOST, port=config.REDIS_PORT)

    # Create subscriber.
    subscriber = yield from connection.start_subscribe()

    # Subscribe to channel.
    yield from subscriber.subscribe(['main'])

    # Inside a while loop, wait for incoming events.
    while True:
        reply = yield from subscriber.next_published()
        print('Received: ', repr(reply.value), 'on channel', reply.channel)

    # When finished, close the connection.
    connection.close()


def main():
    logger.info("kassomat-backend started")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(redis_events())

if __name__ == "__main__":
    main()
