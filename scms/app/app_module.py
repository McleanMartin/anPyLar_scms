from anpylar import Module

from .app_component import AppComponent


class AppModule(Module):

    components = AppComponent

    bindings = {}

    services = {}

    routes = []

    def __init__(self):
        pass
