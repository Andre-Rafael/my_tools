import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requeriments = fh.read().splitlines()

setuptools.setup(
    name='my_tools',
    version='1.0',
    author='Andre Rafael',
    author_email='andre_rafael2012@hotmail.com',
    description='The tools I use every day',
    long_description=long_description,
    url='https://github.com/Andre-Rafael/my_tools',
    license='MIT',
    packages=['my_tools'],
    install_requires=requeriments
)