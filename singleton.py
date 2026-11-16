"""A simple single-process, single-threaded Singleton example."""


class AppSettings:
    """Keep one settings object and return it for every request."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.counter = 0
        return cls._instance


if __name__ == "__main__":
    first = AppSettings()
    second = AppSettings()

    print(f"같은 인스턴스인가요? {first is second}")
    first.counter = 42
    print(f"첫 번째 변수에서 설정한 counter: {first.counter}")
    print(f"두 번째 변수에서 읽은 counter: {second.counter}")
