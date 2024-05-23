class shared_memory(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(shared_memory, cls).__new__(cls)
        return cls.instance