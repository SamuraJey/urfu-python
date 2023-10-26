import unittest
import sys
sys.path.append('/home/samuraj/Documents/gitrepos/python/urfu-python/Thrid lection/first.py')
from first import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.graph.add_vertex(3)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)
    
    def test_add_vertex(self):
        self.graph.add_vertex(4)
        self.assertIn(4, self.graph.vertices)
    
    def test_add_edge(self):
        self.graph.add_edge(1, 3)
        self.assertIn(3, self.graph.vertices[1])
        self.assertIn(1, self.graph.vertices[3])
    
    def test_remove_vertex(self):
        self.graph.remove_vertex(2)
        self.assertNotIn(2, self.graph.vertices)
        self.assertNotIn(2, self.graph.vertices[1])
        self.assertNotIn(2, self.graph.vertices[3])
    
    def test_remove_edge(self):
        self.graph.remove_edge(1, 2)
        self.assertNotIn(2, self.graph.vertices[1])
        self.assertNotIn(1, self.graph.vertices[2])
    
    def test_str(self):
        expected_output = "1: 2 \n2: 1 3 \n3: 2 \n"
        self.assertEqual(str(self.graph), expected_output)

if __name__ == '__main__':
    unittest.main()