a, b, c = map(int, input().split())

V = a * b * c;
S = 2 * (a * b + b * c + a * c);

print(V, S)