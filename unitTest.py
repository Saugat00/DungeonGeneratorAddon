import random as rand
import unittest
import maze_parser.maze_parser as maze_parser
from maze_parser.wilsons_algorithm import wilsons_algorithm

class dungeonTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
    
    def tests_tertiaryParse(self):
        # maze_parser.tertiary_parse(5, 1, 0)
        returnValue = maze_parser.tertiary_parse(1, 1);
        self.assertEqual(returnValue, "a")

        returnValue1 = maze_parser.tertiary_parse(1,2);
        self.assertEqual(returnValue1, "d")
        
        returnValue2 = maze_parser.tertiary_parse(1,4);
        self.assertEqual(returnValue2, "c")
        
        returnValue3 = maze_parser.tertiary_parse(1,10);
        self.assertEqual(returnValue3, "u")
        
        returnValue4 = maze_parser.tertiary_parse(2,1);
        self.assertEqual(returnValue4, "f")
        
        returnValue5 = maze_parser.tertiary_parse(2,2);
        self.assertEqual(returnValue5, "b")
        
        returnValue6 = maze_parser.tertiary_parse(2,3);
        self.assertEqual(returnValue6, "c")
        
        returnValue7 = maze_parser.tertiary_parse(2,9);
        self.assertEqual(returnValue7, "v")

        returnValue8 = maze_parser.tertiary_parse(3,2);
        self.assertEqual(returnValue8, "e")
        
        returnValue9 = maze_parser.tertiary_parse(3,3);
        self.assertEqual(returnValue9, "a")
        
        returnValue10 = maze_parser.tertiary_parse(3,4);
        self.assertEqual(returnValue10, "f")
        
        returnValue11 = maze_parser.tertiary_parse(4,1);
        self.assertEqual(returnValue11, "e")
        
        returnValue12 = maze_parser.tertiary_parse(4,3);
        self.assertEqual(returnValue12, "d")
        
        returnValue13 = maze_parser.tertiary_parse(4,4);
        self.assertEqual(returnValue13, "b")
        
        returnValue14 = maze_parser.tertiary_parse(4,9);
        self.assertEqual(returnValue14, "t")
        
        
        
        
        
    def test_firstTile(self):
        wa = wilsons_algorithm(h =4 , w = 4)
        M = [["0" for _ in range(wa.w)] for _ in range(wa.h)]
        answr = maze_parser.first_tile(wa.path, M, wa.h, wa.w)
        set = [['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0']]
        self.assertListEqual(set, answr)
        
        wa1 = wilsons_algorithm(h =5 , w = 5)
        M1 = [["0" for _ in range(wa1.w)] for _ in range(wa1.h)]
        set1 = [['0', '0', '0', '0',  '0'], ['0', '0','0', '0', '0'], ['0', '0','0',  '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0']]
        answr2 = maze_parser.first_tile(wa1.path, M1, wa1.w, wa1.h)
        self.assertListEqual(set1, answr2)
    
    def test_lastTile(self):
        pass
    
    
    def tests_generate_dungeon(self):
        
        wa = wilsons_algorithm(h=2, w=2)
        try:
           wa.generate_dungeon()
        except:
           print("problem in generate Dungeon function")


    def test_wilsonsAlgo(self):
        wa = wilsons_algorithm(h =3 , w = 3)
        #self.assertRaises(ValueError,wilsons_algorithm, h= 3, w= 3 )
        try:
            wa.wilsons_algorithm()
        except:
            print("problem in wilson_Algorithm") 
    
    def test_makepath(self):
        wa = wilsons_algorithm(h = 7, w = 8)
        try:
            wa.get_path()
        except:
            print("Problem with get Path Function")
    
    def test_getPath(self):
        pass

if __name__ == "__main__":
    unittest.main();
