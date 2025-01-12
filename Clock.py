import time

class Clock:
    '''
    A digital clock class that provides various time-related functionalities.

    Attributes:
        Time_info (time.struct_time): Stores the current local time information.
        Actual_Day (int): Current day of the month.
        Actual_Day_Week (str): Name of the current day of the week.
        Actual_Hour (int): Current hour of the day (24-hour format).
        Actual_Min (int): Current minute of the hour.
        Actual_Sec (int): Current second of the minute.

    Methods:
        Get_Real_Time() -> str: Returns the current time as a formatted string in `HH:MM:SS`.
        CalcTime(hour: int, minute: int) -> tuple[int, int]: Calculates the time remaining until a specified target time.
        Alarm(hour: int, minute: int) -> None: Sets an alarm for a specified time.
        Timer(hour: int, minute: int) -> None: Sets a countdown timer for a specified duration.
        Chronometer() -> None: Starts a chronometer that counts up from zero.
    '''

    def __init__(self):
        '''
        Initializes the clock with current time attributes.
        '''
        self.Time_info = time.localtime()
        self.Actual_Day = self.Time_info.tm_mday
        self.Actual_Day_Week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][self.Time_info.tm_wday]
        self.Actual_Hour = self.Time_info.tm_hour
        self.Actual_Min = self.Time_info.tm_min
        self.Actual_Sec = self.Time_info.tm_sec

    def Get_Real_Time(self) -> str:
        '''
        Returns the current time as a string in the format `HH:MM:SS`.
        '''
        self.Time_info = time.localtime()
        return f'{str(self.Time_info.tm_hour).zfill(2)}:{str(self.Time_info.tm_min).zfill(2)}:{str(self.Time_info.tm_sec).zfill(2)}'

    def CalcTime(self, hour: int, minute: int) -> tuple[int, int]:
        '''
        Calculates the remaining time until the specified hour and minute.

        Args:
            hour (int): Target hour (0-23).
            minute (int): Target minute (0-59).

        Returns:
            tuple[int, int]: Hours and minutes remaining until the target time.
        '''
        actual = list(map(int, self.Get_Real_Time().split(':')))

        if hour > actual[0] or (hour == actual[0] and minute > actual[1]):
            return (hour - actual[0], abs(minute - actual[1]))

        remaining_hour = (hour + 24 - actual[0]) % 24
        remaining_minute = (minute - actual[1]) if minute >= actual[1] else (minute + 60 - actual[1])
        if minute < actual[1]:
            remaining_hour -= 1

        return remaining_hour, remaining_minute

    def Alarm(self, hour: int, minute: int) -> None:
        '''
        Sets an alarm to go off at the specified time.

        Args:
            hour (int): Target hour (0-23).
            minute (int): Target minute (0-59).

        Raises:
            ValueError: If hour or minute is out of valid range.
        '''
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            raise ValueError('Invalid time input. Hours must be in 0-23 and minutes in 0-59 range.')

        time_left = self.CalcTime(hour, minute)
        print(f'Alarm set to ring in {time_left[0]} hours and {time_left[1]} minutes.')
        print('Press Ctrl + C to cancel the alarm.')

        try:
            while True:
                if self.Get_Real_Time().split(':')[:2] == [str(hour).zfill(2), str(minute).zfill(2)]:
                    print('ALARM IS RINGING!!!')
                    break
        except KeyboardInterrupt:
            print('Alarm cancelled.')

    def Timer(self, hour: int, minute: int) -> None:
        '''
        Sets a countdown timer for the specified duration.

        Args:
            hour (int): Duration in hours.
            minute (int): Duration in minutes.

        Raises:
            ValueError: If hour or minute is out of valid range.
        '''
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            raise ValueError('Invalid time input. Hours must be in 0-23 and minutes in 0-59 range.')

        print(f'Timer set for {hour} hours and {minute} minutes. Press Ctrl + C to cancel.')

        try:
            target_hour, target_minute = divmod(self.CalcTime(hour, minute)[0] * 60 + minute, 60)
            self.Alarm(target_hour, target_minute)
        except KeyboardInterrupt:
            print('Timer cancelled.')

    def Chronometer(self) -> None:
        '''
        Starts a chronometer that counts up from zero.

        The chronometer displays hours, minutes, and seconds and updates every second.
        '''
        print('Chronometer started. Press Ctrl + C to stop.')
        hours, minutes, seconds = 0, 0, 0

        try:
            while True:
                time.sleep(1)
                seconds += 1
                if seconds == 60:
                    seconds = 0
                    minutes += 1
                if minutes == 60:
                    minutes = 0
                    hours += 1

                print(f'{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}', end='\r')
        except KeyboardInterrupt:
            print('\nChronometer stopped.')


# Example usage
clock = Clock()

# Alarm
clock.Alarm(19, 30)

# Timer
clock.Timer(19, 30)

# Chronometer
clock.Chronometer()