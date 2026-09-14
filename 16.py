class Transport:

    def get_val(self, type):
        self.type = type

    def show(self):
        print("Type of Transport:", self.type)


class Bus(Transport):

    def input_val(self, seat_number, source, destination):
        self.seat_number = seat_number
        self.source = source
        self.destination = destination

    def display(self):
        self.show()
        print("Seat Number:", self.seat_number)
        print("Source:", self.source)
        print("Destination:", self.destination)

b1 = Bus()
b1.get_val("Bus")
b1.input_val(25, "Kolkata", "Delhi")
b1.display()