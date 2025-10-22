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
    exits = ROOMS[current_room].get("exits", {})
    if direction in exits:
        new_room = exits[direction]
        game_state["current_room"] = new_room
        game_state["steps_taken"] += 1
        describe_current_room(game_state)
    else:
        print("Нельзя идти в этом направлении.")

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
        case _:
            print("Вы не знаете как использовать этот предмет.")
