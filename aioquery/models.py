ENCODING_UTF = "utf-8"
ENCODING_LATIN = "latin-1"


class PlayerModel:
    """Holds details on players.

    Attributes
    ----------
    id: int
        ID of user on the server, not a steam ID.
    name: str
    frags: int
    time: float
    """

    def __init__(self, data: dict) -> None:
        self.id = data["id"]
        self.name = data["name"].encode(ENCODING_LATIN).decode(ENCODING_UTF)
        self.frags = data["frags"]
        self.time = data["time"]


class OSModel:
    """Holds details on OS

    Attributes
    ----------
    windows: bool
    linux: bool
    mac: bool
    """

    windows = False
    linux = False
    mac = False

    def __init__(self, os_code: str) -> None:
        if os_code == "w":
            self.windows = True
        elif os_code in ("m", "o"):
            self.mac = True
        else:
            self.linux = True


class DedicatedModel:
    """Holds details on dedicated

    Attributes
    ----------
    dedicated: bool
    listen: bool
    source_tv: bool
    """

    dedicated = False
    listen = False
    source_tv = False

    def __init__(self, dedicated_code: str) -> None:
        if dedicated_code == "d":
            self.dedicated = True
        elif dedicated_code == "1":
            self.listen = True
        else:
            self.source_tv = True


class ServerModel:
    """Holds details on server.

    Attributes
    ----------
    protocol: byte
    hostname: str
    map: str
    game_dir: str
    game_desc: str
    app_id: int
    players: int
    max_players: int
    bots: int
    dedicated: DedicatedModel
    os: OSModel
    password: str
    secure: bool
    version: str
    game_port: int
    steamid: int
    spec_port: int
    spec_name: str
    tags: list
    gameid: int
    """
    def __init__(self, data: dict) -> None:
        self.protocol = data["protocol"]
        self.hostname = data["hostname"].encode(
            ENCODING_LATIN).decode(ENCODING_UTF)
        self.map = data["map"]
        self.game_dir = data["game_dir"]
        self.game_desc = data["game_desc"].encode(
            ENCODING_LATIN).decode(ENCODING_UTF)
        self.app_id = data["app_id"]
        self.players = data["players"]
        self.max_players = data["max_players"]
        self.bots = data["bots"]
        self.dedicated = DedicatedModel(data["dedicated"])
        self.os = OSModel(data["os"])
        self.password = data["password"]
        self.secure = bool(data["secure"])
        self.version = data["version"]
        self.game_port = data.get("game_port")
        self.steamid = data.get("steamid")
        self.spec_port = data.get("spec_port")
        if data.get("spec_name"):
            self.spec_name = data.get("spec_name").encode(
                ENCODING_LATIN).decode(ENCODING_UTF)
        self.spec_name = data.get("spec_name")
        self.tags = [i.encode(ENCODING_LATIN).decode(
            ENCODING_UTF) for i in data.get('tags')]
        self.gameid = data.get("gameid")
