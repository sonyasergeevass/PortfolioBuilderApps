from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from PortfolioBuilderApps import plugin_modules
from plugins.plugin_loader import get_plugin_info, load_plugins_from_dir


# Create your views here.

def resume_generator_settings(request):
    # Ищем нужный модуль по атрибуту __plugin_name__
    module = None
    for plugin in plugin_modules:
        if getattr(plugin, '__plugin_name__', None) == "Resume Generator":
            module = plugin
            break

    # if module is None:
    #     # Обработка случая, когда модуль не найден
    #     return render(request, 'error.html', {'error': 'Plugin not found'})

    # Получаем информацию о плагине
    plugin_info = get_plugin_info(module)
    context = {
        'plugin_info': plugin_info,
    }
    return render(request, 'resume_generator_settings.html', context)


def create_resume(request):
    if request.method == 'POST':
        pdf_name = request.POST.get('pdf_name')
        if not pdf_name:
            pdf_name = "default_name"
        # Ищем нужный модуль по атрибуту __plugin_name__
        module = None
        for plugin in plugin_modules:
            if getattr(plugin, '__plugin_name__',
                       None) == "Resume Generator":
                module = plugin
                break

        # if module is None:
        #     # Обработка случая, когда модуль не найден
        #     return render(request, 'error.html', {'error': 'Plugin not
        #     found'})

        # Получаем информацию о плагине
        plugin_info = get_plugin_info(module)
        context = {
            'plugin_info': plugin_info,
        }
        html_content = render_to_string('resume_generator_settings.html',
                                        context)
        # Используем функцию из модуля
        if hasattr(module, 'generate_resume_pdf'):
            if module.generate_resume_pdf(html_content,
                                          "resumes/" + pdf_name + ".pdf"):
                return redirect('resume_generator_settings')


def github_repositories(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        module = None
        for plugin in plugin_modules:
            if getattr(plugin, '__plugin_name__',
                       None) == "Pull GitHub Repositories":
                module = plugin
                break
        plugin_info = get_plugin_info(module)
        context['plugin_info'] = plugin_info
        # Используем функцию из модуля
        if hasattr(module, 'get_github_repositories'):
            repositories = module.get_github_repositories(username)
            context['repositories'] = repositories
            return render(request, 'github_repositories.html', context)
    else:
        return render(request, 'github_repositories.html')


def gpt3_response(request):
    if request.method == "POST":
        question = request.POST.get('question')
        module = None
        for plugin in plugin_modules:
            if getattr(plugin, '__plugin_name__',
                       None) == "GPT3.5 Response":
                module = plugin
                break
        plugin_info = get_plugin_info(module)
        context = {'plugin_info': plugin_info}
        # Используем функцию из модуля
        if hasattr(module, 'get_gpt3_response'):
            answer = module.get_gpt3_response(question)
            context['answer'] = answer
            return render(request, 'gpt3_response.html', context)
    else:
        return render(request, 'gpt3_response.html')


def dir_response(request):
    context = {}
    result = "No directory response"
    if request.method == 'POST':
        plugin_file = request.FILES['plugin_file']
        plugin_modules.append(load_plugins_from_dir(plugin_file))
        module = None
        for plugin in plugin_modules:
            if getattr(plugin, '__plugin_name__',
                       None) == "Model1":
                module = plugin
                break
        plugin_info = get_plugin_info(module)
        context['plugin_info'] = plugin_info
        # Используем функцию из модуля
        if hasattr(module, 'a'):
            if module.a():
                result = module.a()
    context['result'] = result
    return render(request, 'import_plugin_from_directory.html', context)

def show_all_plugins(request):
    context = {}
    p_i = []
    for plugin in plugin_modules:
        plugin_info = get_plugin_info(plugin)
        p_i.append(plugin_info)

    context = {
        'plugin_info': p_i,
    }
    return render(request, 'all_plugins.html', context)
