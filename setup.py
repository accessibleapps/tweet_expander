from setuptools import setup

__version__ = 0.1
__doc__ = """Determine if certain links can have their text automatically expanded, and do so"""

setup(
 name = 'tweet_expander',
 version = __version__,
 description = __doc__,
 py_modules = ['tweet_expander'],
 install_requires = [
  'twitlonger',
  'twishort',
 ],
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'Topic :: Software Development :: Libraries',
 ],
)
