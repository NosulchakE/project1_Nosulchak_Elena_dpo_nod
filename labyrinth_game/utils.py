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
