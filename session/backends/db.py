from django.contrib.sessions.backends.db import SessionStore as DBStore

class SessionStore(DBStore):

    def __init__(self, session_key=None):
        super().__init__(session_key)
        self.__dict__['order'] = None

    def __setattr__(self, name, value):
        if name == 'order':
            self.__dict__['modified'] = True
        super().__setattr__(name, value)

    @classmethod
    def get_model_class(cls):
        return CustomSession

    def is_empty(self):
        "Return True when there is no session_key and the session is empty."
        try:
            empty = super().is_empty() and (self.order is None)
            return empty
        except AttributeError:
            print("error")
            return True

    def create_model_instance(self, data):
        obj = super().create_model_instance(data)
        obj.order = self.order
        return obj

    def load(self):
        s = self._get_session_from_db()
        self.order = s.order
        return self.decode(s.session_data) if s else {}


from session.models import CustomSession