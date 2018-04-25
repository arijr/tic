import io
import string
import urllib

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage

text = "When diversity indices are used in ecology, the types of interest are usually species, but they can also be other categories, such as genera, families, functional types or haplotypes. The entities of interest are usually individual plants or animals, and the measure of abundance can be, for example, number of individuals, biomass or coverage. In demography, the entities of interest can be people, and the types of interest various demographic groups. In information science, the entities can be characters and the types the different letters of the alphabet. The most commonly used diversity indices are simple transformations of the effective number of types (also known as 'true diversity'), but each diversity index can also be interpreted in its own right as a measure corresponding to some real phenomenon (but a different one for each diversity index)"
text = text.translate(str.maketrans(" "," ", string.punctuation))
words = text.split()
wordset = set(words)

print(text)
