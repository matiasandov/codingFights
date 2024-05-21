class SQL:

    def __init__(self, names, columns):
        self.schema = {}
        self.info = {}

        for key, val in names, columns:
            self.schema[key] = [{0:[]}]
            self.info[key] = val