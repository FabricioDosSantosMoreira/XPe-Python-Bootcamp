import unittest

from root_square_solver import root_square_solver


class CheckRootSquareSolver(unittest.TestCase):
    # NOTE: python -m unittest -v tests.py

    def test_CheckTwoRoots(self) -> None:
        a, b, c = 1, -5, 6
        response = root_square_solver(a, b, c)
        print(f"\nEquation: {a}x^2 + ({b})x + {c} = 0, Roots: {response}")
        
        self.assertEqual(len(response), 2)


    def test_CheckRootValue1(self) -> None:
        a, b, c = 1, -5, 6
        response = root_square_solver(a, b, c)
        print(f"\nEquation: {a}x^2 + ({b})x + {c} = 0, Roots: {response}")

        self.assertIn(response[0], [2, 3])
        self.assertIn(response[1], [2, 3])
        self.assertNotEqual(response[0], response[1])


    def test_CheckRootValue2(self) -> None:
        a, b, c = 1, -5, 6
        response = root_square_solver(a, b, c)
        print(f"\nEquation: {a}x^2 + ({b})x + {c} = 0, Roots: {response}")

        self.assertIn(response[1], [2, 3])
        self.assertIn(response[0], [2, 3])
        self.assertNotEqual(response[0], response[1])


    def test_CheckOneRoot(self) -> None:
        a, b, c = 1, -4, 4
        response = root_square_solver(a, b, c)
        print(f"\nEquation: {a}x^2 + ({b})x + {c} = 0, Roots: {response}")

        self.assertEqual(len(response), 1)
        self.assertEqual(response[0], 2)


    def test_NoRoots(self) -> None:
        a, b, c = 1, 0, 1
        response = root_square_solver(a, b, c)
        print(f"\nEquation: {a}x^2 + ({b})x + {c} = 0, Roots: {response}")

        self.assertIsNone(response)


if __name__ == "__main__":
    unittest.main()
