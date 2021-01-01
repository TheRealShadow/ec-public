import importlib
import os
import warnings


def init(bot, session):
    bot.loop.run_until_complete(start_plugins(bot, session, [# Dynamically import
        importlib.import_module(f'.', f'{__name__}.{file[:-3]}')

        # All the files in the current directory
        for file in os.listdir(os.path.dirname(__file__))

        # If they start with a letter and are Python files
        if file[0].isalpha() and file.endswith('.py')]))


async def start_plugins(bot, session, plugins):
    for plugin in plugins:
        p_init = getattr(plugin, 'init', None)
        if callable(p_init):
            await p_init(bot, session)

        else:
            print('Couldn\'t get the plugins')


def cleanup_plugins():
    plugins = [# Dynamically import
        importlib.import_module(f'.', f'{__name__}.{file[:-3]}')

        # All the files in the current directory
        for file in os.listdir(os.path.dirname(__file__))

        # If they start with a letter and are Python files
        if file[0].isalpha() and file.endswith('.py')]
    for plugin in plugins:
        p_cleanup = getattr(plugin, 'cleanup', None)
        if callable(p_cleanup):
            try:
                p_cleanup()
            except Exception as e:
                warnings.warn(f'Failed to cleanup {plugin.__name__}: {type(e)} ({e})')
