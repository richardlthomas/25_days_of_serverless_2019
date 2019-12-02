import logging
from random import choice

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    sides = ['נ', 'ג', 'ה', 'ש']
    return func.HttpResponse(choice(sides))
