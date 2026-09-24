import random
from typing import Generator

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep", "grab",
           "move", "swim", "climb", "release", "use"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    """An endless generator that yields random game events."""
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(event_list: list) -> Generator[tuple[str, str], None, None]:
    """Yields and removes random elements from a list until it's empty."""
    while len(event_list) > 0:
        idx = random.randrange(len(event_list))
        yield event_list.pop(idx)


def main():
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()

    for i in range(1000):
        name, action = next(event_stream)
        if i <= 1000:
            print(f"Event {i}: Player {name} did action {action}")

    ten_events = [next(event_stream) for _ in range(10)]
    print(f"\nBuilt list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
