# __ makes attribute private. It will not be available outside

class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, key, count):
        self.__tags[key.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        iter(self.__tags)


cloud = TagCloud()
# cloud.__tags will not be accessible
# But you can access it
print(cloud.__dict__)  # {'_TagCloud__tags': {}}
print(cloud._TagCloud__tags)  # {}
