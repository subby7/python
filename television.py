class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self) -> None:
        '''
        Method sets the default values for television.py
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.min_volume
        self.__channel = Television.min_channel
        self.__previous_volume = None

    def power(self) -> None:
        '''
        Method turns the tv on and off
        '''
        if not self.__status:
            self.__status = True
        else:
            self.__status = False
    def mute(self) -> None:
        '''
        Method mutes or unmutes the TV
        '''
        if self.__status:
            if not self.__muted:
                self.__previous_volume = self.__volume
                self.__muted = True
            else:
                self.__volume = self.__previous_volume
                self.__muted = False

    def channel_up(self) -> None:
        '''
        Method turns the channel up
        '''
        if self.__status:
            if self.__channel == Television.max_channel:
                self.__channel = Television.min_channel
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''
        Method turns channel down
        '''
        if self.__status:
            if self.__channel > Television.min_channel:
                self.__channel -= 1
            else:
                self.__channel = Television.max_channel

    def volume_up(self) -> None:
        '''
        Method turns the volume up
        '''
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume < Television.max_volume:
                self.__volume += 1


    def volume_down(self) -> None:
        '''
        Method turns the volume down
        '''
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume > Television.min_volume:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Method returns a string with the status, channel, and volume
        :return: String with the status, channel, and volume
        '''
        return f'Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}]'