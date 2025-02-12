from anpylar import Observable, Model


class AuthService(Model):
    bindings = {
        'is_logged': False,
        'redir_path': '',
    }

    def login(self):
        return Observable.of(True) \
            .delay(1000) \
            .do_action(lambda x: setattr(self, 'is_logged', x))

    def logout(self):
        self.is_logged = False

    def not_logged(self):
        return self.is_logged_.map(lambda x: not x)
