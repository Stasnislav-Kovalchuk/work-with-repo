class Smartphone:
    def __init__(self, price, model, phone_number, memory, battery):
        self.price = price
        self.model = model
        self.phone_number = phone_number
        self.memory = memory
        self.battery = battery

    def __str__(self):
        return f"{self.price}, {self.model}, {self.phone_number}, {self.memory}, {self.battery}"

class PhoneStore:
    inventory = []

    @staticmethod
    def add_phone(smartphone):
        PhoneStore.inventory.append(smartphone)

    @staticmethod
    def find_best_phone(max_budget):
        best_phone = None
        for phone in PhoneStore.inventory:
            if phone.price <= max_budget and (best_phone is None or phone.price > best_phone.price):
                best_phone = phone
        return best_phone

    @staticmethod
    def get_phone_numbers():
        return [phone.phone_number for phone in PhoneStore.inventory]

    @staticmethod
    def list_phones_sorted_by_price():
        sorted_phones = sorted(PhoneStore.inventory, key=lambda p: p.price)
        for phone in sorted_phones:
            print(f"Smartphone {phone}")

if __name__ == "__main__":
    phone_1 = Smartphone(400, "Iphone11", "099-222-46-93", 64, "2900mph")
    phone_2 = Smartphone(600, "Iphone12", "099-333-46-93", 128, "3900mph")
    phone_3 = Smartphone(550, "Iphone13", "099-444-46-93", 256, "2500mph")
    phone_4 = Smartphone(700, "Iphone14", "099-555-46-93", 512, "4000mph")

    PhoneStore.add_phone(phone_1)
    PhoneStore.add_phone(phone_2)
    PhoneStore.add_phone(phone_3)
    PhoneStore.add_phone(phone_4)

    phone_numbers = PhoneStore.get_phone_numbers()
    print("\nList of phone numbers:")
    print(phone_numbers)

    print("\nList of phones sorted by price:")
    PhoneStore.list_phones_sorted_by_price()

    max_budget = 650

    best_phone = PhoneStore.find_best_phone(max_budget)

    if best_phone:
        print()
        print(f"The best phone within a budget of ${max_budget} is:")
        print(best_phone)
    else:
        print(f"No phones are available within a budget of ${max_budget}")

