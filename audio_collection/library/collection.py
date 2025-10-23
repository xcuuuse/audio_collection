from audio.base import AudioFile


class Collection:
    def __init__(self, name: str, collection_items: list[AudioFile]):
        self.__name = name
        self.__collection_items = collection_items

    @property
    def name(self):
        return self.__name

    @property
    def collection_items(self):
        return self.__collection_items

    def add_item(self, item: AudioFile):
        self.__collection_items.append(item)


class Folder:
    def __init__(self, name: str, folder_items: list[AudioFile]):
        self.__name = name
        self.__folder_items = folder_items

    @property
    def name(self):
        return self.__name

    @property
    def folder_items(self):
        return self.__folder_items


class FolderManager:
    def __init__(self, folders: Folder):
        self.__folders = folders

    @property
    def folders(self):
        return self.__folders

    @staticmethod
    def create_folder(name: str, items: list[AudioFile]):
        return Folder(name, items)