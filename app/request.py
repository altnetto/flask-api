from flask_restful.reqparse import RequestParser


def only(params: list) -> dict:
    parser = RequestParser()

    for param in params:
        parser.add_argument(param)

    return parser.parse_args()