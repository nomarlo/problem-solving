def optimizeMemoryUsage(foregroundTasks, backgroundTasks, K):
    """
    :type foregroundTasks: List[int]
    :type backgroundTasks: List[int]
    :type K: int
    :rtype: List[List[int]]
    """

    max = 0
    selected_tasks = [[-1, -1]]

    if K == 0 or (len(foregroundTasks) == 0 and len(backgroundTasks) == 0):
        return selected_tasks

    if len(foregroundTasks) == 0:
        foregroundTasks.append(K + 1)

    if len(backgroundTasks) == 0:
        backgroundTasks.append(K + 1)

    foreground_tasks = sorted([[ft, idx] for idx, ft in enumerate(foregroundTasks)])
    background_tasks = sorted([[bt, idx] for idx, bt in enumerate(backgroundTasks)])

    ft_idx = 0
    bt_idx = len(background_tasks) - 1
    is_ft_idx_new = True
    is_bt_idx_new = True
    while ft_idx < len(foreground_tasks) and bt_idx >= 0:

        ft = foreground_tasks[ft_idx]
        if is_ft_idx_new and max <= ft[0] <= K:
            if ft[0] > max:
                max = ft[0]
                selected_tasks = [[ft[1], -1]]
            else:
                selected_tasks.append([ft[1], -1])

        bt = background_tasks[bt_idx]
        if is_bt_idx_new and max <= bt[0] <= K:
            if bt[0] > max:
                max = bt[0]
                selected_tasks = [[-1, bt[1]]]
            else:
                selected_tasks.append([-1, bt[1]])

        is_ft_idx_new = False
        is_bt_idx_new = False

        tasks_sum = ft[0] + bt[0]
        if max <= tasks_sum <= K:
            ft_idx = ft_idx + 1
            is_ft_idx_new = True

            if tasks_sum > max:
                max = tasks_sum
                selected_tasks = [[ft[1], bt[1]]]
            else:
                selected_tasks.append([ft[1], bt[1]])

            bt_idx_prev = bt_idx - 1
            while bt_idx_prev >= 0 and background_tasks[bt_idx_prev][0] == bt[0]:
                selected_tasks.append([ft[1], background_tasks[bt_idx_prev][1]])
                bt_idx_prev = bt_idx_prev - 1

        else:
            bt_idx = bt_idx - 1

            if bt_idx == -1 and ft_idx + 1 < len(foreground_tasks) and foreground_tasks[ft_idx + 1][0] == max:

                ft_idx = ft_idx + 1
                is_ft_idx_new = True
                bt_idx = 0
            else:
                is_bt_idx_new = True

    return selected_tasks


import unittest


class TestOptimizeMemoryUsage(unittest.TestCase):

    def test(self):
        self.assertCountEqual(optimizeMemoryUsage([1, 7, 2, 4, 5, 6], [3, 1, 2], 6),
                              [[3, 2], [4, 1], [5, -1]])
        self.assertCountEqual(optimizeMemoryUsage([1, 7, 2, 4, 5, 6], [1, 1, 2], 10), [[1, 2]])
        self.assertCountEqual(optimizeMemoryUsage([12, 7, 2, 4, 5, 6], [11, 21, 2], 1), [[-1, -1]])

        self.assertCountEqual(optimizeMemoryUsage([6, 6, 6], [1], 7), [[0, 0], [1, 0], [2, 0]])
        self.assertCountEqual(optimizeMemoryUsage([6, 6], [1, 1, 1, 1, 1], 7),
                              [[0, 4], [0, 3], [0, 2], [0, 1], [0, 0], [1, 4], [1, 3], [1, 2], [1, 1], [1, 0]])
        self.assertCountEqual(optimizeMemoryUsage([1, 7, 8], [3, 1, 2], 10), [[1, 0], [2, 2]])
        self.assertCountEqual(optimizeMemoryUsage([1, 7, 2, 4, 5, 6], [1, 1, 2], 10), [[1, 2]])
        self.assertCountEqual(
            optimizeMemoryUsage(foregroundTasks=[1, 7, 2, 4, 5, 6], backgroundTasks=[1, 1, 2], K=7),
            [[4, 2], [5, 1], [5, 0], [1, -1]])
        self.assertCountEqual(
            optimizeMemoryUsage(foregroundTasks=[1, 7, 2, 4, 5, 6], backgroundTasks=[1, 1, 2], K=9),
            [[1, 2]])
        self.assertCountEqual(
            optimizeMemoryUsage(foregroundTasks=[1, 7, 2, 4, 5, 6], backgroundTasks=[1, 1, 2], K=0),
            [[-1, -1]])
        self.assertCountEqual(
            optimizeMemoryUsage(foregroundTasks=[1], backgroundTasks=[1], K=1),
            [[0, -1], [-1, 0]])
        self.assertCountEqual(
            optimizeMemoryUsage(foregroundTasks=[1, 1, 1], backgroundTasks=[1, 1], K=1),
            [[-1, 1], [-1, 0], [0, -1], [1, -1], [2, -1]])
        self.assertCountEqual(
            optimizeMemoryUsage(foregroundTasks=[1], backgroundTasks=[1], K=3),
            [[0, 0]])
        self.assertCountEqual(
            optimizeMemoryUsage(foregroundTasks=[1], backgroundTasks=[], K=1),
            [[0, -1]])
        self.assertCountEqual(
            optimizeMemoryUsage(foregroundTasks=[1], backgroundTasks=[], K=3),
            [[0, -1]])
        self.assertCountEqual(
            optimizeMemoryUsage(foregroundTasks=[], backgroundTasks=[1], K=1),
            [[-1, 0]])
        self.assertCountEqual(
            optimizeMemoryUsage(foregroundTasks=[], backgroundTasks=[1], K=3),
            [[-1, 0]])
        self.assertCountEqual(
            optimizeMemoryUsage(foregroundTasks=[], backgroundTasks=[], K=0),
            [[-1, -1]])
        self.assertCountEqual(
            optimizeMemoryUsage(foregroundTasks=[], backgroundTasks=[], K=10),
            [[-1, -1]])
