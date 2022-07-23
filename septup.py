import setuptools
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="BMI_Calculator",
    version="0.0.1",
    author="Sandhya Mourya",
    author_email="sandhya,mourya1998@gmail.com",
    packages=["BMI_Calculator"],
    description="Calculate the BMI from the given json file ",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/sandhyamourya/code-23072022-sandhyamourya",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
