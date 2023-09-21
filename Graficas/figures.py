import numpy as np

class Intercept(object):
    def __init__(self, distance, point, normal, obj):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.obj = obj


class Shape(object):
    def __init__(self, position, material):
        self.position = position
        self.material = material

    def ray_intersect(self, origin, direction):
        return None

class Sphere(Shape):
    def __init__(self, position, radius, material):
        super().__init__(position, material)
        self.radius = radius
        self.material = material

    def ray_intersect(self, origin, direction):
        L = np.subtract(self.position, origin) # Origen menos posicion
        lengthL = np.linalg.norm(L) # Magnitud de L
        tca = np.dot(L, direction) # Producto punto de L y direccion
        d = (lengthL**2 - tca**2)**0.5 # Distancia entre el punto mas cercano y el centro de la esfera

        if d > self.radius:
            return None

        THC = (self.radius**2 - d**2)**0.5 # Distancia entre el punto mas cercano y el punto de interseccion
        t0 = tca - THC # Distancia entre el origen y el punto de interseccion
        t1 = tca + THC # Distancia entre el origen y el punto de interseccion

        if t0 < 0:
            t0 = t1

        if t0 < 0:
            return None


        p = np.add(origin, t0 * np.array(direction))
        normal = np.subtract(p, self.position)
        normal = normal / np.linalg.norm(normal)

        return Intercept(
            distance = t0,
            point = p,
            normal = normal,
            obj = self
        )