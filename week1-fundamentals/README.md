import torch
import matplotlib.pyplot as plt
import requests

print("=== Testing Basic Imports ===")
print(f"PyTorch version: {torch.**version**}")
print(f"Matplotlib version: {matplotlib.**version**}")

# Simple tensor operation

x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])
z = x + y
print(f"Tensor test: {x} + {y} = {z}")

print("All tests passed! ✅")
