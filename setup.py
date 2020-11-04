from setuptools import setup

setup(name='pysassquatch',
      version='0.0.2',
      description='App for converting sqss files into qss files',
      url='#',
      author='Kyle Huggins',
      author_email='khuggins@freng.com',
      license='MIT',
      packages=['pysassquatch'],
      entry_points={
        'console_scripts': [
            'pysassquatch-convert = pysassquatch.main:main'
        ]
      },
      zip_safe=False)
