from setuptools import setup, find_packages

setup(
    name='phrasecutapi',
    version='0.0.0',
    packages=find_packages(),
    python_requires='>=3',
    install_requires=[
        # note that these requirements may not be exhaustive
        # 'matplotlib==3.1.1',
        # 'numpy==1.17.4',
        # 'pillow==6.1.0',
        # 'requests==2.22.0',
        'gdown==3.9.0',
    ],
)