import logging

logger = logging.getLogger(__name__)

LEVEL = logging.INFO
FILE_NAME = "LOG.txt"
_LOG_TIME_FORMAT = "%d/%m/%Y - %H:%M:%S"
_LOG_MESSAGE_FORMAT = """%(levelname)s - %(module)s.%(funcName)s
    Mensagem: %(message)s
    Arquivo: %(name)s
    Linha: %(lineno)d"""


def _setup_logger():
    logging.basicConfig(
        level=LEVEL,
        filename=FILE_NAME,
        datefmt=_LOG_TIME_FORMAT,
        format=_LOG_MESSAGE_FORMAT,
    )
    return logger


def run_function(fun):
    def wrapper(*args, **kw):
        try:
            result = fun(*args, **kw)
            logger.info("[%s] OK!", fun.__name__)
            return result

        except Exception as e:
            logger.error(
                """[%s] levantou %r;
        - Argumentos (args): %r
        - Argumentos-chave (kwargs): %r""",
            fun.__name__, e, args, kw)
            raise e

    return wrapper


if __name__ == "__main__":

    _setup_logger()

    @run_function
    def testinger(usr):
        print("Hello, %s!" % usr if usr else "Bentoo! Are you kidding me?!")

    testinger('None', 4,53,45,34)  # input("Who're U? "))

    @run_function
    def testinger():
        print("Isso dá erro!")
        raise IndexError

    testinger()  # input("Who're U? "))
