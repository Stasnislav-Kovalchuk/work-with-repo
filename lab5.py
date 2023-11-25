"""
This is lab5
"""
class Smartphone:
    """
    This is class where write my parameter
    """
    def __init__(self, price, model, phone_number, memory, battery):
        self.price = price
        self.model = model
        self.phone_number = phone_number
        self.memory = memory
        self.battery = battery

    def __str__(self):
        """
        This is method str
        """
        return f"{self.price}, {self.model}, {self.phone_number}, {self.memory}, {self.battery}"

    def see_price(self):
        """
        this function return my phone price
        """
        return f"Phone price: {self.price}"


class PhoneStore:
    """
    this class where my phones
    """


    @staticmethod
    def add_phone(smartphone):
        This function append smartphone to inventory
        """
        self.inventory.append(smartphone)

    def find_best_phone(self, max_budget):
        """
        This function find best phone
        """
        best_phone = None
        for phone in self.inventory:
            if phone.price <= max_budget and (best_phone is None or phone.price > best_phone.price):
                best_phone = phone
        return best_phone

    def get_phone_numbers(self):
        """
        This function returned my phone number inventory
        """
        return [phone.phone_number for phone in self.inventory]

    def list_phones_sorted_by_price(self):
        """
        This function sort my phone to price
        """
        self.inventory.sort(key=lambda p: p.price)
        for phone in self.inventory:
            print(f"Smartphone: {phone}")


"""
This module demonstrates the use of the Smartphone and PhoneStore classes.
"""

if __name__ == "__main__":
    phone_1 = Smartphone(400, "Iphone11", "099-222-46-93", 64, "4000mph")
    phone_2 = Smartphone(600, "Iphone12", "099-333-46-93", 128, "3200mph")
    phone_3 = Smartphone(550, "Iphone13", "099-444-46-93", 256, "3100mph")
    phone_4 = Smartphone(700, "Iphone14", "099-555-46-93", 512, "2900mph")
    phone_store = PhoneStore()

    phone_store.add_phone(phone_1)
    phone_store.add_phone(phone_2)
    phone_store.add_phone(phone_3)
    phone_store.add_phone(phone_4)

    phone_numbers = PhoneStore.get_phone_numbers(phone_store)
    print("\nList of phone numbers:")
    print(phone_numbers)

    print("\nList of phones sorted by price:")
    PhoneStore.list_phones_sorted_by_price(phone_store)

    MAX_BUDGET = 650

    best_phone = phone_store.find_best_phone(MAX_BUDGET)

    if best_phone:
        print()
        print(f"The best phone within a budget of ${MAX_BUDGET} is:")
        print(best_phone)
    else:
        print(f"No phones are available within a budget of ${MAX_BUDGET}")

