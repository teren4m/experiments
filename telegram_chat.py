import argparse
from pprint import pprint

from telegram.client import Telegram

import utils

import telegram_creds as tc


def main():
    utils.setup_logging()

    parser = argparse.ArgumentParser()
    utils.add_api_args(parser)
    utils.add_proxy_args(parser)
    args = parser.parse_args()

    tg = Telegram(
        api_id=tc.api_id,
        api_hash=tc.api_hash,
        phone=tc.phone,
        database_encryption_key='changeme1234',
    )
    # you must call login method before others
    tg.login()

    result = tg.get_me()
    result.wait()
    pprint(result.update)

    tg.stop()


if __name__ == '__main__':
    main()