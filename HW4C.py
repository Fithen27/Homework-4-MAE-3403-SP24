import numpy as np
from scipy.linalg import solve

def solve_linear_system(coefficients, constants):
    """
    Solve a system of linear equations.

    Parameters:
    - coefficients (numpy.ndarray): Coefficient matrix of the system.
    - constants (numpy.ndarray): Constants vector of the system.

    Returns:
    - solution (numpy.ndarray): Solution vector.
    """
    solution = solve(coefficients, constants)
    return solution

def print_solution(solution):
    """
    Print the solution vector in a readable format.

    Parameters:
    - solution (numpy.ndarray): Solution vector to be printed.
    """
    for i, value in enumerate(solution, start=1):
        print(f"x{i} = {value}")

def main():
    # Define the coefficients matrix and the constants vector for the first problem
    coefficients1 = np.array([[3, 1, -1], [1, 4, 1], [2, 1, 2]])
    constants1 = np.array([2, 12, 10])

    # Solve the first problem
    solution1 = solve_linear_system(coefficients1, constants1)

    # Print the result for the first problem
    print("Solution for the first problem:")
    print_solution(solution1)

    # Define the coefficients matrix and the constants vector for the second problem
    coefficients2 = np.array([[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 4], [-1, 2, 7, 3]])
    constants2 = np.array([2, 12, 21, 37])

    # Solve the second problem
    solution2 = solve_linear_system(coefficients2, constants2)

    # Print the result for the second problem
    print("\nSolution for the second problem:")
    print_solution(solution2)

if __name__ == "__main__":
    main()
