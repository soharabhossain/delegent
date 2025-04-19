import unittest
from delegent.core.engines.assignment_engine import RoleBasedAssignmentEngine

class TestRoleBasedAssignmentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = RoleBasedAssignmentEngine()
        self.agents = [
            {'id': 'a1', 'skills': ['research'], 'role': 'researcher'},
            {'id': 'a2', 'skills': ['writing'], 'role': 'writer'}
        ]
        self.subtasks = [
            {'id': 't1', 'desc': 'Do research', 'skill': 'research', 'role': 'researcher'},
            {'id': 't2', 'desc': 'Write up', 'skill': 'writing', 'role': 'writer'}
        ]

    def test_assignment(self):
        assignments = self.engine.assign(self.subtasks, self.agents)
        self.assertEqual(assignments['t1'], 'a1')
        self.assertEqual(assignments['t2'], 'a2')

if __name__ == '__main__':
    unittest.main()
