from setuptools import find_packages, setup

setup(
  name='Thyme2Eat',
  version='1.0.0',
  packages=find_packages(),
  include_package_data=True,
  install_requires=[
    'flask',
    'flask-bcrypt',
    'flask-sqlalchemy'
    'flask-wtf'
    'wtforms-alchemy',
    'psycopg2-binary',
    'wtforms'
  ]
)