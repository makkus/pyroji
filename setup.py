from setuptools import setup

setup(name='pyroji',
      version='0.1',
      author="Markus Binsteiner",
      author_email="makkus@gmail.com",
      install_requires=[
          "argparse",
          "requests"
      ],
      packages=["pyroji"],
      entry_points={
          'console_scripts': [
              'pyroji = pyroji.pyroji:run'
          ],
      },
      description="Project management helper"
)