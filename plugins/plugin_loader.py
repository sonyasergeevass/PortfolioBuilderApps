import os
import importlib
import importlib.util
import io

PLUGIN_DIR = 'plugins'

def load_plugins():
    plugins = []
    plugin_dir = os.path.dirname(__file__) #return path to current directory(plugins)
    exclude_files = ['plugin_loader.py', '__init__.py']
    for filename in os.listdir(plugin_dir): #listdir получает список имен файлов в директории plugins
        if filename.endswith('.py') and filename not in exclude_files:
            try:
                module_name = f"{PLUGIN_DIR}.{filename[:-3]}"
                module = importlib.import_module(module_name)
                print(module)
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

def load_plugins_from_dir(filename):
    # Чтение содержимого файла
    file_content = filename.read().decode('utf-8')
    # Создание временного модуля в памяти
    module_name = "dynamic_plugin_module"
    spec = importlib.util.spec_from_loader(module_name, loader=None)
    module = importlib.util.module_from_spec(spec)
    exec(file_content, module.__dict__)
    return module
# print(load_plugins())