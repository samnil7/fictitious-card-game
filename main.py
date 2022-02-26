import logging
import sys
from sys import exc_info
import os
from deck_cards import card

log = {"log_format": '%(asctime)15s| %(levelname)5s | %(name)5s | %(module)15s | %(funcName)15s | %(message)s',
       "log_level": logging.INFO,
       "driver_log": "Logs\card_logs.log"
       }

if not os.path.exists("Logs"):
    os.makedirs("Logs")

# noinspection PyArgumentList
logging.basicConfig(format=log["log_format"], level=log["log_level"],
                    handlers=[logging.FileHandler(log["driver_log"], mode="w"), logging.StreamHandler()])

logger = logging.getLogger(__name__)

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    try:
        logging.info('Creating the Deck')
        myDeck = card.Deck()
        # shuffling the deck
        logging.info('Shuffling the Deck')

        myDeck.shuffle()

        player = card.Player()
        player.draw(myDeck, 2)
        player.showHand()
    except Exception:
        exc_type, exc_value, exc_traceback = exc_info()
        logging.exception("Something went wrong, please check the exception", exc_info=True)
        sys.exit(1)
