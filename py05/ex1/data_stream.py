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

    def ingest(self, data: Union[int, float, list[Union[int, float]]]) -> None:
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


class DataStream:

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    handled = True
                    break

            if not handled:
                print(f"DataStream error - "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            remaining = len(proc._internal_storage)
            total_processed = remaining + proc._rank
            proc_name = (proc.__class__.__name__.replace
                         ("Processor", " Processor"))
            print(f"{proc_name}: total {total_processed} "
                  f"items processed, remaining {remaining} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("\n")

    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print("\n")

    print("Registering Numeric Processor")
    print("\n")

    num_proc = NumericProcessor()
    data_stream.register_processor(num_proc)

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]

    print(f"Send first batch of data on stream: {batch}")
    data_stream.process_stream(batch)
    data_stream.print_processors_stats()
    print("\n")

    print("Registering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    data_stream.register_processor(text_proc)
    data_stream.register_processor(log_proc)
    print("Send the same batch again")
    data_stream.process_stream(batch)
    data_stream.print_processors_stats()
    print("\n")

    print("Consume some elements from the "
          "data processors: Numeric 3, Text 2, Log 1")

    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()

    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
