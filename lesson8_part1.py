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

n_layer = 1     # depth of the transformer neural network (number of layers)
n_embd = 16     # width of the network (embedding dimension)
block_size = 16 # maximum context length of the attention window (note: the longest name is 15 characters)
n_head = 4      # number of attention heads
head_dim = n_embd // n_head # derived dimension of each head
matrix = lambda nout, nin, std=0.08: [[Value(random.gauss(0, std)) for _ in range(nin)] for _ in range(nout)]
state_dict = {'wte': matrix(vocab_size, n_embd), 'wpe': matrix(block_size, n_embd), 'lm_head': matrix(vocab_size, n_embd)}

# Exercise 1
import math
import random

random.seed(42)
matrix = lambda nout, nin, std=0.08: [[Value(random.gauss(0, std)) for _ in range(nin)] for _ in range(nout)]

m = matrix(3, 4)
print("rows:", len(m), "cols:", len(m[0]))        # rows: 3 cols: 4

flat = [p for row in m for p in row]
print("flattened length:", len(flat))             # 12

# Exercise 2
def count_params(vocab_size, n_embd, block_size, n_layer):
    embeddings = vocab_size * n_embd + block_size * n_embd + vocab_size * n_embd
    attention = 4 * n_embd * n_embd
    mlp = (4 * n_embd) * n_embd + n_embd * (4 * n_embd)
    return embeddings + n_layer * (attention + mlp)

print(count_params(27, 16, 16, 1))    # 4192
print(count_params(27, 32, 16, 1))    # 14528

# Exercise 3
def softmax(logits):
    max_val = max(logits)
    exps = [math.exp(v - max_val) for v in logits]
    total = sum(exps)
    return [e / total for e in exps]

def softmax_naive(logits):          # no max-subtraction
    exps = [math.exp(v) for v in logits]
    total = sum(exps)
    return [e / total for e in exps]

p = softmax([2.0, 1.0, 0.1])
print(p, sum(p))
# [0.659, 0.2424, 0.0986]  1.0

print(softmax([1000, 1001, 1002]))
# [0.0900, 0.2447, 0.6652]

try:
    print(softmax_naive([1000, 1001, 1002]))
except OverflowError as e:
    print("naive version failed:", e)
# naive version failed: math range error

# Exercise 4
for prob in (0.9, 0.5, 1/27, 0.01):
    print(f"p={prob:.4f}  math.log(p)={math.log(prob):.4f}  -math.log(p)={-math.log(prob):.4f}")

# Exercise 5
def softmax_v(logits):
    max_val = max(v.data for v in logits)
    exps = [(v - max_val).exp() for v in logits]
    total = sum(exps)
    return [e / total for e in exps]

logits = [Value(2.0), Value(1.0), Value(0.1)]
probs = softmax_v(logits)
loss = -probs[0].log()
loss.backward()

for i, l in enumerate(logits):
    print(f"logit {i}: grad = {l.grad:.4f}")

