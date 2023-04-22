def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    Nlst = []
    for item in lst:
        if item:
            Nlst.append(item)
    return Nlst
        