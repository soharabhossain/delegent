import unittest
from delegent.core.engines.greedy_assignment_engine import GreedyAssignmentEngine

class TestGreedyAssignmentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = GreedyAssignmentEngine()
        self.agents = [
            {'id': 'a1', 'skills': ['research']},
            {'id': 'a2', 'skills': ['writing']},
            {'id': 'a3', 'skills': ['editing']}
        ]
        self.subtasks = [
            {'id': 't1', 'desc': 'Research topic', 'skill': 'research'},
            {'id': 't2', 'desc': 'Write report', 'skill': 'writing'},
            {'id': 't3', 'desc': 'Edit report', 'skill': 'editing'},
            {'id': 't4', 'desc': 'Translate report', 'skill': 'translation'}  # No agent with this skill
        ]

    def test_assignment(self):
        assignments = self.engine.assign(self.subtasks, self.agents)
        self.assertEqual(assignments['t1'], 'a1')
        self.assertEqual(assignments['t2'], 'a2')
        self.assertEqual(assignments['t3'], 'a3')
        self.assertIsNone(assignments['t4'])  # No agent can do this task

if __name__ == '__main__':
    unittest.main()
