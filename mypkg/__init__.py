from mydependency import hi as dep_hi


def hi():
    return dep_hi() + " (with a dependency)"