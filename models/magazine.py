class Magazine:
    def __init__(self, id, title, category):
        self.id = id
        self.title = title
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.title}>'
