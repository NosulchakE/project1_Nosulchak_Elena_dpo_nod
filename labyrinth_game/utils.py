from labyrinth_game.constants import ROOMS
import math
from game_data import game_map
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
    puzzle = ROOMS[current_room]["puzzle"]

    if not puzzle:
        print("Загадок здесь нет.")
        return

    question, correct_answer = puzzle
    print(f"Загадка: {question}")
    player_answer = input("Ваш ответ: ").strip().lower()

    alt_answer = {
        "10": ["10", "десять", "ten"],
        "шаг шаг шаг": ["шаг шаг шаг", "шаги", "шаг три раза"],
        "резонанс": ["резонанс"],
        "8": ["8", "восемь"],
        "огонь": ["огонь", "пламя", "пламень"]
    }
    valid_answer = alt_answer.get(correct_answer, [correct_answer])
    if player_answer in valid_answer:
        print("Верно! Загадка решена.")

        ROOMS[current_room]["puzzle"] = None

        if current_room == "hall":
            print("Вы получили ключ от сокровищницы!")
            game_state["player_inventory"].append(treasure_key")
        elif current_room == "trap_room":
            print("Вы обезвредили ловушку!")
        elif current_room == "library":
            print("Вы нашли секрет в книге и усилили свой меч!")
        elif current_room == "garden":
            print("Вам вручили волшебный амулет!")
            game_state["player_inventory"].append("magic_amulet")
    else:
        print("Неверною Попробуйте снова.")
        if current_room == "trap_room":
            trigger_trap(game_state)

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

def pseudo_random(seed, modulo):
    x = math.sin(seed*12.9898)*43758.5453
    x = x - math.floor(x)
    return int(x*modulo)

def trigger_trap(game_state):
    print("\nЛовушка активирована! Пол начал дрожжать и стены сдвигаются...")
    inventory = game_state("player_inventory", [])

    if inventory:
        index = pseudo_random(game_state["steps_taken"], len(inventory))
        lost_item = inventory.pop(index)
        print(f"Вы не удержали равновесие и потеряли предмет: {lost_item}!")
    else:
        danger = pseudo_random(game_state["steps_taken"], 10)
        if danger < 3:
            print("Ловушка оказалась смертельной...Вы проиграли.")
            game_state["game_over"] = True
        else:
            print("Вам чудом удалось выбраться из ловушки! Но это было опасно...")

def random_event(game_state):
    chance = pseudo_random(game_state["steps_taken"], 10)
    if chance != 0:
        return
    print("\nНеожиданное событие!")

    event_type = pseudo_random(game_state["steps_taken"] +1, 3)

    current_room = game_state["current_room"]
    inventory = game_state["player_inventory"]
    room_data = game_map[current_room]

    if event_type == 0:
        print("Вы замечаете, что на полу что-то блестит...Это монетка!")
        room_data["items"].append("coin")

    elife event_type == 1:
        print("Из тени раздается странный шорох...")
        if "sword" in inventory:
            print("Вы вскидываете меч - и существо убегает прочь.")
        else:
            print("Вы стоите неподвижно, стараясь не дышать. Кажется, пронесло...")
        elife event_type == 2:
            if current_room == "trap_room" and "torch" not in inventory:
                print("В темноте что-то щелкнуло - возможно ловушка!")
                trigger_trap(game_state)
            else:
                print("Вы чувствуете легкий сквозняк... но ничего не происходит.")
