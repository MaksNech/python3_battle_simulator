import time


class Timer:

    def get_current_time(self) -> int:
        """
        Get current time in milliseconds.
        :return: (int)
        """
        return int(round(time.time() * 1000))
