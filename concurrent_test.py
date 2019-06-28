import time
from concurrent.futures.process import ProcessPoolExecutor
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


def wrapper(args):
    return task(*args)


def error_wrapper(args):
    return error_task(*args)


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as executor:

        for result in executor.map(wrapper, [['1', '2'], ['3', '4']]):
            logger.debug(result)

    with ProcessPoolExecutor(max_workers=2) as executor:

        for result in executor.map(error_wrapper, [['5', '6'], ['7', '8']]):
            logger.debug(result)
