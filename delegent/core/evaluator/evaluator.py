# multi_agent_system/evaluator/evaluator.py

from typing import List
from delegent.core.execution.execution_layer import ExecutionResult
# from collections import Counter
from colorama import Fore, Style

from delegent.utils.logger import log_step

class ResultAggregator:
    @log_step("ResultAggregation")
    def summarize_results(self, results: List[ExecutionResult]):
        total = len(results)
        success = 0
        failure = 0

        print(f"\n{Fore.BLUE}--- Execution Summary ---{Style.RESET_ALL}")

        for res in results:
            if res.status.startswith("completed"):
                print(f"{Fore.GREEN}✔ {res.subtask_id}: {res.status}{Style.RESET_ALL}")
                success += 1
            else:
                print(f"{Fore.RED}✘ {res.subtask_id}: {res.status}{Style.RESET_ALL}")
                failure += 1

        print(f"\n{Fore.CYAN}Total Subtasks: {total}")
        print(f"Successful Executions: {success}")
        print(f"Failures: {failure}{Style.RESET_ALL}")

        return {
            "total": total,
            "success": success,
            "failure": failure,
        }
