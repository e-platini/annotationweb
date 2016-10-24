from os.path import basename

from annotationweb import settings
from annotationweb.models import Task
from os.path import join
import os
import importlib

exporters = []


class MetaExporter(type):

    def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, dict(namespace))
        if name is not 'Exporter':
            print('Found the exporter class', name)
            exporters.append(result)
        return result


class Exporter(metaclass=MetaExporter):

    def get_form(self, data=None):
        raise NotImplementedError('An exporter needs to implement an export method')

    def export(self, form):
        raise NotImplementedError('An exporter needs to implement an export method')


def find_all_exporters(task_type):
    result = []

    # Go through each app and see if there is an exporters.py file
    for app in settings.INSTALLED_APPS:
        if app[:7] == 'django.':
            continue
        exporters.clear()
        module_filename = join(settings.PROJECT_PATH, join(app, 'exporters.py'))
        if not os.path.isfile(module_filename):
            continue
        module_name = basename(app + '.exporters')
        foo = importlib.machinery.SourceFileLoader(module_name, module_filename).load_module()
        for exporter in exporters:
            if exporter.task_type == task_type:
                result.append(exporter)
            else:
                print('Exporter not correct type')

        # Python 3.5
        # spec = importlib.util.find_spec(app + '.exporters')
        # if spec is not None:
        #     print('Found exporters module in ', app)
        #     print('Importing..')
        #     exporters.clear()
        #     foo = importlib.util.module_from_spec(spec)
        #     spec.loader.exec_module(foo)
        #     for exporter in exporters:
        #         if exporter.task_type == task_type:
        #             result.append(exporter)
        #         else:
        #             print('Exporter not correct type')
        # else:
        #     print('No exporters module found in ', app)

    return result
