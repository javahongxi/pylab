"""
This is a module
"""
from urllib import request
import re


class Spider:
    """
    This is a class
    """
    url = 'http://localhost:8080/mock/www.zhenai.com/zhenghun'
    cities_re = '<a href="(http://localhost:8080/mock/www.zhenai.com/zhenghun/[0-9a-z]+)"[^>]*>([^<]+)</a>'

    @classmethod
    def __fetch_content(cls):
        """
        This is a method
        :return:
        """
        r = request.urlopen(cls.url)
        return str(r.read(), encoding='utf-8')

    @classmethod
    def __analysis(cls, content):
        return re.findall(cls.cities_re, content)

    def go(self):
        content = self.__fetch_content()
        cities = self.__analysis(content)
        print(cities)


# test
spider = Spider()
spider.go()