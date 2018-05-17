#####################  IMPORT BIBLIOTECAS ########################

import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters.rank import entropy
from skimage.morphology import disk

##################### FIM IMPORT BIBLIOTECAS ########################

imagem = "macacofezsilfie.jpg" #imagem que será analizada
image = imread(imagem, as_grey= True) # Função da bbilioteca skimage que será usada para ler a imagem e converter para escala de cinza,
                                      #

fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(12, 4),
                               sharex=True, sharey=True)

img0 = ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title("Image")
ax0.axis("off")
fig.colorbar(img0, ax=ax0)

img1 = ax1.imshow(entropy(image, disk(5)), cmap='gray')
ax1.set_title("Entropy")
ax1.axis("off")
fig.colorbar(img1, ax=ax1)

fig.tight_layout()

plt.show()
