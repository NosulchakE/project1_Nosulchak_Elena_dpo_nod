from labyrinth_game.constants import ROOMS
def describe_current_room(game_state):
    current_room = game_state["current_room"]
    room_data = ROOMS[current_room]
    print(f"\n == {current_room.upper()} ==")
    print(room_data["description"])
    if room_data["items"]:
        print("Заметные предметы")
        for item in room_data["items"]:
            print(f" - {item}")
    exits = ",".join(room_data["exits"].keys())
    print(f"Выходы: {exits}")
    if room_data["puzzle"]:
        print("Кажется здесь есть загадка (используйте команду solve).")

def solve_puzzle(game_state):
    current_room = game_state["current_room"]
    room_data = ROOMS[current_room]
    if not room_data.get("puzzle"):
        print("Загадок здесь нет.")
        return
    question, answer = room_data["puzzle"]
    print("\Загадка: ")
    print(question)
    user_answer = input("Ваш ответ: ").strip().lower()
    if user_answer == answer.lower():
        print("Верно! Загадка решена.")
        room_data["puzzle"] = None
        reward = "mysterious artifact"
        game_state["player_inventory"].append(reward)
        print(f"Вы получили награду: {reward}")
    else:
        print("Неверно. Попробуйте снова.")

def attempt_open_treasure(game_state):
    room = game_state["current_room"]
    room_data = ROOMS[room]

    if room != "treasure_room":
        print("Здесь нечего открывать.")
        return
    
    if "treasure_chest" not in room_data["items"]:
        print("Сундук уже открыт. Здесь пусто.")
        return

    if "treasure_key" in game_state["player_inventory"]:
        print("Вы применяете ключ, и замое щелкает. Сундук открыт!")
        room_data["items"].remove("treasure_chest")
        print("В сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
        return
    print("Сундук заперт. Без ключа не открыть...")
    choice = input("Хотите попробовать ввести код? (да/нет): ").strip().lower()
    if choice != "да":
        print("Вы отступаете от сундука.")
        return

    puzzle = room_data.get("puzzle")
    if not puzzle:
        print("Не видно механизма для кода...")
        return

    correct_code = puzzle[1]
    user_code = input("Введите код: ").strip().lower()

    if user_code == correct_code:
        print("Механизм щелкает - вы взломали сундук!")
        room_data["items"].remove("treasure_chest")
        print("В сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
    else:
        print("Неверно. Сундук остается закрытым.")

def show_help():
    print("\nДоступные команды:")
    print(" go <направление> - перейти (north/south/east/west)")
    print(" look    -осмотреть текущую комнату")
    print(" take <предмет>  -поднять предмет")
    print(" use <предмет>  -использовать предмет из инвентаря")
    print(" inventory  -показать инвентарь")
    print(" solve  -решить загадку или открыть сундук")
    print(" open  -попытаться открыть сундук")
    print(" help  -показать это сообщение")
    print(" quit/exit  -выйти из игры")
