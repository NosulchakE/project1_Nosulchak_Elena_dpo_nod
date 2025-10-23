#!/usr/bin/env python3
from labyrinth_game.constants import ROOMS, COMMANDS
from labyrinth_game.utils import describe_current_room, solve_puzzle, attempt_open_treasure, show_help, pseudo_random, trigger_trap
from labyrinth_game.player_actions import get_input, move_player, take_item, show_inventory, use_item
game_state = {
        "player_inventory": [],
        "current_room": "entrance",
        "game_over": False,
        "steps_taken": 0
}
def process_command(game_state, command):
    parts = command.split()
    if not parts:
        print("Введите команду.")
        return

    cmd = parts[0]
    arg = " ".join(parts[1:]) if len(parts)>1 else None
    directions = ["north", "south", "east", "west"]
    if cmd in directions:
        move_player(game_state, cmd)
        return

    match cmd:
        case "look":
            describe_current_room(game_state)
        case "go":
            if arg:
                move_player(game_state, arg)
            else:
                print("Укажите направление. Пример: go north")
        case "take":
            if arg == "treasure_chest":
                print("Вы не можете поднять сундук, он слишком тяжелый!")
            elif arg:
                take_item(game_state, arg)
            else:
                print("Укажите предмет. Пример: take torch")

        case "use":
            if arg:
                use_item(game_state, arg)
            else:
                print("Что использовать? Используйте: use <предмет>")
        case "inventory":
            show_inventory(game_state)
        case "solve":
            if game_state["current_room"] == "treasure_room":
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)
        case "open":
            attempt_open_treasure(game_state)
        case "help":
            show_help()
        case "exit":
            print("Выход из игры. До скорых встреч!")
            game_state["game_over"] = True
        case "quit":
            print("Выход из игры. До скорых встреч!")
            game_state["game_over"] = True
        case _:
            print("Неизвестная команда. Введите 'help' из списка команд")
            

def main():
    print("Игра стартует!")
    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)
    while not game_state["game_over"]:
        command = get_input("\nВведите команду: ").lower()
        process_command(game_state, command)
   
if __name__ == "__main__":
    main()

