from taskType import TaskType
from task_solver_factory import TaskSolverFactory


class Processor:
    _solvers_factory = TaskSolverFactory()

    def solve_task(self, task_type: TaskType, file_name: str = '') -> str:
        task_solver = self._solvers_factory.get_solver(task_type)
        if file_name:
            task_solver.FILE_NAME = file_name
        return task_solver.solve()
