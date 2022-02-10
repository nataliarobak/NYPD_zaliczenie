from setuptools import setup
setup(
    name="library",
    version="0.1.0",
    packages=["src"],
    package_dir={"": "."},
    author="Natalia Robak, 421550",
    author_email="n.robak@student.uw.edu.pl",
    description="Biblioteka do testowania danych na temat choroby Parkinsona",
    install_requires=["pandas >= 1.3.5",
                      "numpy >= 1.21.5",
                      "matplotlib >= 3.5.1"]
)
