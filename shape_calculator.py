class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (self.width * 2 + self.height * 2)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** 0.5)

  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return 'Too big for picture.'
    else:
      picture = ''
      for i in range(0, self.height):
        picture += '*' * (self.width) + '\n'
      return picture

  def get_amount_inside(self, otherShape):
    return round((self.get_area()/otherShape.get_area())-0.5)


class Square(Rectangle):
  def __init__(self, side):
    self.width = self.height = side

  def __str__(self):
    return 'Square(side=' + str(self.width) + ')'

  def set_width(self, side):
    self.width = self.height = side
  
  def set_height(self, side):
    self.width = self.height = side

  def set_side(self, side):
    self.width = self.height = side