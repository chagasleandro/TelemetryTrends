from collections import defaultdict, deque

class InMemoryStorage:
    def __init__(self, maxlen=500):
        self._data = defaultdict(lambda: deque(maxlen=maxlen))

    def save(self, telemetry: dict):
        self._data[telemetry["device_id"]].append(telemetry)

    def query(self, device_id: str):
        return list(self._data[device_id])
