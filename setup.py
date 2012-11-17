from setuptools import setup, find_packages

setup(
    name = "twitter-account-manager",
    version = "0.1-SNAPSHOT",
    packages = find_packages(),
    install_requires = [
      'flask==0.9',
      'Flask-DebugToolbar==0.7.1',
      'Flask-Script==0.5.1',
      'flask-peewee==0.6.1',
    ],
    extras_require= {
    },
    package_data = {
        '': ['*.txt', '*.rst', '*.md'],
    },
    author='Daroth',
    author_email='daroth@braindead.fr',
    description='Twitter account manager'
)
