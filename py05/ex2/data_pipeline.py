from abc import ABC, abstractmethod
from typing import Any, Union, Protocol


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
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._internal_storage.append(str(item))


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
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._internal_storage.append(item)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_dict(d: Any) -> bool:
            return (isinstance(d, dict) and all(isinstance(k, str)
                    and isinstance(v, str) for k, v in d.items()))
        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(is_valid_dict(x) for x in data)
        return False

    def ingest(self, data:
               Union[dict[str, str], list[dict[str, str]]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            fmt = f"{item.get('log_level')}: {item.get('log_message')}"
            self._internal_storage.append(fmt)


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        print("CSV Output:")
        print(",".join([item[1] for item in data]))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        print("JSON Output:")
        json_items = [f'"item_{rank}": "{val}"' for rank, val in data]
        print("{" + ", ".join(json_items) + "}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            extracted_batch = []
            for _ in range(nb):
                try:
                    extracted_batch.append(proc.output())
                except IndexError:
                    break
            plugin.process_output(extracted_batch)

    def print_processors_stats(self) -> None:
        print("\n")
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            remaining = len(proc._internal_storage)
            total = remaining + proc._rank
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


def main():
    print("=== Code Nexus - Data Pipeline ===")
    print("\n")

    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()
    print("\n")

    print("Registering Processors")

    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    batch1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]
    ds.process_stream(batch1)
    ds.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVExportPlugin())
    ds.print_processors_stats()

    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
          'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"Send another batch of data: {batch2}")
    ds.process_stream(batch2)
    ds.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JSONExportPlugin())
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
