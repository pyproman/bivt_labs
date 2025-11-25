import inspect
from typing import Callable, Any


def run(function: Callable, *, result: Any) -> None:
    """
    Запускает function (обычно lambda), проверяет результат
    с result (может быть классом ошибки)
    """
    src = inspect.getsource(function).strip().split("lambda:")[-1].split(", result=")[0]
    try:
        value = function()
    except Exception as err:
        if (
            isinstance(result, type)
            and issubclass(result, Exception)
            and isinstance(err, result)
        ):
            print(f"[GOOD] {src} -> {err}")
        else:
            print(f"[FAIL] {src} -> {err}, expected {result}")
            raise
    else:
        if value == result:
            print(f"[GOOD] {src} -> {value}")
        else:
            print(f"[FAIL] {src} -> {value}, expected {result}")
