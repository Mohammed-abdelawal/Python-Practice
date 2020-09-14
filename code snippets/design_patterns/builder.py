class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()

        # First goes the body
        body = self.__builder.getBody()
        car.setBody(body)

        # Then engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        # And four wheels
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1
        return car

# The whole product


class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print('body: %s' % self.__body.shape)
        print('engine horsepower: %d' % self.__engine.horsepower)
        print('tire size: %d\'' % self.__wheels[0].size)


class Builder:
    def getWheel(self): pass

    def getEngine(self): pass

    def getBody(self): pass


class RollsRoyceBuilder(Builder):

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 28
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 3000
        return engine

    def getBody(self):
        body = Body()
        body.shape = 'sedan luxary'
        return body

# Car parts


class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


rolls_royceBuilder = RollsRoyceBuilder()  # initializing the class

director = Director()

# Build rolls_royce
print('Rolls Royce')
director.setBuilder(rolls_royceBuilder)
rolls_royce = director.getCar()
rolls_royce.specification()
print('')
