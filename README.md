# session-11-assignment-shane-rodricks
# Session 11 Assignment - Refactoring Polygons Class into an Iterable with Lazy Evaluation
Name: Shane Rodricks
Email: spiderpig27570@gmail.com
Session: 8: Advanced Python Topics

# Project Description
This project involves refactoring the Polygons class to implement lazy evaluation while making it an iterable. The goal is to generate polygons on demand (lazily) as they are iterated, rather than storing all polygons upfront in a list. This approach improves memory efficiency and aligns with the Python iterator protocol, making the Polygons class more scalable for large values of m (number of sides).

# Original Functionality
In the original implementation:

The Polygons class was designed as a sequence type, with polygons stored in a list.
The list was precomputed, containing polygons with side counts ranging from 3 to m.
The class supported indexing and slicing through __getitem__, but it lacked the lazy evaluation and memory efficiency required for large polygon collections.
Changes Made (Refactoring for Lazy Evaluation)
This refactor introduces the following major changes:

# Removed List Storage:

The previous version used a list to store all polygons. This has been replaced by lazy computation of each polygon during iteration.
Implemented an Iterator:

A custom iterator, PolygonsIterator, was created to generate polygons one at a time as the iteration progresses. The polygons are not computed until they are needed.
Lazy Evaluation:

The polygons are generated on the fly in the __next__ method of the iterator, adhering to the principle of lazy evaluation. This ensures that no polygons are stored in memory unnecessarily.
Key Changes to the Code
# PolygonsIterator Class:

This class implements the iteration logic. It starts at 3 sides and lazily generates polygons up to m sides.
When the iteration is complete, it raises a StopIteration exception.

class PolygonsIterator:
    def __init__(self, m, R):
        self._index = 3  # Start from polygon with 3 sides
        self._m = m      # Maximum number of sides
        self._R = R      # Circumradius of all polygons

    def __iter__(self):
        return self

    def __next__(self):
        if self._index > self._m:
            raise StopIteration
        else:
            polygon = Polygon(self._index, self._R)
            self._index += 1
            return polygon
# Polygons Class:

The Polygons class now implements __iter__, which returns an instance of PolygonsIterator. This makes the Polygons class an iterable, supporting lazy evaluation.

# Max Efficiency Polygon:

The method for finding the polygon with the highest area-to-perimeter ratio now iterates over the polygons lazily. It no longer relies on a precomputed list.

@property
def max_efficiency_polygon(self):
    max_efficiency = 0
    max_polygon = None
    for polygon in self:
        efficiency = polygon.area / polygon.perimeter
        if efficiency > max_efficiency:
            max_efficiency = efficiency
            max_polygon = polygon
    return max_polygon

# Functionality
Polygons Class:

Can now be iterated over using for loops or any other iteration context.
Lazily generates polygons with side counts ranging from 3 to m.
Iterator (PolygonsIterator):

Handles the logic for generating polygons on demand.
Raises StopIteration when the iteration is complete.
Max Efficiency Calculation:

Efficiently finds the polygon with the maximum area-to-perimeter ratio, iterating over polygons as they are generated.

# Testing
The refactored implementation has been thoroughly tested to ensure correct behavior. The tests include:

Iteration Test: Verifying that the polygons are generated lazily and in the correct order.
Max Efficiency Test: Ensuring that the correct polygon with the highest area-to-perimeter ratio is found.
StopIteration: Ensuring that iteration stops correctly when the maximum number of sides is reached.
Here are some example test cases:

# Testing iteration and lazy evaluation
def test_polygons_lazy():
    polygons = Polygons(6, 5)
    for polygon in polygons:
        print(polygon)

test_polygons_lazy()

# Testing max efficiency polygon
def test_max_efficiency_polygon():
    polygons = Polygons(10, 5)
    print(f'Max efficiency polygon: {polygons.max_efficiency_polygon}')

test_max_efficiency_polygon()

# Key Concepts Demonstrated
Lazy Evaluation:

The polygons are generated only when required, making the code more memory-efficient and scalable.
Iterator Protocol:

The Polygons class now adheres to the iterator protocol, using a custom PolygonsIterator to handle polygon generation.
Efficiency:

The use of lazy evaluation ensures that memory is not wasted by storing unnecessary polygons, and computation is deferred until needed.

# Conclusion
This refactor demonstrates the power of lazy evaluation in Python. By removing the list storage and generating polygons dynamically, the Polygons class becomes more memory-efficient and scalable, especially for large values of m. The use of the iterator protocol makes the class more Pythonic and flexible for use in different contexts.
