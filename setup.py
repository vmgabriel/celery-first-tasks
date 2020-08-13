
"""
Main Module, this run the app
"""

from src.app import add_data

if __name__ == '__main__':
    print(' -- Load Main -- ')
    add_data.delay('x', 'y')
