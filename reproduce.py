from nova.db import api as db


@db.select_db_reader_mode
def _db_service_get_by_compute_host(context, host, use_slave=False):
    print('yes')
