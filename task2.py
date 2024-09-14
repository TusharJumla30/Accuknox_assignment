class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Creating an iterator that will return the length first, then the width
        self._index = 0
        return self

    def __next__(self):
        if self._index == 0:
            self._index += 1
            return {'length': self.length}
        elif self._index == 1:
            self._index += 1
            return {'width': self.width}
        elif self._index == 2:
            self._index += 1
            return {'Area': self.length * self.width}
        else:
            raise StopIteration  # To end the iteration
    

length = int(input("Enter Lenght of rectangle: "))
width = int(input("Enter Width of rectangle: "))
rectangle = Rectangle(length, width)

# Iterating over the instance
for item in rectangle:
    print(item)
