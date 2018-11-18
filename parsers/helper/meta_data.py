class MetaDataHelper:
    def __init__(self):
        pass

    @staticmethod
    def get_meta_data(exchange):
        return {'name': exchange.name, 'endPoint': exchange.end_point}
