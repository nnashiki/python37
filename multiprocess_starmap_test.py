import multiprocessing as mp
import time
from logging import getLogger, basicConfig, DEBUG

basicConfig(level=DEBUG)
logger = getLogger(__name__)


def task(param1, param2):
    logger.debug(param1)
    time.sleep(3)
    logger.debug(param2)
    return True


def error_task(param1, param2):
    logger.debug(param1)
    time.sleep(3)
    logger.debug(param2)
    raise Exception('例外だよ!')


if __name__ == '__main__':
    with mp.Pool(2) as pool:
        result = pool.starmap(task, [['1', '2'], ['3', '4']])
        logger.debug(result)

    with mp.Pool(2) as pool:
        result = pool.starmap(error_task, [['5', '6'], ['7', '8']])
        logger.debug(result)
