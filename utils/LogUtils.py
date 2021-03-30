import logging
from datetime import datetime

m_logger = logging.getLogger('sudoku_mutation')
m_logger.setLevel(logging.DEBUG)

c_logger = logging.getLogger('sudoku_crossover')
c_logger.setLevel(logging.DEBUG)

dt_string = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

m_fh = logging.FileHandler('mutation-%s.log' % dt_string)
m_fh.setLevel(logging.DEBUG)
m_fh.setFormatter(formatter)
m_logger.addHandler(m_fh)

c_fh = logging.FileHandler('crossover-%s.log' % dt_string)
c_fh.setLevel(logging.DEBUG)
c_fh.setFormatter(formatter)
c_logger.addHandler(c_fh)


def log_to_all(message: str)-> None:
    m_logger.info(message)
    c_logger.info(message)
