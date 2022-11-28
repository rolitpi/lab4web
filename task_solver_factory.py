from taskType import TaskType
from tasks.solver1 import Solver1
from tasks.solver2 import Solver2
from tasks.solver3 import Solver3
from tasks.solver4 import Solver4
from tasks.solver5 import Solver5
from tasks.solver6 import Solver6
from tasks.solver7 import Solver7
from tasks.solver8 import Solver8
from tasks.solver9 import Solver9
from tasks.solver10 import Solver10
from tasks.solver11 import Solver11
from tasks.solver12 import Solver12
from tasks.solver13 import Solver13
from tasks.solver14 import Solver14
from tasks.solver15 import Solver15
from tasks.solver16 import Solver16
from tasks.solver17 import Solver17
from tasks.solver18 import Solver18
from tasks.solver19 import Solver19
from tasks.solver20 import Solver20


class TaskSolverFactory:
    def __init__(self):
        self._solvers = {
            TaskType.Task1: Solver1,
            TaskType.Task2: Solver2,
            TaskType.Task3: Solver3,
            TaskType.Task4: Solver4,
            TaskType.Task5: Solver5,
            TaskType.Task6: Solver6,
            TaskType.Task7: Solver7,
            TaskType.Task8: Solver8,
            TaskType.Task9: Solver9,
            TaskType.Task10: Solver10,
            TaskType.Task11: Solver11,
            TaskType.Task12: Solver12,
            TaskType.Task13: Solver13,
            TaskType.Task14: Solver14,
            TaskType.Task15: Solver15,
            TaskType.Task16: Solver16,
            TaskType.Task17: Solver17,
            TaskType.Task18: Solver18,
            TaskType.Task19: Solver19,
            TaskType.Task20: Solver20
        }

    def register_solver(self, task_solver, task_type: TaskType):
        self._solvers[task_type] = task_solver

    def get_solver(self, task_type: TaskType):
        solver = self._solvers.get(task_type)
        if not solver:
            raise ValueError(task_type)
        return solver()
