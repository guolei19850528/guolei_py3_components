#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def get_logging_logger_obj(logger_name="guolei_py3_components", logging_level="info", logging_dir_path="",
                           is_save_file=False):
    """
    get logging logger obj
    :param logger_name:str
    :param logging_level:str
    debug,info,warning,error,critical,warn
    :param logging_dir_path:str
    default os.getcwd()/runtime/logs/logger_name/year/month/day/hour/%Y-%m-%d%H.log
    :param is_save_file:bool
    if true save file
    :return:logging logger object
    """
    import sys
    import os
    import logging
    import time
    logging_logger_obj = logging.getLogger(logger_name)
    logging_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(filename)s - %(lineno)d - %(message)s")
    logging_logger_obj.level = logging.INFO
    if logging_level.lower() == "debug":
        logging_logger_obj.level = logging.DEBUG
    if logging_level.lower() == "info":
        logging_logger_obj.level = logging.INFO
    if logging_level.lower() == "warning":
        logging_logger_obj.level = logging.WARNING
    if logging_level.lower() == "error":
        logging_logger_obj.level = logging.ERROR
    if logging_level.lower() == "critical":
        logging_logger_obj.level = logging.CRITICAL
    if logging_level.lower() == "warn":
        logging_logger_obj.level = logging.WARN
    if is_save_file:
        time_struct = time.localtime(time.time())
        year_str, month_str, month_day_str, hour_str, minute_str, second_str, _, _, _ = tuple(
            map(str, list(time_struct)))
        if not isinstance(logging_dir_path, str) or len(logging_dir_path) == 0:
            log_dir_path = os.path.join(os.getcwd(), "runtime", "logs", logger_name, year_str,
                                        "{year_str}{month_str}{month_day_str}".format(year_str=year_str,
                                                                                      month_str=month_str,
                                                                                      month_day_str=month_day_str),
                                        logging_level)
        try:
            os.makedirs(log_dir_path)
        except:
            pass
        log_file_name = time.strftime("%Y%m%d-%H", time.localtime(time.time())) + ".log"
        log_file_path = os.path.join(log_dir_path, log_file_name)
        file_handler = logging.FileHandler(filename=log_file_path, encoding="utf8")
        file_handler.formatter = logging_formatter
        logging_logger_obj.addHandler(file_handler)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.formatter = logging_formatter
    logging_logger_obj.addHandler(console_handler)
    return logging_logger_obj


def call_logging_logger_log(logging_logger_obj, attr="info",prefix=""):
    """
    call logging logger log by decorator
    :param logging_logger_obj:
    :param attr:
    :return:
    """

    def decorator_func(func):
        def wrapper_func(*args, **kw):
            if hasattr(logging_logger_obj, attr):
                call_attr = getattr(logging_logger_obj, attr)
                call_attr({"prefix":prefix,"data":func(*args, **kw)})
                return func(*args, **kw)
        return wrapper_func

    return decorator_func
