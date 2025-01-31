from .vae_fashion_mnist import FashionMNIST as VAE_fashion_mnist
from .vae_dsprites import DSPRITES as VAE_dsprites
from .vae_pinwheel import Pinwheel as VAE_pinwheel
from .vae_rotated_mnist import RotatedMNIST as VAE_rotated_mnist
__all__ = [VAE_dsprites, VAE_pinwheel, VAE_fashion_mnist, VAE_rotated_mnist]
