import os
import importlib

PLUGIN_DIR = 'plugins'

def load_plugins():
    plugins = []
    plugin_dir = os.path.dirname(__file__) #return path to current directory(plugins)
    exclude_files = ['plugin_loader.py']
    for filename in os.listdir(plugin_dir): #listdir получает список имен файлов в директории plugins
        if filename.endswith('.py') and filename not in exclude_files:
            try:
                module_name = f"{PLUGIN_DIR}.{filename[:-3]}"
                module = importlib.import_module(module_name)
                plugins.append(module)
            except ImportError:
                pass
    return plugins

def get_plugin_info(plugin):
    info = {
        'name': getattr(plugin, '__plugin_name__', 'Unknown'),
        'version': getattr(plugin, '__version__', 'Unknown'),
        'author': getattr(plugin, '__author__', 'Unknown'),
    }
    return info

# print(load_plugins())