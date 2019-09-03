import setuptools
    
setuptools.setup(name='multiprefixspan',
  version= '0.0.2',
  description='Implementation of Prefixspan for multiple items',
  author='Cheng-Yuan Yu',
  author_email='yu8861213@hotmail.com',
  packages=setuptools.find_packages(),
  py_modules=['multiprefixspan'],
  url = 'https://github.com/RonaldYu/multiprefixspan',
  classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"],
    python_requires='>=3.6',
  keywords = ['machine learning', 'data mining', 'sequential pattern mining', 'data exploration', 'sequential data']
 )
