import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision import datasets

# loading training data
train_dataset = datasets.MNIST(
    root="./data", train=True, transform=transforms.ToTensor(), download=True
)
# loading test data
test_dataset = datasets.MNIST(
    root="./data", train=False, transform=transforms.ToTensor()
)

batch_size = 32
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)

# images are 28x28
input_size = 28 * 28
# 0-9 => 10 digits
output_size = 1

model = nn.Sequential(nn.Linear(input_size, output_size), nn.Sigmoid())

n_epochs = 100
history = []
loss_fn = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(n_epochs):
    for i, (images, labels) in enumerate(train_loader):
        inputs = images.view(-1, input_size)
        labels = labels.float()
        y_pred = model(inputs)
        loss = loss_fn(y_pred, labels)  # issue
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    model.eval()
    for images, labels in test_loader:
        y_pred = model(images.view(-1, 28 * 28))
        mse = loss_fn(y_pred, labels)
        mse = float(mse)
        history.append(mse)

    print(f"Finished epoch {epoch}, latest MSE {history[-1]}")
