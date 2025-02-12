from anpylar import Module

from .app_component import AppComponent
from .users.UsersModule  import Users_Auth


class AppModule(Module):

    modules = Users_Auth

    components = AppComponent

    bindings = {}

    services = {}

    routes = []

    def __init__(self):
        pass
