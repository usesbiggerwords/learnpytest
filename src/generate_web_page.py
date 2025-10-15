from django.template import Template, Context, loader

from django.conf import settings
settings.configure()

def generate_page(json_data, mapping):
    t = loader.get_template('default.html')
    context_data = {k: json_data[v] for k, v in mapping}
    c = Context(context_data)
    result = t.render(c)
    print(result)