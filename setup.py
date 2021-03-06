from setuptools import setup, find_packages

setup(
    name='amundsen-common',
    version='0.1.6',
    description='Common code library for Amundsen',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lyft/amundsencommon',
    maintainer='Lyft',
    maintainer_email='amundsen-dev@lyft.com',
    packages=find_packages(exclude=['tests*']),
    dependency_links=[],
    install_requires=[
        # Packages in here should rarely be pinned. This is because these
        # packages (at the specified version) are required for project
        # consuming this library. By pinning to a specific version you are the
        # number of projects that can consume this or forcing them to
        # upgrade/downgrade any dependencies pinned here in their project.
        #
        # Generally packages listed here are pinned to a major version range.
        #
        # e.g.
        # Python FooBar package for foobaring
        # pyfoobar>=1.0, <2.0
        #
        # This will allow for any consuming projects to use this library as
        # long as they have a version of pyfoobar equal to or greater than 1.x
        # and less than 2.x installed.
        'flask>=1.0.2',
    ],
    python_requires=">=3.7",
    package_data={'amundsen_common': ['py.typed']},
)
