class zeros(Matrix):
    """basic class for constructing m x n all zero matrices"""

    def __init__(self,m,n):
        super().__init__([[0.0 for col in range(n)] for row in range(m)])

class ones(Matrix):
    """basic class for constructing m x n all ones matrices"""

    def __init__(self,m,n):
        super().__init__([[1.0 for col in range(n)] for row in range(m)])

class diag(Matrix):
    """basic class for constructing m x m diagonal matrix"""

    def __init__(self,d):
        super().__init__([[0.0 for col in range(len(d))] for row in range(len(d))])
        for i in range(len(d)):
            self.data[i][i] = d[i]

class eye(diag):
    """identity matrix"""

    def __init__(self,n=3):
        super().__init__([1.0 for i in range(n)])
