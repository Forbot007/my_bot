import requests
from config import GIGACHAT_API_KEY, GIGACHAT_URL

def generate_task(topic: str) -> str:
    """Генерация задачи по указанной теме."""
    prompt = f"Сгенерируй задачу по математике для подготовки к ОГЭ на тему: {topic}. Только текст задачи, без решений."
    headers = {"Authorization": f"Bearer {GIGACHAT_API_KEY}"}
    data = {"prompt": prompt, "max_tokens": 100}

    response = requests.post(GIGACHAT_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get("task", "Не удалось сгенерировать задачу.")
    else:
        return "Ошибка при генерации задачи."

def check_answer(task: str, user_answer: str) -> dict:
    """Проверка ответа пользователя и генерация объяснения."""
    prompt = f"""
    Задача: {task}
    Ответ пользователя: {user_answer}
    Проверь правильность ответа. Если ответ неверный, укажи конкретный шаг, на котором допущена ошибка, и объясни правильное решение.
    Ответь в формате JSON: {{"is_correct": bool, "explanation": str}}.
    """
    headers = {"Authorization": f"Bearer {GIGACHAT_API_KEY}"}
    data = {"prompt": prompt, "max_tokens": 200}

    response = requests.post(GIGACHAT_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get("result", {"is_correct": False, "explanation": "Не удалось проверить ответ."})
    else:
        return {"is_correct": False, "explanation": "Ошибка при проверке ответа."}
