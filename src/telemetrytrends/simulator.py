import threading, time, random

def _worker(storage, device_id, interval_base=2.0):
    while True:
        payload = {
            "device_id": device_id,
            "metric": "temperature",
            "value": round(20 + random.random() * 10, 2),
            "ts": time.time()
        }
        storage.save(payload)
        time.sleep(interval_base + random.random() * 3.0)

def start_simulator(storage, count=3):
    for i in range(count):
        t = threading.Thread(target=_worker, args=(storage, f"device-{i+1}"), daemon=True)
        t.start()
