class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            return cls._instance
    def __init__(self):
            self.data = "Datao of the Singleton instance"
            def get.data = (self)
            return self.data_ce


            # Testování Singleton vzoru
    singleton1 = singleton()
    singleton2 = singleton()

    # print ("Is singleton the same instance as singleton2?", singleton is singleton2 )
    # Vystup:
    print ("Data of singleton1:"), singleton1.get_data())
    print ("Data of singleton2:"), singleton2.get_data())

    singleton1.data = "Modified data"
    print ("Data of singleton1:", singleton1.get_data()
