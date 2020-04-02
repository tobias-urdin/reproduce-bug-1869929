import sys
import logging

from oslo_db import options
from oslo_config import cfg
from oslo_db import concurrency

CONF = cfg.CONF

_BACKEND_MAPPING = {'sqlalchemy': 'nova.db.sqlalchemy.api'}
IMPL = concurrency.TpoolDbapiWrapper(CONF, backend_mapping=_BACKEND_MAPPING)

def select_db_reader_mode(f):
    """Decorator to select synchronous or asynchronous reader mode.

    The kwarg argument 'use_slave' defines reader mode. Asynchronous reader
    will be used if 'use_slave' is True and synchronous reader otherwise.
    """
    return IMPL.select_db_reader_mode(f)

@select_db_reader_mode
def _db_service_get_by_compute_host(context, host, use_slave=False):
    print('yessss')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

CONF.register_opts(options.database_opts, 'database')
CONF.log_opt_values(logger, logging.WARNING)
