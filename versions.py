
__version__ = "1.3.0"

def get_version():
    """
    Возвращает текущую версию проекта
    
    Returns:
        str: Строка с версией в формате SemVer
    """
    return __version__

def print_version():
    """Печатает текущую версию проекта"""
    print(f"SemVer Project v{__version__}")

if __name__ == "__main__":
    print_version()