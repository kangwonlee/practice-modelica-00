# https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/ompython.html
import logging


import OMPython


def check_ompythion():
    logging.basicConfig(level=logging.INFO)

    # instance of OMCSession.ZMQ
    omc = OMPython.OMCSession.ZMQ()

    # run commands
    logging.info(omc.sendExpression("getVersion()"))
    logging.info(omc.sendExpression("cd()"))


if __name__ == "__main__":
    check_ompythion()
