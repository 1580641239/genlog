# coding=utf-8
import os
import random
import time
from loguru import logger
import uuid

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

log_file_path = os.path.join(BASE_DIR, 'log/access.log')
err_log_file_path = os.path.join(BASE_DIR, 'log/err.log')
logger.remove(handler_id=None)
logger.add(log_file_path, format="{message}", rotation="1 H", level="INFO",
           enqueue=True, encoding='utf-8',
           retention=2)
logger.add(err_log_file_path, format="{time} {message}", rotation="1 H", encoding='utf-8', retention=2, level='ERROR')

local_time = time.localtime(time.time())

from_service = ["za-%s" % (i) for i in range(5)]
to_module = ["nz-az-%s" % (i) for i in range(4, 9)]

n = 0
while True:
    line = f"[ISIS] [{time.strftime('%d/%b/%Y:%H:%M:%S +0800', time.localtime(time.time()))}] logid={uuid.uuid5(uuid.NAMESPACE_URL, str(random.randint(0, 1000))).hex} " \
           "callid=cdmdqm00rjlds35qglfg local_hostname=ax01-xaxax-axa-.ax01 " \
           "remote_addr=127.0.0.1 server_addr=- host=127.0.0.1 client_costtime=0.18 " \
           f"http_code={random.randint(200, 599)} req_time=0.000 client_timeout=- timeout_quantile=- " \
           "fault=- sdk_version=GO-1.0.0.6 request_from=local ufc_time=0.126 " \
           f"to_module={random.choice(to_module)} ufc_backup=- from_service={random.choice(from_service)} " \
           "update_lantency=10 ori_to_service=q-table " \
           "api=/pwds method=get from_idc=YQ " \
           "interact=[[callid=cdmdqm00rjlds35qglfg cost_time=0.000 to_module=sa-table " \
           "to_bns=netsa-proxy.TABLE.yq01 to_ip=10.123.725.124:000 to_idc=- upstream_status=200]]"

    logger.info(line)
    n += 1
    if n == 200:
        try:
            1 / 0
        except Exception as e:
            logger.exception(e)
        n = 0
        time.sleep(2)
