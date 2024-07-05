import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPONAME = 'chickenshit-classification'
AUTHOR_USERNAME = 'deng-snippets'
SRC_REPO_URL = 'cnnClassifier'
AUTHOR_EMAIL = 'pdmisc@pm.me'

setuptools.setup(
    name=REPONAME,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description='A CNN classifier',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR_USERNAME}/{SRC_REPO_URL}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOR_USERNAME}/{SRC_REPO_URL}/issues'
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
)