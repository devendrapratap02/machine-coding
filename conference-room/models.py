import json, tomllib

from dataclasses import dataclass, asdict, field

data = {}

@dataclass
class User:
    name: str

    def __repr__(self) -> str:
        return json.dumps(asdict(self))

    __key__ = "users"
    __filter__ = "name"

@dataclass
class Floor:
    name: str
    rooms: list[str]

    def __repr__(self) -> str:
        return json.dumps(asdict(self))

    __key__ = "floors"
    __filter__ = "name"

@dataclass
class Building:
    name: str
    time_slot: list[int]
    floors: list[Floor] = field(default=[], default_factory=list)

    def __post_init__(self):
        self.floors = get_list({Floor.__key__: self.floors}, Floor)

    def __repr__(self) -> str:
        return json.dumps(asdict(self))

    __key__ = "buildings"
    __filter__ = "name"

@dataclass
class Meeting:
    id: str
    user: str
    time_slot: list[int]
    building: Building
    floor: Floor
    room: str

    def __post_init__(self):
        self.building = get_model(data, Building, self.building)
        self.floor = get_model(asdict(self.building), Floor, self.floor)
        
    def __repr__(self) -> str:
        return json.dumps(asdict(self))

    __key__ = "meetings"
    __filter__ = "id"

@dataclass
class DataStore:
    buildings: list[Building]
    meetings: list[Meeting]
    users: list[User]

    def __post_init__(self):
        self.buildings = [Building(**b) for b in self.buildings]
        self.meetings = [Meeting(**m) for m in self.meetings]
        self.users = [User(**u) for u in self.users]
        
    def has_user(self, user):
        return any(u for u in self.users if u.name == user)
    
    def add_building(self, building_name, time_slot):
        self.buildings.append(Building(name=building_name, time_slot=time_slot))

    def __repr__(self) -> str:
        return json.dumps(asdict(self))

def get_list(data, model):
    return [model(**d) for d in data[model.__key__]]

def get_model(data, model, key):
    return next(iter(model(**d) for d in data[model.__key__] if d[model.__filter__] == key), None)

def read_data() -> DataStore:
    global data

    with open("data.toml", mode="rb") as data_file:
        data = tomllib.load(data_file)

    return DataStore(**data)

if __name__ == "__main__":
    read_data()
