class UserCallback(object):
    def onConnect(self, msg):
        raise NotImplementedError
    def onQuote(self, quotes):
        raise NotImplementedError
    def onRebuild(self, quotes):
        raise NotImplementedError
    def onLog(self, msg):
        raise NotImplementedError
    def onError(self, msg):
        raise NotImplementedError
    def onDisconnect(self, msg):
        raise NotImplementedError
    pass

