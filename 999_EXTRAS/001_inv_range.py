# Encountered this while trying to do a reverse loop
# Problem: Tapping rain water
# We need to iterate a loop, in reverse, from the second last item all the way to the very first

items = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(items)

for i in range(
    n - 2, -1, -1
):  # Python range second param is upto, we need more than upto zero, we need also zero
    # if you need also zero then you add -1
    print(items[i])
