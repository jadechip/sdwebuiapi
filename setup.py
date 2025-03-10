""" See:
https://github.com/mix1009/sdstarrysky
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="starrysky",
    version="0.9.3",
    description="Python API client for AUTOMATIC1111/stable-diffusion-webui",
    url="https://github.com/mix1009/sdstarrysky",
    author="ChunKoo Park",
    author_email="mix1009@gmail.com",
    keywords="stable-diffuion-webui, AUTOMATIC1111, stable-diffusion, api",
    packages=["starrysky"],
    #packages=find_packages(),
    python_requires=">=3.7, <4",
    install_requires=['requests',
                      'Pillow',],
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
)
