
class GTN(object):

    def __init__(self, gtn_id, tag):
        self._gtn_id = gtn_id
        self._tag = tag
        self._re_trigger = False

    @property
    def gtn_id(self):
        return self._gtn_id


    @property.setter
    def gtn_id(self, value):
        self._gtn_id = value

    @property
    def tag(self):
        return self._tag

    @property.setter
    def tag(self, value):
        self._tag = value

    @property
    def re_trigger(self):
        return self._re_trigger


    @property.setter
    def re_trigger(self, value=True):
        self._re_trigger = value
