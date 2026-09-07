import random
import sys
from job import (available_jobs, completed_jobs, generate_repair,
                 generate_assembly, generate_demolish)
from tool import (toolbox, tools_for_sale, generate_hammer,
                  generate_screwdriver, generate_saw, generate_drill,
                  generate_sander, generate_pliers)


class Player:
    def __init__(self, cash, tools, skill, stress):
        self.cash = cash
        self.tools = tools
        self.skill = skill
        self.stress = stress

    def __str__(self):
        return f"Cash: {self.cash:.2f}, Skill: {self.skill:.1f}, Stress: {self.stress}"

    def __repr__(self):
        return self.__str__()


def buy_tool(name):
    tool = None
    for tool_for_sale in tools_for_sale[:]:
        if tool_for_sale.name == name:
            if player.cash >= tool_for_sale.price:
                tool = tool_for_sale
                tools_for_sale.remove(tool_for_sale)
                player.cash -= tool_for_sale.price
                print(f"Successfully bought {tool_for_sale.name}!")
            else:
                print("Not enough cash to buy this tool.")
            break
    return tool


def tool_break(name):
    for tool_in_box in player.tools[:]:
        if tool_in_box.name == name:
            player.tools.remove(tool_in_box)
            break


def replenish_store():
    # Make sure there is always at least one of each tool type for sale
    required_types = ["hammer", "screwdriver", "saw", "drill", "sander", "pliers"]
    generators = {
        "hammer": generate_hammer,
        "screwdriver": generate_screwdriver,
        "saw": generate_saw,
        "drill": generate_drill,
        "sander": generate_sander,
        "pliers": generate_pliers
    }

    available_types = [t.tool_type for t in tools_for_sale]
    for req_type in required_types:
        if available_types.count(req_type) < 2:
            # Add a new tool to the store if stock is low
            new_tool = generators[req_type]()
            tools_for_sale.append(new_tool)


def replenish_jobs():
    # We no longer need to check customer_names because job.py handles recycling automatically
    while len(available_jobs) < 5:
        job_type = random.choice([generate_repair, generate_assembly, generate_demolish])
        new_job = job_type()
        available_jobs.append(new_job)


def choose_job():
    while True:
        print("Choose a job from above. (Or type 'quit' to exit)")
        choice = input("Type customer name here: ")

        if choice.lower() == 'quit':
            sys.exit(0)

        for current_job in available_jobs:
            if current_job.customer.lower() == choice.lower():

                player_tool_types = [t.tool_type for t in player.tools]
                missing_tools = [req for req in current_job.req_tools if req not in player_tool_types]

                if missing_tools:
                    print(f"You cannot do this job. You are missing: {', '.join(missing_tools)}\n")
                    break

                # Skill check
                if player.skill <= current_job.difficulty / 2:
                    print("You do not have the skill for this job.\n"
                          "If you attempt this job, your stress will increase.\n")
                    attempt = input("Attempt? y/n\n").lower()
                    if attempt == "n":
                        break
                    else:
                        stressor = round((current_job.difficulty - player.skill) / 2)
                        if stressor > 2:
                            stressor = 2
                        player.stress += stressor

                tools_used = []
                for req in current_job.req_tools:
                    for t in player.tools:
                        if t.tool_type == req and req not in tools_used:
                            if random.random() < 0.5:
                                t.durability -= round(current_job.time / 4)
                            tools_used.append(req)
                            break

                available_jobs.remove(current_job)
                current_job.completed = True
                completed_jobs.append(current_job)

                player.skill += (current_job.difficulty + current_job.time) / 20

                print("Job completed!\n")
                return current_job
        else:
            print("Customer not found or job aborted. Please try again.\n")


cash = 100.00
tools = []
skill = 1
stress = 1
player = Player(cash, tools, skill, stress)

day = 0
player.tools = toolbox

if __name__ == "__main__":
    print("Handyman Simulator\n")
    while True:
        day += 1
        print(f"--- Day {day} ---")
        if day % 7 == 0:
            print("You wake up feeling rested today. -1 Stress")
            player.stress -= 1

        # Check if stress is too high
        if player.stress >= 10:
            print("Your stress reached critical levels! Game over!.")
            break

        if day % 10 == 0:
            print("Rent due! Cash - $200")
            player.cash -= 200

        # Iterate on a copy of player.tools because tool_break modifies the original list
        for toolp in player.tools[:]:

            if toolp.durability <= 0:
                print(f"\n*** Your {toolp.tool_type}, {toolp.name}, has broken! ***")
                tool_break(toolp.name)

                replenish_store()  # Restock the store so there is always a replacement available

                buy = input(f"Buy a new {toolp.tool_type}? y/n\n").lower()
                if buy == "y":
                    available_tools = []
                    for toolk in tools_for_sale:
                        if toolk.tool_type == toolp.tool_type:
                            available_tools.append(toolk)

                    if not available_tools:
                        print("Sorry, there are no tools of that type for sale right now.\n")
                    else:
                        print("\nAvailable Replacements:")
                        for t in available_tools:
                            print(t)
                        new_tool = input("Choose a tool from above.\n"
                                         "Input tool's name here: ")
                        new_bought_tool = buy_tool(new_tool)
                        if new_bought_tool:
                            player.tools.append(new_bought_tool)
        print("Your tools:\n")

        for player_tool in player.tools:
            print(player_tool)
        print("\nAvailable jobs:\n")
        replenish_jobs()  # Ensure there are always jobs
        for job_item in available_jobs:
            print(job_item)
        print('')
        print(player)
        todays_job = choose_job()
        print(todays_job)
        player.cash += todays_job.pay
        print(f"You earned ${todays_job.pay:.2f}!\n")
