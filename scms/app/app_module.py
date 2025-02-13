from anpylar import Module

from .app_component import AppComponent
from .users.LoginModule  import LoginComponent


class AppModule(Module):

    modules = LoginComponent

    components = AppComponent

    bindings = {}

    services = {}

    routes = []

    def __init__(self):
        pass
