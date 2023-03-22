template<typename T>
class BinaryIndexedTree {
 public:
  BinaryIndexedTree(size_t n): n_(n) { bit_.resize(n + 1); }
  T sum(size_t i) { T s = 0; while (i > 0) { s += bit_[i]; i -= i & -i; } return s; }
  void add(size_t i, T x) { while (i <= n_) { bit_[i] += x; i += i & -i; } }

 private:
  size_t n_;
  std::vector<T> bit_;
};

