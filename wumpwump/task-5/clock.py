# clock.py

"""Provide a Clock class that uses the 24-hour format."""

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60

class Clock:

    """Represent a time on a 24-hour clock."""

    def __init__(self, hour=0, minute=0):
        """Create a clock with the given time (00:00 by default).

        Precondition: hour and minute are valid
        Raise: ValueError if the time is invalid."""

        if 0 <= hour < HOURS_PER_DAY and 0 <= minute < MINUTES_PER_HOUR:
            self.__hour = hour
            self.__minute = minute
        else:
            raise ValueError('Invalid time %02d:%02d' % (hour, minute))
    def increment_hour(self):
        self.__hour +=1
        if self.__hour >=HOURS_PER_DAY:
            self.__hour=0
    def increment_minute(self):
        """Increment the minute."""
        self.__minute += 1
        if self.__minute >= MINUTES_PER_HOUR:
            self.__minute = 0
            self.increment_hour()

    
    def get_hour(self):
        return self.__hour
    def get_minute(self):
        return self.__minute

    def set_time(self,hour,minute):
        if 0 <= hour < HOURS_PER_DAY and 0 <= minute < MINUTES_PER_HOUR:

            self.__hour=hour
            self.__minute=minute
        else:
            raise ValueError('Invalid time %02d:%02d' % (hour, minute))

    def __eq__(self, obj):
        return '%s:%s'%(str(self.__hour),str(self.__minute)) == '%s:%s'%(str(obj.__hour),str(obj.__minute))
  

    def __str__(self):
        """Create a string representation in format (%.2f, %.2f)."""
        return '%.2d:%.2d' % (self.__hour, self.__minute)




# test_clock.py

