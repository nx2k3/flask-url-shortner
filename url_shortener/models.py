from string import digits,ascii_letters
from datetime import datetime
from random import choices

from . import db 

class Link(db.Document):
    meta = {'collection': 'links'}
    url = db.URLField(max_length=512)
    short = db.StringField(max_lenght=3, unique=True)
    visits = db.IntField(default=0)
    timestamp = db.DateTimeField(default=datetime.now())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short = self.generate_short_link()

    def generate_short_link(self):
        short = ''.join(choices(digits + ascii_letters, k=3))
        link = Link.objects (short=short).first()

        if link:
            return self.generate_short_link()
        return short
