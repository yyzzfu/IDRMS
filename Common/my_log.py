import logging
from Common import dir_config


class MyLog:

    def my_log(self, msg, level):
        # 1.定义一个日志收集器
        my_logger = logging.getLogger('IDRMS')

        # 日志输出的格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - 日志信息：%(message)s')
        # formatter = logging.Formatter('%(asctime)s - %(name)s - "%(pathname)s:%(lineno)d" - %(funcName)s
        # - %(levelname)s - %(message)s',"%Y-%m-%d %H:%M:%S")

        # 设置收集日志的级别
        my_logger.setLevel('DEBUG')

        # 2.定义一个输出渠道--控制台
        ch = logging.StreamHandler()

        # 设置输出日志的格式
        ch.setFormatter(formatter)

        # 定义输出日志的级别
        ch.setLevel('DEBUG')

        # 定义一个输出渠道--文本
        file_name = dir_config.log_dir + "/log.txt"
        fh = logging.FileHandler(file_name, encoding='UTF-8')
        # 设置输出日志的格式
        fh.setFormatter(formatter)

        # 定义日志输出的级别
        fh.setLevel('DEBUG')

        # 3.将日志收集器和输出渠道两者相结合，指定输出渠道
        my_logger.addHandler(fh)
        my_logger.addHandler(ch)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

        # 关闭日志收集器，防止日志重复
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')


if __name__ == '__main__':
    MyLog().debug('debug级别')
    MyLog().my_log('error级别', 'ERROR')


