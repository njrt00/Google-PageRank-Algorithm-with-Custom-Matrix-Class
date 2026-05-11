class Matrix:
    """A simple vector class"""

    def __init__(self,X=[[]]):
        """constructor for vectors"""
        self.data = [[x for x in row] for row in X] # create a new list of lists (in memory)
        self.m = len(X)               # store the size of the list
        self.n = len(X[0])            # store the size of the list
        self.shape = self.m,self.n    # matrix dimensions (tuple)
    
    def __add__(self,other):
        """returns the sum of the matrix and the other matrix"""
        
        if self.m!=other.m: raise Exception("Matrix rows do not match")
        if self.n!=other.n: raise Exception("Matrix cols do not match")
        
        output = Matrix(self.data)           # copy current matrix
        
        for i in range(self.m):                        # loop over rows
            for j in range(self.n):                    # loop over cols
                output.data[i][j] += other.data[i][j]  # add value from other matrix
        
        return output    # return the output matrix
    
    def __sub__(self,other):
        """returns the difference of the matrix and the other matrix"""
        
        if self.m!=other.m: raise Exception("Matrix rows do not match")
        if self.n!=other.n: raise Exception("Matrix cols do not match")
        
        output = Matrix(self.data)           # copy current matrix
        
        for i in range(self.m):                        # loop over rows
            for j in range(self.n):                    # loop over cols
                output.data[i][j] -= other.data[i][j]  # add value from other matrix
        
        return output    # return the output matrix

    def __neg__(self):
        """returns the opposite of the vector"""
        
        output = Matrix(self.data)           # copy current matrix
        
        for i in range(self.m):              # loop over rows
            for j in range(self.n):          # loop over cols
                output.data[i][j] *= -1      # multiply by -1
        
        return output    # return the output matrix

    def __mul__(self,other):
        """multiply by scalar (on the right)"""
        output = Matrix(self.data)           # copy current matrix
        
        for i in range(self.m):              # loop over rows
            for j in range(self.n):          # loop over cols
                output.data[i][j] *= other      # multiply by other (scalar)
        
        return output    # return the output matrix
    
    def __rmul__(self,other):
        """multiply by scalar (on the left)"""
        output = Matrix(self.data)           # copy current matrix
        
        for i in range(self.m):              # loop over rows
            for j in range(self.n):          # loop over cols
                output.data[i][j] *= other      # multiply by other (scalar)
        
        return output    # return the output matrix
    
    def __matmul__(self,other):
        """implements basic 3-loop matrix multiplication out = self @ other"""
        if self.n!=other.m: raise Exception("Matrix dimensions do not match")
        
        output = Matrix([[0 for j in range(other.n)] for i in range(self.m)])           # copy current matrix
        
        for i in range(self.m):              # loop over rows
            for j in range(other.n):          # loop over cols

                for k in range(self.n):
                    output.data[i][j] += self.data[i][k]*other.data[k][j]      # multiply by other (scalar)
        
        return output    # return the output matrix

    def norm(self):
        """computes the Euclidean norm of the vector"""
        output = 0.0
        for i in range(self.m):              # loop over rows
            for j in range(self.n):          # loop over cols
                output += self.data[i][j]**2    # Sum Of Squares of the entries (S.O.S.)
        return output**0.5               # return the square root of S.O.S.

    def transpose(self):
        """returns the transpose of the matrix"""
        output = Matrix([[0 for j in range(self.m)] for i in range(self.n)])           # copy current matrix
        
        for i in range(self.n):              # loop over rows (new matrix)
            for j in range(self.m):          # loop over cols (new matrix)
                output.data[i][j] += self.data[j][i]      # transpose data (from old matrix)
        
        return output    # return the output matrix

    def __getitem__(self,i):
        """returns the ith row of the matrix (as a Vector)"""
        if type(i)==int:#------------------------------row extraction
            return self.data[i]
        elif type(i)==slice:#--------------------------slice of rows
            return Matrix(self.data[i])
        elif type(i)==tuple:#--------------------------slice of rows and cols
            row_slice,col_slice = i
            if type(row_slice)!=slice or type(col_slice)!=slice:
                raise Exception("Incorrect Usage: Matrix[slice,slice] format or Matrix[int][int] format only ")
            return Matrix([row[col_slice] for row in self.data[row_slice]])
        else:
            raise Exception("Incorrect slice/index type")
    
    def __setitem__(self,i,v):
        """sets row i to Vector v"""
        if type(i)==int:#------------------------------overwrite a row
            self.data[i] = v
        elif type(i)==slice:#--------------------------overwrite slice of rows
            step = i.step if i.step else 1
            if len(v)!=(i.stop-i.start)/step:
                raise Exception("RHS not the same length as slice (Matrix)")
            if len(self.data[0])!=len(v[0]):
                raise Exception("RHS cols do not match Matrix cols")
            # update the data based on (row) slice(s)
            self.data[i] = v
        elif type(i)==tuple:#--------------------------overwrite slice of rows and cols
            row_slice,col_slice = i # extract slices
            if type(row_slice)!=slice or type(col_slice)!=slice:
                raise Exception("Incorrect Usage: Matrix[slice,slice] format or Matrix[int][int] format only ")            
            row_start,row_stop,row_step = row_slice.indices(self.m) # extract the row slice indices
            col_start,col_stop,col_step = col_slice.indices(self.n) # extract the col slice indices
            if len(v)!=(row_stop-row_start)/row_step:
                raise Exception("RHS not the same length as row slice (Matrix)")
            if len(v[0])!=(col_stop-col_start)/col_step:
                raise Exception("RHS not the same length as col slice (Matrix)")
            #-----------------------------update the data based on row and column slice(s)
            row_idx,k = row_start,0
            while row_idx < row_stop:
                self.data[row_idx][col_slice] = v[k]                
                row_idx += row_step
                k += 1

    def __len__(self):
        """returns the number of rows in the matrix"""
        return self.m
    
    def __repr__(self):
        """matrix printing utility with fixed format"""
        out = ""
        for row in self.data:          # loop over the rows
            row_str = "["    # construct the row string
            for e in row:              # loop over the columns
                row_str += "{:8.4f}, ".format(e)    # format floating point
            out += row_str[:-2] + "]\n"             # add row string to output
        return out[:-1] + "\n"         # return final output

