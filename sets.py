set={1,23,45}
print(sorted(set,reverse=True))
#sets are faster than lists.
# we can use add() to add elements to the list.
# if we write add(x,y) it prints {(x,y)}
# if we want to add two or more elements than we can use update([x,y])
# sets ignore repition.
# to remove a set we can use remove() or discard() but if any element is absent than remove() gives a key error while discard() doesn't.
#pop() to remove element from last position.
#clear() remove all the elements from the set.
# sets are mutable.
# frozenset are immutable
#