from typing import Callable, Sequence, Any


class BinaryIndexedTree:
    def __init__(
            self,
            n_or_xs: int,
            ident: Any = 0,
            op: Callable[[Any, Any], Any] = int.__add__,
            neg: Callable[[Any], Any] = int.__neg__,
    ) -> None:
        if isinstance(n_or_xs, Sequence):
            n = len(n_or_xs)
        elif isinstance(n_or_xs, int):
            n = n_or_xs
        else:
            raise ValueError('invalid input: n_or_xs')

        self.n = n
        self.data = [ident for _ in range(n + 1)]

        # define group
        self.ident = ident
        self.op = op
        self.neg = neg

        # populate initial elements
        if isinstance(n_or_xs, Sequence):
            for i in range(n):
                self.add(i, n_or_xs[i])

    def sum(self, i: int) -> Any:
        s = self.ident
        while i > 0:
            s = self.op(s, self.data[i])
            i -= i & -i
        return s

    def add(self, i: int, x: int) -> None:
        i += 1
        while i <= self.n:
            self.data[i] = self.op(self.data[i], x)
            i += i & -i

    def update(self, i: int, x: int) -> None:
        prev = self.query(i, i + 1)
        self.add(i, self.op(x, self.neg(prev)))

    def query(self, a: int) -> Any:
        for i in range(a):
            total =  self.op(self.sum(i), self.neg(self.sum(a)))
        return total
    
    def get_input():
        inputLine = input().split(" ")
        n = int(inputLine[0])
        q = int(inputLine[1])
        bIT = BinaryIndexedTree(n, None, None, None )
        for i in range(q):
            line = [x for x in input().split(' ')]
            if len(line) > 1:
                #call update 
                bIT.update(int(line[1]), int(line[2]))
            else:
                #call query
                bIT.query(int(line[1]))


    if __name__ == "__main__":
         get_input()