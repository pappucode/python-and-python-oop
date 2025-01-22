class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_postcode, new_dist):
        self.name = new_name
        self.address.change_address(new_city, new_postcode, new_dist)


class Address:
    def __init__(self, city, postcode, dist):
        self.city = city
        self.postcode = postcode
        self.dist = dist

    def change_address(self, new_city, new_postcode, new_dist):
        self.city = new_city
        self.postcode = new_postcode
        self.dist = new_dist



add = Address('Dhaka', 1205, 'Jamalpur')
cust = Customer("Rabiul", "Male", add)

cust.edit_profile("Pappu", "Mymensingh", 2005, "Tangail")

print(cust.address.postcode)