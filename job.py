import random


class Job:
    def __init__(self, customer, task, item, time, pay, req_tools, difficulty, completed):
        self.customer = customer
        self.task = task
        self.item = item
        self.time = time
        self.pay = pay
        self.req_tools = req_tools
        self.difficulty = difficulty
        self.completed = completed

    def __str__(self):
        return (f"|{self.customer}| needs someone to {self.task} their {self.item}. "
                f"Time: {self.time}hr - Pay: ${self.pay:.2f} - "
                f"Required Tools: {self.req_tools} - Difficulty: {self.difficulty}\n")

    def __repr__(self):
        return self.__str__()


class Repair(Job):
    def __init__(self, customer, item, time, pay, difficulty):
        super().__init__(customer, "repair", item, time, pay,
                         ["pliers", "screwdriver", "sander"], difficulty, False)


class Assembly(Job):
    def __init__(self, customer, item, time, pay, difficulty):
        super().__init__(customer, "assemble", item, time, pay,
                         ["drill", "hammer", "screwdriver"], difficulty, False)


class Demolish(Job):
    def __init__(self, customer, item, time, pay, difficulty):
        super().__init__(customer, "demolish", item, time, pay,
                         ["hammer", "saw", "drill"], difficulty, False)


available_jobs = []

customer_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan",
                  "Fiona", "George", "Hannah", "Ian", "Julia",
                  "Kevin", "Liam", "Mia", "Noah", "Olivia",
                  "Paul", "Quinn", "Rachel", "Sam", "Tara"]

items = ["bookshelf", "dining table", "chair", "cabinet", "bed frame",
         "desk", "wardrobe", "coffee table", "sofa", "deck",
         "fence", "shed", "door", "window", "dresser",
         "nightstand", "tv stand", "patio furniture"]

used_names = []


def _get_customer_name():
    """Helper to cleanly extract a customer name and recycle the list if needed."""
    if not customer_names:
        # If the pool is empty, recycle all used names
        customer_names.extend(used_names)
        used_names.clear()
        
    customer = random.choice(customer_names)
    customer_names.remove(customer)
    used_names.append(customer)
    return customer


def generate_repair():
    customer = _get_customer_name()
    item = random.choice(items)  # We no longer remove from items
    time = random.randint(1, 4)
    difficulty = random.randint(3, 6)
    pay = ((difficulty + time) * 7) - random.random()
    return Repair(customer, item, time, pay, difficulty)


def generate_assembly():
    customer = _get_customer_name()
    item = random.choice(items)
    time = random.randint(3, 6)
    difficulty = random.randint(1, 7)
    pay = ((difficulty + time) * 9) - random.random()
    return Assembly(customer, item, time, pay, difficulty)


def generate_demolish():
    customer = _get_customer_name()
    item = random.choice(items)
    time = random.randint(1, 8)
    difficulty = random.randint(4, 10)
    pay = ((difficulty + time) * 8) - random.random()
    return Demolish(customer, item, time, pay, difficulty)


for i in range(0, 3):
    repair = generate_repair()
    available_jobs.append(repair)
    assembly = generate_assembly()
    available_jobs.append(assembly)
    demolish = generate_demolish()
    available_jobs.append(demolish)

available_jobs.sort(key=lambda x: x.difficulty)
completed_jobs = []
