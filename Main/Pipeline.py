from transformers import pipeline

import torch
import torch.nn.functional as F

classifier = pipeline("sentiment-analysis")

res = classifier("We are so happy to be here!")

print(res)
