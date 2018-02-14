#  do_nothing()
#  print(do_nothing())
# None
#  print(do_nothing)
# <function do_nothing at 0x7f205f130e18>
#  x = do_nothing
#  print(x)
# <function do_nothing at 0x7f205f130e18>
#  x()
#  id(x)
# 139777010765336
#  hex(id(x))
# '0x7f205f130e18'
#  print()
#
#  print(print)
# <built-in function print>
#  do_nothing?
#   File "<stdin>", line 1
#     do_nothing?
#               ^
# SyntaxError: invalid syntax
#  def do_something(x, y, z=12, w="ola"):
# ...     print(x, y, z, w)
# ...
#  do_something(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: do_something() missing 1 required positional argument: 'y'
#  do_something(1, 23)
# 1 23 12 ola
#  do_something(1, 23, "trzy")
# 1 23 trzy ola
#  do_something(1, 23, z=12)
# 1 23 12 ola
#  do_
# do_nothing(    do_something(
#  do_something(1, 23, 14, "ala")
# 1 23 14 ala
#  do_something(1, 23, z=14, w="ala")
# 1 23 14 ala
#  do_something(1, 23, w="ania', z=15)
#   File "<stdin>", line 1
#     do_something(1, 23, w="ania', z=15)
#                                       ^
# SyntaxError: EOL while scanning string literal
#  do_something(1, 23, w="ania", z=15)
# 1 23 15 ania
#  do_something(1, 23, "ania", z=15)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: do_something() got multiple values for argument 'z'
#  do_something(x=1,y= 23, w="ania", z=15)
# 1 23 15 ania
#  do_something(y=1, x= 23, w="ania", z=15)
# 23 1 15 ania


def infinite_arguments(*args):
    print(args)
    print(type(args))

infinite_arguments(1, 2, 3, 4, 5)

print(sum([1, 2]))

#@ TODO: napisz funkcje ktora przyjmuje dowolna liczbe argumentow liczbowych
#@ TODO: i wyswietla na ekranie ich sume

def improved_sum(*args):
    print(sum(args))

improved_sum(1, 2, 3, 4, 5, 7)
improved_sum(*[1, 2, 3])

x, y, z, *something = (1, 2, 3, 4, 5, 6)
*nevermind, a, b = (1, 10, 20, 30, 40)
print(nevermind)
print(a, b)

def foo(a, b, *args):
    print(a, b, args)

foo(1, 2)
foo(1, 2, 3, 4, 5, 6)
foo(1, 2, *range(100))