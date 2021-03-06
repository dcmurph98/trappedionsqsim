try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Quantum and Classical Simulations for Trapped Ions',
    'author': 'Omid Khosravani, Lauren Lopez',
    'url': 'https://github.com/trxw/trappedionsqsim',
    'version': '0.1',
    'install_requires': ['qutip', 'numpy', 'matplotlib', 'scipy'],
    'packages': ['operators',],
    'name': 'trappedionsqsim'
}

setup(**config)
