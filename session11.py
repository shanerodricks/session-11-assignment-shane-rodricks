import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def count_edges(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R
    
    @property
    def interior_angle(self):
        return (self._n - 2) * 180 / self._n

    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)
    
    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)
    
    @property
    def area(self):
        return self._n / 2 * self.side_length * self.apothem
    
    @property
    def perimeter(self):
        return self._n * self.side_length
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented


class PolygonsIterator:
    def __init__(self, m, R):
        self._index = 3  # start from the polygon with 3 sides
        self._m = m      # maximum number of sides
        self._R = R      # circumradius of all polygons

    def __iter__(self):
        return self

    def __next__(self):
        if self._index > self._m:
            raise StopIteration
        else:
            polygon = Polygon(self._index, self._R)
            self._index += 1
            return polygon


class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        
    def __iter__(self):
        return PolygonsIterator(self._m, self._R)
    
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'
    
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
