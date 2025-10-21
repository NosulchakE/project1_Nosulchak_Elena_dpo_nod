#!/usr/bin/env python3
from constants import ROOMS
from utils import describe_current_room
game_state = {
        "player_inventory": [],
        "current_room": "entrance",
        "game_over": False,
        "steps_taken": 0
}
def main():
    print("Игра стартует!")
    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)
    while not game_state["game_over"]:
        command = input("\nВведите команду: ").strip().lower()
        print(f"Вы ввели: {command}")
        if command == "exit":
            print("Выход из игры. До скорых встреч!")
            game_state["game_over"] = True
        else:
            print("Неизвестная команда. Доступные команды: exit, inventory, go, solve")
if __name__ == "__main__":
    main()
