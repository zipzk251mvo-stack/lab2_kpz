class Laptop:
    def get_info(self):
        pass


class Netbook:
    def get_info(self):
        pass


class EBook:
    def get_info(self):
        pass


class Smartphone:
    def get_info(self):
        pass


class IProneLaptop(Laptop):
    def get_info(self):
        return "IProne Laptop"


class IProneNetbook(Netbook):
    def get_info(self):
        return "IProne Netbook"


class IProneEBook(EBook):
    def get_info(self):
        return "IProne EBook"


class IProneSmartphone(Smartphone):
    def get_info(self):
        return "IProne Smartphone"


class KiaomiLaptop(Laptop):
    def get_info(self):
        return "Kiaomi Laptop"


class KiaomiNetbook(Netbook):
    def get_info(self):
        return "Kiaomi Netbook"


class KiaomiEBook(EBook):
    def get_info(self):
        return "Kiaomi EBook"


class KiaomiSmartphone(Smartphone):
    def get_info(self):
        return "Kiaomi Smartphone"


class BalaxyLaptop(Laptop):
    def get_info(self):
        return "Balaxy Laptop"


class BalaxyNetbook(Netbook):
    def get_info(self):
        return "Balaxy Netbook"


class BalaxyEBook(EBook):
    def get_info(self):
        return "Balaxy EBook"


class BalaxySmartphone(Smartphone):
    def get_info(self):
        return "Balaxy Smartphone"


class DeviceFactory:
    def create_laptop(self):
        pass

    def create_netbook(self):
        pass

    def create_ebook(self):
        pass

    def create_smartphone(self):
        pass


class IProneFactory(DeviceFactory):
    def create_laptop(self):
        return IProneLaptop()

    def create_netbook(self):
        return IProneNetbook()

    def create_ebook(self):
        return IProneEBook()

    def create_smartphone(self):
        return IProneSmartphone()


class KiaomiFactory(DeviceFactory):
    def create_laptop(self):
        return KiaomiLaptop()

    def create_netbook(self):
        return KiaomiNetbook()

    def create_ebook(self):
        return KiaomiEBook()

    def create_smartphone(self):
        return KiaomiSmartphone()


class BalaxyFactory(DeviceFactory):
    def create_laptop(self):
        return BalaxyLaptop()

    def create_netbook(self):
        return BalaxyNetbook()

    def create_ebook(self):
        return BalaxyEBook()

    def create_smartphone(self):
        return BalaxySmartphone()


if __name__ == "__main__":
    factory = KiaomiFactory()
    phone = factory.create_smartphone()
    laptop = factory.create_laptop()

    print(phone.get_info())
    print(laptop.get_info())