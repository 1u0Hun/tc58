# conding=utf-8


import sys

from tc58.crawl_xici_ip import GetIP

reload(sys)
sys.setdefaultencoding('utf-8')

class RandomProxyMiddleware(object):
    def process_request(self, request, spider):
        get_ip = GetIP()
        request.meta["proxy"] = get_ip.get_random_ip()
