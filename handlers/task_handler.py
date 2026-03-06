from aiogram import Router, types
from aiogram.filters import Command
from services.gigachat_api import generate_task, check_answer

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Я помогу тебе подготовиться к ОГЭ по математике. "
        "Напиши тему, по которой хочешь решать задачи (например, 'квадратные уравнения')."
    )

@router.message()
async def task_handler(message: types.Message):
    topic = message.text
    task = generate_task(topic)
    await message.answer(f"Реши задачу:\n{task}")

    # Сохраняем задачу в пользовательском контексте (например, в FSM)
    # Здесь можно использовать aiogram.fsm для управления состояниями
