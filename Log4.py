#-*-coding:utf-8-*-2
__author__ = 'Sky'
##date:2016/12/12
#自定义一个log类装饰器，和装饰器方法

import logging

class Log4(object):
    def __init__(self, level):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%s',
                            filename='%s.log' % ('show'),
                            filemode='w'
                            )
        # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s  %(name)-6s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        self.level = level

    def __call__(self, func):
        self.func = func
        return self.decorate_log()

    def decorate_log(self, *args):
        if self.level == 'info':
            logging.info('%s %s  is running'%(self.func.__name__, args))
        elif self.level == 'warning':
            logging.warning('%s %s  is running'%(self.func.__name__, args))
        else:
            print 'no'
        return self.func


'''
#装饰器方法
def decorate_log(level):
    def _decorate(func):
        def wrapper(*args, **kwargs):
            if level == 'info':
                logging.info('%s is running'%(func.__name__))
                func(*args)
            elif level == 'warning':
                logging.warning('%s with warning '%(func.__name__))
            else:
                func(*args)
            #return func
        return wrapper
    return _decorate

'''


@Log4('info')
def knock():
    print 'Tim knocked the desk'

knock()