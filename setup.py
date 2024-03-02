from setuptools import setup, find_packages

__version__ = "0.1.2.2"

with open("README.md", "r", encoding="utf-8") as desc_long:
    description_long = desc_long.read()

setup(
    name='moonheim-sms',
    version=__version__,
    author='fafatypoty',
    author_email='fafatypoty@proton.me',
    description=(
        'Асинхронный модуль для работы с Moonheim SMS API'
    ),
    long_description=description_long,
    long_description_content_type='text/markdown',
    project_urls={
        "Telegram": "https://t.me/fafatypoty_cloaca",
        "Github": "https://github.com/fafatypoty/moonheim-sms",
    },
    license='Apache License, Version 2.0, see LICENSE file',
    packages=find_packages(include=["moonheim_sms", "moonheim_sms.*"]),
    zip_safe=False,
    install_requires=["setuptools",
                      "pydantic",
                      "aiohttp"],
    python_requires=">=3.7",
    keywords=['moonheim', 'moonheim api', 'asyncmoonheim', 'moonheim sms', 'moonheimsms'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: Apache Software License',  # Again, pick a license

        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
