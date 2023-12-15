from setuptools import setup, find_packages

setup(
    name = 'img64',
    version = '0.0.3',
    description = "This library is a tool for converting images to base64 encoding and vice versa.",
    long_description = open('README.md', encoding='utf-8').read(),
    long_description_content_type = 'text/markdown',
    author = 'gibiee',
    author_email = 'gibiee@naver.com',
    url = 'https://github.com/gibiee/img64',
    download_url = '',
    packages = find_packages(exclude=[]),
    include_package_data = True,
    zip_safe = False,
    install_requires = ['pillow', 'numpy'],
    python_requires ='>=3',
    license = 'MIT',
    keywords = ['image', 'base64', 'image_base64'],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)