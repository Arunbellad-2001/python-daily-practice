import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithmethicApp")

def add(a,b):
    result=a+b
    logger.debug(f"adding{a}+{b}={result}")
    return result

def substarct(a,b):
    result=a-b
    logger.debug(f"substarct{a}-{b}={result}")
    return result

def multi(a,b):
    result=a*b
    logger.debug(f"Multification{a}*{b}={result}")
    return result
def divsion(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing{a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("Dvision by zero error")
        return None

add(10,15)
substarct(15,10)
multi(10,20)
divsion(20,0)

