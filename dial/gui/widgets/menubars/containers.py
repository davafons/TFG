# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

"""
Dependency Injection containers.
"""

import dependency_injector.containers as containers
import dependency_injector.providers as providers

from .menubar_main import MainMenuBar


class MenuBars(containers.DeclarativeContainer):
    Main: MainMenuBar = providers.Factory(MainMenuBar)
