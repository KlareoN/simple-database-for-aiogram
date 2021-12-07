from core import *

from aiogram.utils import executor
from management import dispatcher


if __name__ == '__main__':
    executor.start_polling(
        dispatcher,
        skip_updates=False
    )
