class Cell:
    def __init__(self, x, y):
        """
        Creates a new cell object and sets it's initial value to 0
        :param x: x coordinate of the cell
        :param y: y coordinate of the cell
        """
        self._x = x
        self._y = y
        self._value = 0
    
    @property
    def x(self):
        """
        Gets the x coordinate of the cell
        :return: int
        """
        return self._x
    
    @x.setter
    def x(self, new_x):
        """
        Sets the x coordinate of the cell
        :param new_x: int
        """
        self._x = new_x

    @property
    def y(self):
        """
        Gets the y coordinate of the cell
        :return: int
        """
        return self._y

    @y.setter
    def y(self, new_y):
        """
        Sets the y coordinate of the cell
        :param new_y: y
        """
        self._y = new_y

    @property
    def value(self):
        """
        Gets the current value of the cell
        :return: int
        """
        return self._value

    @value.setter
    def value(self, new_value):
        """
        Sets the current value of the cell
        :param new_value: int
        """
        self._value = new_value

    