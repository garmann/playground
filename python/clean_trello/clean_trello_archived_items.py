#!/usr/bin/python3

"""
simple python script to clean my trello archived items. 
it will look for archived cards in all boards to delete them.
"""

from trello import TrelloClient

CONFIG = {
    'api_key'         : "x",
    'server_token'    : "x",
}

client = TrelloClient(
    api_key         = CONFIG['api_key'],
    api_secret      = CONFIG['server_token'],
)

# manual list generated with:
# >> > for board in client.list_boards():
# ... print(board.__dict__)
my_boards = [
    'fill with ids',
    ]

for idx, card in enumerate(client.search(query="is:archived", cards_limit=1000, board_ids=my_boards, models="cards")):
    print(idx, card.id, card.board, card.name, card.url, card.list_id)
    #card.delete()
    print()
