from anpylar import AuthGuard


class AuthGuard(AuthGuard):

    def can_activate(self, route):
        return self.check_login(route.path)

    def can_activate_child(self, route):
        return self.can_activate(route)

    def check_login(self, path):
        if self.auth_service.is_logged:
            return True

        self.auth_service.redir_path = path
        self.router.route_to('/login', session_id=1234567890)
        return False
