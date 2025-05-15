class MobilePhone:
    def __init__(self, number):
        self.number = number

    def turn_on(self):
        print("mobile phone " + str(self.number) + " is turned on.")

    def turn_off(self):
        print("mobile phone " + str(self.number) + " is turned off.")

    def call(self, number):
        print("calling " + str(number))


phone_1 = MobilePhone("01632-960004")
phone_2 = MobilePhone("01632-960012")
phone_1.turn_on()
phone_2.turn_on()
phone_1.call(phone_2.number)
phone_1.turn_off()
phone_2.turn_off()