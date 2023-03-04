import inspect
import logging

class LogGeneration:


    def logGen(loglevel = logging.DEBUG):

        logger_name = inspect.stack()[1][3]
        # step1:create logger object
        logger = logging.getLogger(logger_name)
        #step2: set logging level
        logger.setLevel(loglevel)
        #step3:create console handler or file handler
        fh = logging.FileHandler(".//Logs//automation.log",mode='a')   # default mode is a=append, w=overridden
        fh.setLevel(loglevel)
        #step3: create formatter on how to see our logs
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        #STEP4: Add the formatter to console handler or file handler
        fh.setFormatter(formatter)
        # step5:add ch to logger
        logger.addHandler(fh)

        return logger