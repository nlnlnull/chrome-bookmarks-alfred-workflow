# -*- coding: utf-8 -*-
import time
import os
from feedback import Feedback
from settings import Settings, ImmutableSettings

_NON_PERSISTENT_PATH = '~/Library/Caches/com.runningwithcrayons.Alfred-2/Workflow Data'
_PERSISTENT_PATH = '~/Library/Application Support/Alfred 2/Workflow Data'


class Workflow:
    def __init__(self):
        self.preferences = ImmutableSettings('info.plist')
        self.id = self.preferences.get('bundleid')
        self.settings = Settings(os.path.join(self.path(True), self.id, 'settings.plist'))
        self.feedback = Feedback()

    def path(self, persistent=False):
        return _PERSISTENT_PATH if persistent else _NON_PERSISTENT_PATH

    def cid(self, value):
        return u'-'.join(map(unicode, (self.id, value)))

    def uid(self):
        return self.cid(time.time())