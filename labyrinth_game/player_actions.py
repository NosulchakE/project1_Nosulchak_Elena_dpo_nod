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
    if direction exits:
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
