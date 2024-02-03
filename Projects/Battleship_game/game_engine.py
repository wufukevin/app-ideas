import random
from typing import List


class ship:
    def __init__(self, x, y, direction, ship_length):
        self.direction = direction
        self.ship_length = ship_length
        self.ship_location = [(x+i, y) for i in range(ship_length)
                              ] if direction == "horizontal" else [(x, y+i) for i in range(ship_length)]

    def crush(self, other):
        for point in self.ship_location:
            if point in other.ship_location:
                return True
        return False

    def __str__(self) -> str:
        return f"Ship location: {self.ship_location}"


class battlefield_data:
    def __init__(self, player_number):
        self.player_number = player_number
        self.placed_ships:List[ship] = []
        self.shooed_points = []


class Battleship_engine:
    def __init__(self, width, height, ship_a_count=1, ship_b_count=1, ship_c_count=1, player_count=1):
        # ship_a: 1*2
        # ship_b: 1*3
        # ship_c: 1*4
        self.width = width
        self.height = height
        self.ship_a_count = ship_a_count
        self.ship_b_count = ship_b_count
        self.ship_c_count = ship_c_count
        self.player_count = player_count
        self.battlefield_data = [
            battlefield_data(i) for i in range(self.player_count)]
        for data in self.battlefield_data:
            self.layout(data)
            for ship in data.placed_ships:
                print(ship)
        print("Game start")

    def layout(self, battlefield_data):
        for i in range(self.ship_c_count):
            while not self.place_ship("ship_c", battlefield_data):
                pass
        for i in range(self.ship_b_count):
            while not self.place_ship("ship_b", battlefield_data):
                pass
        for i in range(self.ship_a_count):
            while not self.place_ship("ship_a", battlefield_data):
                pass

    def check_boundary(self, ship: ship):
        if ship.direction == "horizontal":
            if ship.ship_location[-1][0] >= self.width:
                return False
        else:
            if ship.ship_location[-1][1] >= self.height:
                return False
        return True

    def place_ship(self, ship_type, battlefield_data: battlefield_data):
        temp_ship = ship(random.randint(0, self.width - 1), random.randint(0, self.height - 1),
                         random.choice(["horizontal", "vertical"]),
                         2 if ship_type == "ship_a" else 3 if ship_type == "ship_b" else 4)
        result = self.check_boundary(temp_ship) and not any(temp_ship.crush(
            placed_ship) for placed_ship in battlefield_data.placed_ships)
        if result:
            battlefield_data.placed_ships.append(temp_ship)
        return result

    def get_placed_ships(self, player_number=0):
        return self.battlefield_data[player_number].placed_ships

    def shoot(self, x, y, player_number=0):
        for ship in self.battlefield_data[player_number].placed_ships:
            for point in ship.ship_location:
                if point == (x, y):
                    ship.ship_location.remove(point)
                    self.battlefield_data[player_number].shooed_points.append(
                        point)
                    if len(ship.ship_location) == 0:
                        self.battlefield_data[player_number].placed_ships.remove(
                            ship)
                    return True
        for point in self.battlefield_data[player_number].shooed_points:
            if point == (x, y):
                return True
        return False

    def is_game_over(self):
        for data in self.battlefield_data:
            if len(data.placed_ships) != 0:
                return False
        return True
