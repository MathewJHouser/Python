class Scanner():
    def scan(self):
        print("\tscan() method from Scanner class")


class Fax():
    def send(self):
        print("\tsend() method from Fax class")

    def pint(self):
        print("\tprint method from Fax class")


class Printer():
    def pint(self):
        print("\tprint method from Printer class")


class MFD_SFP(Scanner, Fax, Printer):
    pass


class MFD_SPF(Scanner, Printer, Fax):
    pass


print('Creating device following the order: Scanner, Fax, Printer')
mfd_sfp = MFD_SFP()
print('Device capabilities:')
mfd_sfp.scan()
mfd_sfp.pint()
mfd_sfp.send()

print("")
print('Creating device following the order: Scanner, Printer, Fax')
mfd_spf = MFD_SPF()
print('Device capabilities:')
mfd_spf.scan()
mfd_spf.pint()
mfd_spf.send()
