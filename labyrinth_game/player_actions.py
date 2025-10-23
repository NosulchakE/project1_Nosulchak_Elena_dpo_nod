from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room, random_event
def show_inventory(game_state):
    inventory = game_state["player_inventory"]
    if inventory:
        print("\nВаш инвентарь:")
        for item in inventory:
            print(f" - {item}")
    else:
        print("\nВаш инвентарь пуст")

def get_input(prompt = ">"):
    try:
        user_input = input(prompt).strip()
        return user_input
    except (KeyboardInterrupt, EOFError):
        print("\Выход из игры.")
        return "quit"

def move_player(game_state, direction):
    current_room = game_state["current_room"]
    exits = ROOMS[current_room]["exits"]
    if direction not in exits:
        print("Нельзя идти в этом направлении.")
        return

    next_room = exits[direction]
    if next_room == "treasure_room":
        if "rusty_key" in game_state["player_inventory"]:
            print("Вы используете найденный ключ, чтобы открыть путь в комнату сокровищ.")
        else:
            print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
            return

    game_state["current_room"] = next_room
    game_state["steps_taken"] += 1

    describe_current_room(game_state)

    try:
        random_event(game_state)
    except NameError:
        pass 

def take_item(game_state, item_name):
    current_room = game_state["current_room"]
    room_items = ROOMS[current_room].get("items", [])
    if item_name in room_items:
        game_state["player_inventory"].append(item_name)
        room_items.remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")
    if item_name == "treasure_chest":
        print("Вы не сможете поднять сундук. он слишком тяжелый.")
        return

def use_item(game_state, item_name):
    inventory = game_state["player_inventory"]
    if item_name not in inventory:
        print("У вас нет такого предмета.")
        return
    match item_name:
        case "torch":
            print("Вы зажгли факел. Теперь стало светлее и вы чувствуете себя увереннее.")
        case "sword":
            print("Вы сжали меч в руке. Никакие преграды не остановят вас!")
        case "bronze_box":
            print("Вы открыли бронзовую шкатулку...внутри что-то есть!")
            if "rusty key" not in inventory:
                inventory.append("rusty key")
                print("Вы нашли предмет: rusty key.")
            else:
                print("Но внутри пусто - вы уже забрали все ценное.")
        case "rusty_key":
            current_room = game_state["current_room"]
            if current_room == "hall":
                print("Вы используете найденный ключ, чтобы открыть путь в комнату сокровищ.")
            else:
                print("Вы осматриваете ключ, но пока не знаете, куда его применить.")
        case _:
            print("Вы не знаете как использовать этот предмет.")
