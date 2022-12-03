import uvicorn
import webbrowser
from fastapi import FastAPI

from processor import Processor
from taskType import TaskType

app = FastAPI()
HOST_NAME = "127.0.0.1"
PORT = 8000
processor = Processor()


@app.get("/solvers/test", name="Протестировать все задачи")
async def test():
    for data in TaskType:
        await test_single_solver(TaskType(data))
    return "Все тесты пройдены успешно"


@app.get("/solvers/{task}", name="Получить ответ на задачу")
async def get_answer(task: TaskType):
    return {"Ответ": processor.solve_task(task)}


@app.get("/solvers/test/{task}", name="Протестировать одну задачу")
async def test_single_solver(task: TaskType):
    if task == TaskType.Task10:  # нет примера для этой задачи
        return
    print(f"Тестируем задачу '{task.value}'")
    answer = processor.solve_task(task, f'inputs/test/{task.name}.txt')
    print(f'Получили ответ {answer}')
    f = open(f'inputs/test/{task.name}_output.txt')
    intended_answer = f.readline()
    print(f'Эталонный ответ {intended_answer}')
    assert answer == intended_answer


if __name__ == "__main__":
    webbrowser.open(f"http://{HOST_NAME}:{PORT}/docs")
    uvicorn.run(app, host=HOST_NAME, port=PORT)
