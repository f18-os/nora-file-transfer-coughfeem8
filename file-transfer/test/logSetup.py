import logging

# DEBUG: 10 Detailed information, typically of interest only when diagnosing problems.

# INFO:  20 Confirmation that things are working as expected.

# WARNING: 30  An indication that something unexpected happened, or indicative of some problem in the near future (e.g. disk space low). The software is still working as expected.

# ERROR:  40  Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: 50 A serious error, indicating that the program itself may be unable to continue running.

'''
Attribute          name 
args 	        automatic 	
asctime 	%(asctime)s 	
created 	%(created)f 	
exc_info 	automatic 	
filename 	%(filename)s 	
funcName 	%(funcName)s 	
levelname 	%(levelname)s 	('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
levelno 	%(levelno)s 	
lineno 	        %(lineno)d 	
message 	%(message)s 
module 	        %(module)s 	
msecs 	        %(msecs)d 	
msg 	        automatic 	
name 	        %(name)s 	Name of the logger.
pathname 	%(pathname)s 
process 	%(process)d 	Process ID (if available).
processName 	%(processName)s
relativeCreated %(relativeCreated)d
stack_info 	automatic
thread 	        %(thread)d 	
threadName 	%(threadName)s 	
'''

#how to set up:

# connect and actuvate the  necesary formats to your loggin and files you intend to run
 
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
   # filename='logs.log',
    filemode='w')

logger = logging.getLogger(__name__)


#debug set up
#debug_formatter = logging.Formatter('%(asctime)s: ln %(lineno)d:       %(message)s')

#debug_handler = logging.FileHandler('debug.log')
#debug_handler.setLevel(logging.DEBUG)
#debug_handler.setFormatter(debug_formatter)

debug_stream = logging.StreamHandler()
debug_stream.setLevel(logging.DEBUG)
#debug_stream.setFormatter(info_formatter)

#info setup
info_formatter = logging.Formatter('%(asctime)s - %(message)s')

#info_handler = logging.FileHandler('info.log')
#info_handler.setLevel(logging.ERROR)
#info_handler.setFormatter(info_formatter)

#info_stream = logging.StreamHandler()
#info_stream.setLevel(logging.INFO)
#info_stream.setFormatter(info_formatter)


#debug_stream = logging.StreamHandler()
#debug_stream.setFormatter(debug_formatter)

#warning setup
#warning_formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

#warning_handler = logging.FileHandler('warn.log')
#warning_handler.setLevel(logging.WARNING)
#warning_handler.setFormatter(warning_formatter)

#warn_stream = logging.StreamHandler()
#warn_stream.setLevel(logging.WARNING)
#warn_stream.setFormatter(warning_formatter)


#error setup
#error_formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

#error_handler = logging.FileHandler('err.log')
#error_handler.setLevel(logging.ERROR)
#error_handler.setFormatter(error_formatter)

#err_stream = logging.StreamHandler()
#err_stream.setLevel(logging.ERROR)
#err_stream.setFormatter(error_formatter)

#critical setup
#critical_formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

#critical_handler = logging.FileHandler('crit.log')
#critical_handler.setLevel(logging.CRITICAL)
#critical_handler.setFormatter(critical_formatter)

#crit_stream = logging.StreamHandler()
#crit_stram.setLevel(logging.CRITICAL)
#crit_stream.setFormatter(critical_formatter)

''''
add the handlers you want
'''
#logger.addHandler(info_stream)
logger.addHandler(debug_stream)

#logger.debug('debug file send to it.')
#logger.info('coming from Info')

