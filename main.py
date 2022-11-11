# coding=utf-8
import os
import random
import time
from loguru import logger
import uuid

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

log_file_path = os.path.join(BASE_DIR, 'Log/access.log')
err_log_file_path = os.path.join(BASE_DIR, 'Log/err.log')

logger.add(log_file_path, format="{message}", rotation="50 MB", encoding='utf-8',
           retention=6)
logger.add(err_log_file_path, rotation="100 MB", encoding='utf-8', retention=2, level='ERROR')

logger.remove(handler_id=None)
local_time = time.localtime(time.time())

if __name__ == '__main__':

    n = 0
    while True:
        line = f"[ISIS] [{time.strftime('%d/%b/%Y:%H:%M:%S +0800', time.localtime(time.time()))}] logid={uuid.uuid5(uuid.NAMESPACE_URL, str(random.randint(0, 1000))).hex} " \
               "callid=cdmdqm00rjlds35qglfg local_hostname=yq01-pcs-cloudcache-redis042.yq01.baidu.com " \
               "remote_addr=127.0.0.1 server_addr=- host=127.0.0.1 client_costtime=0.18 " \
               f"http_code={random.randint(200, 599)} req_time=0.000 client_timeout=- timeout_quantile=- " \
               "fault=- sdk_version=GO-1.0.0.6 request_from=local ufc_time=0.126 " \
               "to_module=netdisk-deepfile-table ufc_backup=- from_service=netdisk-deepfile " \
               "update_lantency=10 ori_to_service=netdisk-deepfile-table " \
               "api=/bypass method=get_backend from_idc=YQ " \
               "interact=[[callid=cdmdqm00rjlds35qglfg cost_time=0.000 to_module=netdisk-deepfile-table " \
               "to_bns=netdiskdeep-qilin-proxy.TABLE.yq01 to_ip=10.62.75.14:8444 to_idc=- upstream_status=200]]"

        logger.info(line)
        n += 1
        if n == 200:
            line = """
          Traceback (most recent call last):
          File "/main.py", line 40, in <module>
            logger.error()
          TypeError: error() missing 1 required positional argument: '_Logger__message'
                    """
            logger.error(line)
            n = 0
            time.sleep(1)
