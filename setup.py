# setup.py
from setuptools import setup, find_packages

setup(
    name="kudet-arac-degerleme",
    version="1.0.0",
    author="Binnur Soztutar, Mert Çolakoğlu, Emrah Tunç",
    author_ID= "210316084, 220316081, 210316082",
    description="İkinci El Araç Değerleme Uygulaması",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.24.3',
        'pandas>=2.0.3',
        'matplotlib>=3.7.1',
        'seaborn>=0.12.2',
        'scikit-learn>=1.3.0',
        'jupyter>=1.0.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)