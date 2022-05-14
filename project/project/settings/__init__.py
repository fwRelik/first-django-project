from .base import *

try:
    from .local import *
except ImportError:
    print("Can't find module settings.local! Make it from local.py.skeleton")
    print("Не удается найти модуль settings.local! Сделайте это из local.py.skeleton")
