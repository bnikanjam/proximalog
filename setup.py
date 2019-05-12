from setuptools import find_namespace_packages, setup

setup(
    name='proximalog',
    version='0.1.0',
    packages=find_namespace_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ]
)