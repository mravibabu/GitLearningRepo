import itertools.zip_longest

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

print(grouper('ABCDEFG', 3, 'x'))

print("this is git demo of jeffknup")
print("removing from the staging")

print("moved to dev branch from master branch")
print("staging and comit at a time")

