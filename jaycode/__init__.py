from .ssh import SSHNamespace as SSH
from .db import DBNamespace as DB
from .file import FileNamespace as File
from .crawling import CrawlingNamespace as Crawling

class Core:
    def __init__(self):
        self.SSH = SSH(self)
        self.DB = DB(self)
        self.File = File(self)
        self.Crawling = Crawling(self)

init = Core