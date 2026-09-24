from abc import ABC, abstractmethod
from typing import Any, Union


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._internal_storage: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._internal_storage:
            raise IndexError("No data left to output.")

        extracted_data = self._internal_storage.pop(0)
        current_rank = self._rank
        self._rank += 1

        return current_rank, extracted_data


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return (all(isinstance(x, (int, float))
                    and not isinstance(x, bool) for x in data))
        return False

    def ingest(self, data: int | float| list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._internal_storage.append(str(item))
        else:
            self._internal_storage.append(str(data))


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Union[str, list[str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._internal_storage.append(item)
        else:
            self._internal_storage.append(data)


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        def is_valid_dict(d: Any) -> bool:
            return (isinstance(d, dict) and all(isinstance(k, str)
                    and isinstance(v, str) for k, v in d.items()))

        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(isinstance(x, dict) and is_valid_dict(x) for x in data)
        return False

    def ingest(self, data:
               Union[dict[str, str], list[dict[str, str]]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")

        def format_log(log_dict: dict[str, str]) -> str:
            if "log_level" in log_dict and "log_message" in log_dict:
                return f"{log_dict['log_level']}: {log_dict['log_message']}"
            return str(log_dict)

        if isinstance(data, list):
            for item in data:
                self._internal_storage.append(format_log(item))
        elif isinstance(data, dict):
            self._internal_storage.append(format_log(data))


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print("\n")

    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")

    try:
        num_proc.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")
    data_num = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_num}")
    num_proc.ingest(data_num)
    print("Extracting 3 values...")

    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {rank}: {val}")
    print("\n")

    print("Testing Text Processor...")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")
    data_text = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {data_text}")
    text_proc.ingest(data_text)
    print("Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"Text value {rank}: {val}")
    print("\n")

    print("Testing Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    data_log = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {data_log}")
    log_proc.ingest(data_log)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")


if __name__ == "__main__":
    main()
