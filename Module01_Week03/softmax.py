import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        x_exp_sum = x_exp.sum(0, keepdims=True)
        return x_exp/x_exp_sum


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        x_exp_sum = x_exp.sum(0, keepdims=True)
        return x_exp/x_exp_sum


# Testcase:
if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3])
    softmax = MySoftmax()
    output = softmax(data)
    print(output)

    data = torch . Tensor([1, 2, 3])
    softmax_function = nn. Softmax(dim=0)
    output = softmax_function(data)
    assert round(output[0]. item(), 2) == 0.09
    print(output)

    data = torch . Tensor([5, 2, 4])
    my_softmax = MySoftmax()
    output = my_softmax(data)
    assert round(output[-1]. item(), 2) == 0.26
    print(output)

    data = torch . Tensor([1, 2, 300000000])
    my_softmax = MySoftmax()
    output = my_softmax(data)
    assert round(output[0]. item(), 2) == 0.0
    print(output)

    data = torch . Tensor([1, 2, 3])
    softmax_stable = SoftmaxStable()
    output = softmax_stable(data)
    assert round(output[-1]. item(), 2) == 0.67
    print(output)
