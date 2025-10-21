def show_inventory(game_state):
    inventory = game_state["player_inventory"]
    if inventory:
        print("\nВаш инвентарь:")
        for item in inventory:
            print(f " - {item}")
    else:
        print("\nВаш инвентарь пуст")
