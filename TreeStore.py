class TreeStore:
    def __init__(self, items: list[dict]):
        self.items = items
        self.items_elements = {}
        self.children_elements = {}
        for item in items:
            self.items_elements[item['id']] = item

            parent = item['parent']
            if self.children_elements.get(parent) is None:
                self.children_elements[parent] = []

            self.children_elements[parent].append(item)

    def getAll(self) -> list[dict]:
        return self.items

    def getItem(self, id: int) -> dict:
        return self.items_elements.get(id)

    def getChildren(self, id: int) -> list[dict]:
        return self.children_elements.get(id, [])

    def getAllParents(self, id: int) -> list[dict]:
        parents = []
        current_id = id
        while current_id is not None:
            item = self.items_elements.get(current_id)
            if item is None:
                break

            parents.append(item)
            current_id = item['parent']

        return parents


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)

# Примеры использования:
# print(ts.getItem(7))
# print(ts.getChildren(4))
# print(ts.getChildren(5))
# print(ts.getAllParents(7))