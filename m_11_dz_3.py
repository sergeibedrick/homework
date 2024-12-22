import inspect
import types


def introspection_info(obj):
    """
    Проводит интроспекцию объекта и возвращает словарь с информацией о нем.
    Args:
        obj: Объект любого типа.
    Returns:
        dict: Словарь с информацией об объекте.
    """
    info = {}
    info['type'] = str(type(obj))

    attributes = [name for name in dir(obj) if not name.startswith('__')]
    info['attributes'] = attributes

    methods = [name for name in dir(obj) if callable(getattr(obj, name)) and not name.startswith('__')]
    info['methods'] = methods

    try:
        module_name = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else "unknown"
        info['module'] = module_name
    except AttributeError:
        if isinstance(obj, types.ModuleType):  # если это модуль
            info['module'] = obj.__name__
        else:
            info['module'] = 'unknown'

    # Дополнительные свойства для некоторых типов
    if isinstance(obj, int):
        info['is_positive'] = obj > 0
        info['is_even'] = obj % 2 == 0
    elif isinstance(obj, float):
        info['is_finite'] = str(obj).lower() != "inf" and str(obj).lower() != "-inf"
    elif isinstance(obj, str):
        info['length'] = len(obj)
        info['is_upper'] = obj.isupper()
    elif inspect.isclass(obj):
        info['base_classes'] = [base.__name__ for base in obj.__bases__]
    elif inspect.isfunction(obj) or inspect.ismethod(obj):
        try:
            info['docstring'] = inspect.getdoc(obj)
            info['signature'] = str(inspect.signature(obj))
            # info['source'] = inspect.getsource(obj) - усложняет вывод, если нужно, расскомментируйте
        except:
            info['docstring'] = "unknown"
            info['signature'] = "unknown"

    return info

# Пример использования с собственным классом и объектами других типов

class MyClass:
    """This is my custom class"""

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._c = 10

    def my_method(self):
        """This is my custom method"""
        return self.a + self.b


def my_function(x, y=5):
    """This is my custom function"""
    return x * y


if __name__ == '__main__':
    obj_instance = MyClass(5, 10)
    class_info = introspection_info(MyClass)
    method_info = introspection_info(obj_instance.my_method)
    number_info = introspection_info(42)
    float_info = introspection_info(3.14)
    string_info = introspection_info("Hello")
    list_info = introspection_info([1, 2, 3])
    function_info = introspection_info(my_function)

    print("Instance of MyClass:")
    print(introspection_info(obj_instance))
    print("\nMyClass class:")
    print(class_info)
    print("\nmy_method:")
    print(method_info)
    print("\nInteger:")
    print(number_info)
    print("\nFloat:")
    print(float_info)
    print("\nString:")
    print(string_info)
    print("\nList:")
    print(list_info)
    print("\nFunction:")
    print(function_info)