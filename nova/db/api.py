from oslo_db import concurrency
from oslo_config import cfg
from oslo_db import options


CONF = cfg.CONF
CONF.register_opts(options.database_opts, 'database')

_BACKEND_MAPPING = {'sqlalchemy': 'nova.db.sqlalchemy.api'}

IMPL = concurrency.TpoolDbapiWrapper(CONF, backend_mapping=_BACKEND_MAPPING)


def select_db_reader_mode(f):
    print('called nova.db.api.select_db_reader_mode')
    return IMPL.select_db_reader_mode(f)
