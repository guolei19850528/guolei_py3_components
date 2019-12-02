#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def get_logging_logger_obj(logger_name="guolei_py3_components", logging_level="info", logging_dir_path="",
                           is_save_file=False):
    """
    get logging logger obj
    :param logger_name:str
    :param logging_level:str
    debug
    info
    warning
    error
    critical
    warn
    :param logging_dir_path:str
    default os.getcwd()/runtime/logs/logger_name/year/month/day/hour/%Y-%m-%d%H.log
    :param is_save_file:bool
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
    if logging_level == "debug":
        logging_logger_obj.level = logging.DEBUG
    if logging_level == "info":
        logging_logger_obj.level = logging.INFO
    if logging_level == "warning":
        logging_logger_obj.level = logging.WARNING
    if logging_level == "error":
        logging_logger_obj.level = logging.ERROR
    if logging_level == "critical":
        logging_logger_obj.level = logging.CRITICAL
    if logging_level == "warn":
        logging_logger_obj.level = logging.WARN
    if is_save_file:
        time_struct = time.localtime(time.time())
        year_str, month_str, month_day_str, hour_str, minute_str, second_str, _, _, _ = tuple(
            map(str, list(time_struct)))
        if not isinstance(logging_dir_path, str) or len(logging_dir_path) == 0:
            logging_dir_path = os.path.join(os.getcwd(), "runtime", "logs", logger_name, year_str, month_str,
                                            month_day_str,
                                            hour_str)
        try:
            os.makedirs(logging_dir_path)
        except:
            pass
        log_file_name = time.strftime("%Y%m%d%H", time.localtime(time.time())) + ".log"
        log_file_full_path = os.path.join(logging_dir_path, log_file_name)
        file_handler = logging.FileHandler(filename=log_file_full_path, encoding="utf8")
        file_handler.formatter = logging_formatter
        logging_logger_obj.addHandler(file_handler)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.formatter = logging_formatter
    logging_logger_obj.addHandler(console_handler)
    return logging_logger_obj
