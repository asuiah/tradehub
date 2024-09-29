from .interface import TransformerAbstract


class TransformYFinanceDF(TransformerAbstract):
    def process_data(self, data):
        print(data)
        # TODO: restruct yahoo fiannace dataframe
        return data["Open"]
