from torch.nn.modules.module import Module
from ..functions.crop_resize import CropResizeFunction, CropResizeFunctionBCHW

class _RoICrop(Module):
    def __init__(self, layout = 'BHWD'):
        super(_RoICrop, self).__init__()
        if layout == 'BHWD':
            self.f = CropResizeFunction()
        else:
            self.f = CropResizeFunctionBCHW()
    def forward(self, input1, input2):
        return self.f(input1, input2)