# Lesson
import math

class Value:
    def __init__(self, data, children=(), local_grads=()):
        self.data = data                 # the number itself
        self.grad = 0                    # d(loss)/d(this), filled in by backward()
        self._children = children        # the Values this one was computed from
        self._local_grads = local_grads  # d(this)/d(each child)

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.data + other.data, (self, other), (1, 1))

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.data * other.data, (self, other), (other.data, self.data))

    def __pow__(self, other):
        return Value(self.data**other, (self,), (other * self.data**(other - 1),))

    def log(self):  return Value(math.log(self.data), (self,), (1 / self.data,))
    def exp(self):  return Value(math.exp(self.data), (self,), (math.exp(self.data),))
    def relu(self): return Value(max(0, self.data), (self,), (float(self.data > 0),))

    def __neg__(self):          return self * -1
    def __radd__(self, other):  return self + other
    def __sub__(self, other):   return self + (-other)
    def __rsub__(self, other):  return other + (-self)
    def __rmul__(self, other):  return self * other
    def __truediv__(self, other):  return self * other**-1
    def __rtruediv__(self, other): return other * self**-1

    def backward(self):
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._children:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        self.grad = 1
        for v in reversed(topo):
            for child, local_grad in zip(v._children, v._local_grads):
                child.grad += local_grad * v.grad

a = Value(2.0)
b = Value(3.0)
c = a * b          # 6
L = c + a          # 8
L.backward()
print(a.grad, b.grad)    # 4.0 2.0

# Exercise 1
a = Value(2.0)
b = Value(3.0)
c = a * b          # 6
L = c + a          # 8
L.backward()
print(a.grad, b.grad)    # 4.0 2.0

# Exercise 2
a = Value(3.0)
b = Value(2.0)
f = (a + b) * (a - b)
f.backward()
print(f.data, a.grad, b.grad)    # 5.0 6.0 -4.0

#exercise 3
for lr in (0.1, 0.5, 1.0, 1.1):
    x = Value(0.0)
    history = []
    for step in range(10):
        loss = (x - 3) ** 2
        loss.backward()
        x.data -= lr * x.grad
        x.grad = 0
        history.append(round(x.data, 3))
    print(f"lr={lr}: {history}")

# Exercise 4
data = [(1, 3), (2, 5), (3, 7)]
w = Value(0.0)
b = Value(0.0)
lr = 0.02

for step in range(500):
    loss = sum((w * x + b - y) ** 2 for x, y in data)
    loss.backward()
    w.data -= lr * w.grad
    b.data -= lr * b.grad
    w.grad = 0
    b.grad = 0

print(f"w = {w.data:.4f}, b = {b.data:.4f}")