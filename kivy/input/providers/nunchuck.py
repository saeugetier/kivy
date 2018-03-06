'''
Wii Nunchuck over I2C
'''

__all__ = ('NunchuckEventProvider', 'NunchuckEvent')

from collections import deque
from kivy.logger import Logger
from kivy.input.provider import MotionEventProvider
from kivy.input.factory import MotionEventFactory
from kivy.input.motionevent import MotionEvent

class NunchuckEvent(MotionEvent):
    def depack(self, args):
        super(NunchuckEvent, self).depack(args)


class NunchuckEventProvider(MotionEventProvider):
    __handlers__ = {}

    def start(self):
        pass

    def update(self, dispatch_fn):
        pass


    def process_frame(self, frame):
        pass