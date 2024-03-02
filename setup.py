from setuptools import setup, find_packages
from moonheim_sms.__version__ import __version__

# def requirements():
#     requirements_list = list()
#     with open('requirements.txt') as pc_requirements:
#         for install in pc_requirements:
#             requirements_list.append(
#                 install.strip()
#             )
#     return requirements_list


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

        'License :: OSI Approved :: MIT License',  # Again, pick a license

        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
