
def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return pos
    return go


tourist = factory(0)
print(tourist(2))
print(tourist(3))
print(tourist(5))
