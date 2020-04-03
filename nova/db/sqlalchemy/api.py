import sys
import functools
import inspect
from oslo_db.sqlalchemy import enginefacade


def get_backend():
    print('called nova.db.sqlalchemy.api.get_backend')
    return sys.modules[__name__]


def get_wrapped_function(function):
    print('called nova.db.sqlalchemy.api.get_wrapped_function')

    if not hasattr(function, '__closure__') or not function.__closure__:
        return function

    def _get_wrapped_function(function):
        if not hasattr(function, '__closure__') or not function.__closure__:
            return None

        for closure in function.__closure__:
            func = closure.cell_contents

            deeper_func = _get_wrapped_function(func)
            if deeper_func:
                return deeper_func
            elif hasattr(closure.cell_contents, '__call__'):
                return closure.cell_contents

        return function

    return _get_wrapped_function(function)


def _get_db_conf(conf_group, connection=None):
    print('called nova.db.sqlalchemy.api._get_db_conf')

    kw = dict(conf_group.items())
    if connection is not None:
        kw['connection'] = connection
    return kw


def create_context_manager(connection=None):
    print('called nova.db.sqlalchemy.api.create_context_manager')

    ctxt_mgr = enginefacade.transaction_context()
    ctxt_mgr.configure(**_get_db_conf(CONF.database, connection=connection))
    return ctxt_mgr


def get_context_manager(context):
    print('called nova.db.sqlalchemy.api.get_context_manager')
    return _context_manager_from_context(context) or main_context_manager


def select_db_reader_mode(f):
    print('called nova.db.sqlalchemy.api.select_db_reader_mode')

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        wrapped_func = get_wrapped_function(f)
        keyed_args = inspect.getcallargs(wrapped_func, *args, **kwargs)

        context = keyed_args['context']
        use_slave = keyed_args.get('use_slave', False)

        if use_slave:
            reader_mode = get_context_manager(context).async_
        else:
            reader_mode = get_context_manager(context).reader

        with reader_mode.using(context):
            return f(*args, **kwargs)
    return wrapper
