https://jeffknupp.com/blog/2018/12/13/how-to-do-just-about-anything-with-python-lists/

Reverse/Sort A List In Python
There are two ways to reverse a list in Python, and which one you use depends on what you want to do with the resulting reversed data. If you're only going iterate over the items in the reversed list (say, to print them out), use the Python built-in function reversed(seq)

If you need the reversed list itself, use the Python built-in function sorted(iterable, *, key=None, reverse=False)
sorted(readings, key=lambda reading: reading[1], reverse=True)
Accessing elements of a tuple or class is such a common task that Python provides a set of convenience functions in the operator built-in module.
 use the field's index in the tuple as an argument to operator.itemgetter:

sorted(readings, key=itemgetter(1), reverse=True)

Split A Python List Into Chunks
Splitting a list into equally sized sub-lists (for processing data in parallel, perhaps) is a common task. It's so common, in fact, that the itertools module (a module practically begging to be used in these kinds of tasks, by the way) gives actual code for how to accomplish this in Python

Python itertools module
Python itertools module is very useful in creating efficient iterators.

Python itertools module provide us various ways to manipulate the sequence while we are traversing it.
9440503239 sudarshan
import itertools.zip_longest

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

print(grouper('ABCDEFG', 3, 'x'))

print("Removed all print messages")
