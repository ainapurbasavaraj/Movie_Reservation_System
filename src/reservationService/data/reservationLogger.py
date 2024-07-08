import logging
import inspect

class ReservationLogger:
    def __init__(self) -> None:
        self.logfile='reservationApp.log'

    def get_logger(self):
        loggerName=inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)
        filehandler=logging.FileHandler(self.logfile)
        formatter=logging.Formatter(
            "%(ascitime)s : %(levelname)s : %(modules)s : %(funcName)s : %(message)s"
        )
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger