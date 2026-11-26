import logging

logger = logging.getLogger(__name__)

LEVEL = logging.INFO
FILE_NAME = "LOG.txt"
_LOG_TIME_FORMAT = '%m/%d/%Y - %H:%M:%S'
_LOG_MESSAGE_FORMAT = '%(funcName)s - [%(levelname)s at %(asctime)s]: %(message)s'

def _setup_logger():
	logging.basicConfig(
		filename = FILE_NAME,
		level = LEVEL,
		format=_LOG_MESSAGE_FORMAT,
		datefmt=_LOG_TIME_FORMAT)

def run_function(fun):
	def wrapper(*args, **kw):
		try:
			result = fun(*args, **kw)
		except Exception as e:
			logger.error(e)
			raise e

		else:
			logger.info("OK")
			return result

	return wrapper
	
if __name__ == '__main__':

	_setup_logger()

	@run_function
	def testinger(usr):
		print("Hello, %s!" % usr if usr else "Bentoo! Are you kidding me?!")

	testinger(input("Who're U? "))









