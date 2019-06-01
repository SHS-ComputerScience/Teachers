class Matrix():

    _matrix = [[
            chr(x) if x < 75 else chr(x + 1) 
            for x in range(65 + y, 70 + y)
        ] 
        for y in range(0, 25, 5)
    ]

    def _encode_char(self, c):
        for x in range(5):
            if c.upper() in self._matrix[x]:
                return (x + 1, self._matrix[x].index(c.upper()) + 1)
        return None

    def _decode_char(self, x, y):
        return self._matrix[x - 1][y - 1]

    def encode(self, s):
        t = []
        for c in s:
            t.append(self._encode_char(c))
        return tuple(t)
    
    def decode(self, *coords):
        s = ''
        for i in range(len(coords)):
            s += self._decode_char(coords[0], coords[1])
        return s

    def __repr__(self):
        repr_ = ''
        for x in range(5):
            for y in range(5):
                repr_ += str(self._matrix[x][y])
                if y < 4: 
                    repr_ += ' '
            if x < 4:
                repr_ += '\n'
        return repr_


matrix = Matrix()
print(matrix)

print(matrix.encode('a'))
print(matrix.encode('bye'))
print(matrix.decode(1, 1))
print(matrix.decode((1, 2), (5, 4), (1, 5)))