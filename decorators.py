# Our decorator function
def interior_decorator(func):
    def add_curtains():
        func()
        print("now my house has purple curtains")

    return add_curtains

# Our function to be decorated
def move_in():
    print("My house was empty, but...")

# bind returned function from interiorDecorator to new variable
new_house = interior_decorator(move_in)
new_house()
# ==============================================================
# BUT naming things is hard! Let's skip the whole "new_house" variable thing with @interior_decorator, an abstraction of what's happening above, so we can call `move_in()` directly and STILL have it be decorated
# White space matters, so notice that the next two lines are at the same indentation depth
@interior_decorator
def move_in():
    print("My house was empty, but...")

# Now move in has been decorated and we can call it directly:
move_in()

# ==============================================================
# We can decorate a function multiple times
def landscaper(func):
    def add_trees():
        func()
        print("And I planted 12 maples for shade.")
    return add_trees

@landscaper
@interior_decorator
def move_in():
    print("My house was empty, but...")

move_in()

# =================================================================
# But what about passing args to the internal function? Mind melting time...
def interior_decorator(func):

  def add_curtains(color):
    if color == "orange":
      color = "ugly-ass"
    func(color)
    print(f'now my house has {color} curtains')

  return add_curtains


@interior_decorator
def move_in(color):
  print("My house was empty, but...")


move_in("orange")
move_in("brown")
