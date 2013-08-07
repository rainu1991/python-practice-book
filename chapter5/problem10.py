def izip(*iterables):
    iterators = map(iter, iterables)
    while iterators:
        yield tuple(map(next, iterators))
