from setuptools import setup, find_packages


setup(
    name='scrapehelper',
    version='0.0.1-git',
    description='Helpful library for scraping information from web',
    url='https://github.com/sio/scrapehelper',
    author='Vitaly Potyarkin',
    author_email='sio.wtf@gmail.com',
    license='Apache',
    platforms='any',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=[
        'requests',
        'lxml',
    ],
    python_requires='>=3.3',
    zip_safe=True,
)
