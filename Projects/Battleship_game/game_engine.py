import random

class xy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # judge if two xy objects are equal
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class battlefield_data:
    def __init__(self, player_number):
        self.player_number = player_number
        self.placed_ships = []
        self.shooed_points = []

class Battleship_engine:
    def __init__(self, width, height, ship_a_count = 1, ship_b_count = 1, ship_c_count = 1, player_count = 1):
        #ship_a: 1*2
        #ship_b: 1*3
        #ship_c: 1*4
        self.width = width
        self.height = height
        self.ship_a_count = ship_a_count
        self.ship_b_count = ship_b_count
        self.ship_c_count = ship_c_count
        self.player_count = player_count
        self.battlefield_data = [battlefield_data(i) for i in range(self.player_count)]
        # self.placed_ships = []
        # self.shooed_points = []
        for data in self.battlefield_data:
            self.layout(data)
            for ship in data.placed_ships:
                for point in ship:
                    print(data.player_number, point.x, point.y)
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
    
    def place_ship(self, ship_type, battlefield_data: battlefield_data):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        direction = random.choice(["horizontal", "vertical"])
        ship_to_place = []

        if ship_type == "ship_a":
            ship_size = 2
        elif ship_type == "ship_b":
            ship_size = 3
        elif ship_type == "ship_c":
            ship_size = 4
        else:
            print("Invalid ship type")
            return None

        if direction == "horizontal":
            if x + ship_size > self.width:
                print("Invalid ship placement")
                return None
            else:
                for i in range(ship_size):
                    point = xy(x + i, y)
                    if any(point == placed_point for ship in battlefield_data.placed_ships for placed_point in ship):
                        print("Invalid ship placement")
                        return None
                    else:
                        ship_to_place.append(point)
                battlefield_data.placed_ships.append(ship_to_place)
        elif direction == "vertical":
            if y + ship_size > self.height:
                print("Invalid ship placement")
                return None
            else:
                for i in range(ship_size):
                    point = xy(x, y + i)
                    if any(point == placed_point for ship in battlefield_data.placed_ships for placed_point in ship):
                        print("Invalid ship placement")
                        return None
                    else:
                        ship_to_place.append(point)
                battlefield_data.placed_ships.append(ship_to_place)
        else:
            print("Invalid direction")
            return None
        print("Ship placed successfully")
        return True
    
    def get_placed_ships(self, player_number = 0):
        return self.battlefield_data[player_number].placed_ships
    
    def shoot(self, x, y, player_number=0):
        for ship in self.battlefield_data[player_number].placed_ships:
            for point in ship:
                if point == xy(x, y):
                    ship.remove(point)
                    self.battlefield_data[player_number].shooed_points.append(point)
                    if len(ship) == 0:
                        self.battlefield_data[player_number].placed_ships.remove(ship)
                    return True
        for point in self.battlefield_data[player_number].shooed_points:
            if point == xy(x, y):
                return True
        return False
    
    def is_game_over(self):
        for data in self.battlefield_data:
            if len(data.placed_ships) != 0:
                return False
        return True