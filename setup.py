from setuptools import setup, find_packages

setup(
    name='openprocurement.search_plugins',
    version='0.1', # NOQA
    description="Plugin for OpenProcurement Search",
    long_description=open("README.md").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
    ],
    keywords='prozorro search plugin',
    author='Volodymyr Flonts',
    author_email='flyonts@gmail.com',
    license='Apache License 2.0',
    url='https://github.com/imaginal/openprocurement.search_plugins',
    namespace_packages=['openprocurement'],
    packages=find_packages(),
    package_data={'': ['*.md', '*.txt']},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'openprocurement.search'
    ],
    entry_points={
    }
)
