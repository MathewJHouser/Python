import abc

class Scanner(abc.ABC):
    def scan_document(self):
        return "The document has been scanned. "

    @abc.abstractmethod
    def get_scanner_status(self):
        pass

class Printer(abc.ABC):
    def print_document(self):
        return "The document has been printed. "

    @abc.abstractmethod
    def get_printer_status(self):
        pass

class MFD1(Scanner, Printer):
    def get_scanner_status(self):
        return "Scan Resolution: Low \t | \t Serial Number: ABC"

    def get_printer_status(self):
        return "Print Resolution: Low \t | \t Serial Number: DEF"

class MFD2(Scanner, Printer):
    def get_scanner_status(self):
        return "Scan Resolution: Fine \t | \t Serial Number: GHI"

    def get_printer_status(self):
        return "Print Resolution: Fine \t | \t Serial Number: JKL"

    def print_history(self):
        return "Recently Printed Documents: .... "

class MFD3(Scanner, Printer):
    def get_scanner_status(self):
        return "Scan Resolution: High \t | \t Serial Number: MNO"

    def get_printer_status(self):
        return "Print Resolution: High \t | \t Serial Number: PQR"

    def print_history(self):
        return "Recently Printed Documents: .... "

    def send_fax(self):
        return "Sending Fax"

    def receive_fax(self):
        return "Receiving Fax"


mfd1 = MFD1()
print(mfd1.print_document())
print(mfd1.get_printer_status())

mfd2 = MFD2()
print(mfd2.print_document())
print(mfd2.get_printer_status())

mfd3 = MFD3()
print(mfd3.print_document())
print(mfd3.get_printer_status())