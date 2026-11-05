class Person:
    def __init__(self, user_id, name, contact):
        self._user_id = user_id
        self._name = name
        self._contact = contact
    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def contact(self):
        return self._contact