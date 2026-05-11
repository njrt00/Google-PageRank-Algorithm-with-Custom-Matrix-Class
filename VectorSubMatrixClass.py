class Vector(Matrix):
    """a Vector class built from the Matrix class above"""

    def __init__(self,X=[]):
        super().__init__([[x] for x in X])
