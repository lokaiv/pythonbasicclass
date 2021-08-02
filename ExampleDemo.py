class USB:
    def __init__(self,capacity):
        self.capacity = capacity

    def info(self):
        print('{}GB USB'.format(self.capacity))

usb = USB(64)
usb.info()


class Service:
    def __init__(self,service):
        self.service = service
        print('{} Service has started'.format(self.service))

    def __del__(self):
        print('{}Service has been shut down'.format(self.service))

s = Service('Direction guidance')
del s