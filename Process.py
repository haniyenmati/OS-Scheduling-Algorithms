class Process:
    def __init__(self, arrival, cpu1, io, cpu2):
        self.arrival = arrival
        self.cpu1 = cpu1
        self.io = io
        self.cpu2 = cpu2

    def __str__(self) -> str:
        return f"{self.arrival}-{self.cpu1}-{self.io}-{self.cpu2}"

    def __repr__(self) -> str:
        return f"Process({self.arrival}-{self.cpu1}-{self.io}-{self.cpu2})"
        