from entities.constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, RIGHT

class Snake:
  def __init__(self):
    self.body = [(5, 5), (4, 5), (3, 5)]
    self.direction = RIGHT

  def move(self):
    head = self.body[0]
    new_head = ((head[0] + self.direction[0]) % (SCREEN_WIDTH // CELL_SIZE),
                (head[1] + self.direction[1]) % (SCREEN_HEIGHT // CELL_SIZE))
    self.body.insert(0, new_head)
    self.body.pop()

  def grow(self):
    head = self.body[0]
    new_head = ((head[0] + self.direction[0]) % (SCREEN_WIDTH // CELL_SIZE),
                (head[1] + self.direction[1]) % (SCREEN_HEIGHT // CELL_SIZE))
    self.body.insert(0, new_head)

  def change_direction(self, new_dir):
    if (new_dir[0], new_dir[1]) != (-self.direction[0], -self.direction[1]):
      self.direction = new_dir

  def collides_with_itself(self):
    return self.body[0] in self.body[1:]

