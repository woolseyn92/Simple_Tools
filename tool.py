import random


class Tool:
    def __init__(self, name, tool_type, use, durability, weight, price):
        self.name = name
        self.tool_type = tool_type
        self.use = use
        self.durability = durability
        self.weight = weight
        self.price = price

    def __str__(self):
        return (f"{self.name} - Tool Type: {self.tool_type} - Use: {self.use}. "
                f"Durability: {self.durability} - Weight: {self.weight} - Price: {self.price}\n")

    def __repr__(self):
        return self.__str__()


class Hammer(Tool):
    def __init__(self, name, durability, weight, price):
        super().__init__(name, "hammer", "Drives nails", durability, weight, price)


class Screwdriver(Tool):
    def __init__(self, name, durability, weight, price):
        super().__init__(name, "screwdriver", "Drives screws", durability, weight, price)


class Saw(Tool):
    def __init__(self, name, durability, weight, price):
        super().__init__(name, "saw", "Cuts wood", durability, weight, price)


class Drill(Tool):
    def __init__(self, name, durability, weight, price):
        super().__init__(name, "drill", "Drills holes", durability, weight, price)


class Sander(Tool):
    def __init__(self, name, durability, weight, price):
        super().__init__(name, "sander", "Sands wood", durability, weight, price)


class Pliers(Tool):
    def __init__(self, name, durability, weight, price):
        super().__init__(name, "pliers", "Grips objects", durability, weight, price)


def generate_hammer():
    return Hammer(random.choice(tool_names), random.randint(4, 10),
                  random.randint(5, 10), random.randint(1, 20) - 0.01)


def generate_screwdriver():
    return Screwdriver(random.choice(tool_names), random.randint(1, 10),
                       random.randint(1, 5), random.randint(1, 20) - 0.01)


def generate_saw():
    return Saw(random.choice(tool_names), random.randint(1, 10),
               random.randint(1, 5), random.randint(1, 20) - 0.01)


def generate_drill():
    return Drill(random.choice(tool_names), random.randint(1, 10),
                 random.randint(1, 5), random.randint(1, 20) - 0.01)


def generate_sander():
    return Sander(random.choice(tool_names), random.randint(1, 10),
                  random.randint(1, 5), random.randint(1, 20) - 0.01)


def generate_pliers():
    return Pliers(random.choice(tool_names), random.randint(1, 10),
                  random.randint(1, 5), random.randint(1, 20) - 0.01)


tool_names = [
    "Ol' Reliable",
    "The Persuader",
    "Sir Fix-A-Lot",
    "Trusty Rusty",
    "The Fixinator",
    "Major Malfunction",
    "The Workhorse",
    "Professor Tinkers",
    "General Assembly",
    "The DIY Machine",
    "Lil' Helper",
    "The Contraption",
    "Gordon's Deathtrap",
    "Toolie",
    "Mr. Repair",
    "Bob The Builder",
    "Constructor",
    "Big Bertha"
]

toolbox = []

ol_hitty = Hammer("Ol' Hitty", 10, 7, 9.99)
twisty = Screwdriver("Twisty McGee", 7, 3, 5.99)
toothed = Saw("The Toothed Menace", 4, 4, 12.99)
drill_sgt = Drill("Drill Sergeant", 2, 8, 19.99)
col_sander = Sander("Colonel Sander", 6, 5, 14.99)
squeeze = Pliers("Squeeze", 9, 2, 4.99)

toolbox.append(ol_hitty)
toolbox.append(twisty)
toolbox.append(toothed)
toolbox.append(drill_sgt)
toolbox.append(col_sander)
toolbox.append(squeeze)

tools_for_sale = []

for i in range(0, 3):
    hammer = generate_hammer()
    tools_for_sale.append(hammer)
    screwdriver = generate_screwdriver()
    tools_for_sale.append(screwdriver)
    saw = generate_saw()
    tools_for_sale.append(saw)
    drill = generate_drill()
    tools_for_sale.append(drill)
    sander = generate_sander()
    tools_for_sale.append(sander)
    pliers = generate_pliers()
    tools_for_sale.append(pliers)
    
toolbox.sort(key=lambda x: x.tool_type)
tools_for_sale.sort(key=lambda x: x.tool_type)
