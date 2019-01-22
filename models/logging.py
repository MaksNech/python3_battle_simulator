import logging
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from models.configurations import SIMULATOR_CONFIG as CONFIG

# ENABLE Sentry sdk: ###################################################
sentry_logging = LoggingIntegration(
    level=logging.INFO,  # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)
sentry_sdk.init(
    dsn="https://58e86215dc53446883956e21b20a5d6f@sentry.io/1376290",
    integrations=[sentry_logging]
)
########################################################################

# CONFIGURATE Logger: ###################################################
# create logger
logger = logging.getLogger('logging.py_logger')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def enable_logger():
    logger.disabled = not (CONFIG['enable_python_logging'])


#########################################################################

class BattlePythonLog():

    def logging_armies_set(self, armies_set: set) -> None:
        """
        Display in terminal armies set.
        :param armies_set: (set)
        :return: (None)
        """
        logger.debug('CURRENT ARMIES SET obj: {}'.format(armies_set))

    def logging_army_info(self, army) -> None:
        """
        Display in terminal army info.
        :param army: (Army)
        :param step: (int)
        :return: (None)
        """
        logger.debug('CURRENT ARMY obj: {}'.format(army))

    def logging_own_formation_info(self, own_formation) -> None:
        """
        Display in terminal own formation info.
        :param own_formation: Formed(abc) child class object
        :return: (None)
        """
        logger.debug('CURRENT OWN_FORMATION obj: {}'.format(own_formation))

    def logging_opposing_formation_info(self, opposing_formation) -> None:
        """
        Display in terminal opposing formation info.
        :param opposing_formation: Formed(abc) child class object
        :return: (None)
        """
        logger.debug('CURRENT OPPOSING_FORMATION obj: {}'.format(opposing_formation))

    def logging_units_recharging_info(self) -> None:
        """
        Display in terminal units recharging info
        :return: (None)
        """
        logger.debug("UNITS ARE NOT READY, RECHARGING...")

    def logging_successful_attack_info(self, own_formation, opposing_formation) -> None:
        """
        Display in terminal successful attack info.
        :param own_formation: Formed(abc) child class object
        :param opposing_formation: Formed(abc) child class object
        :return: (None)
        """
        logger.debug('SUCCESSFULL ATTACK')
        logger.debug('CURRENT OWN_FORMATION attack success probability: {}'.format(own_formation._attack_success))
        logger.debug('CURRENT OWN_FORMATION damage value to opposing: {}'.format(own_formation._last_to_damage_val))
        logger.debug(
            'CURRENT OPPOSING_FORMATION attack success probability: {}'.format(opposing_formation._attack_success))

    def logging_unsuccessful_attack_info(self, own_formation, opposing_formation) -> None:
        """
        Display in terminal unsuccessful attack info.
        :param own_formation: Formed(abc) child class object
        :param opposing_formation: Formed(abc) child class object
        :return: (None)
        """
        logger.debug('UNSUCCESSFULL ATTACK')
        logger.debug('CURRENT OWN_FORMATION attack success probability: {}'.format(own_formation._attack_success))
        logger.debug(
            'CURRENT OPPOSING_FORMATION attack success probability: {}'.format(opposing_formation._attack_success))

    def logging_destroyed_army_info(self, army) -> None:
        """
        Display in terminal destroyed army info
        :param army: (Army)
        :return: (None)
        """
        logger.debug('DESTROYED ARMY obj: {}'.format(army))

    def logging_winning_army_info(self, army) -> None:
        """
        Display in terminal winning army info
        :param army: (Army)
        :return: (None)
        """
        logger.debug('THE WINNING ARMY obj: {}'.format(army))
