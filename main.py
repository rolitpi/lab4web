import uvicorn
import webbrowser
from fastapi import FastAPI

from processor import Processor
from taskType import TaskType

app = FastAPI()
HOST_NAME = "127.0.0.1"
PORT = 8000


@app.get("/solvers/{task}", name="Получить ответ на задачу")
async def get_answer(task: TaskType):
    processor = Processor()
    return {"Ответ": processor.solve_task(task)}


if __name__ == "__main__":
    webbrowser.open(f"http://{HOST_NAME}:{PORT}/docs")
    uvicorn.run(app, host=HOST_NAME, port=PORT)
