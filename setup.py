import setuptools
import toolbox as package

setuptools.setup(
    name=package.__name__,
    version=package.__version__,
    author="DataJoint Contributor",
    author_email="example@email.com",
    description="Package description.",
    packages=setuptools.find_packages(exclude=['tests*']),
)
