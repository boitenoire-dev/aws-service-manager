from setuptools import setup

setup(
  name='AWS-service-manager',
  version='0.1',
  author='Robin Norwood',
  author_email='isaacm90@gmail.com',
  summary='A CLI tool to manage AWS resources',
  license='GPLV3+',
  packages=['serviceapp'],
  url='https://github.com/boitenoire-dev/aws-service-manager',
  install_requires=[
    'click',
    'boto3'
  ],
  entry_points='''
      [console_scripts]
      servicemanager=servicemanager.servicemanager:cli
  '''
)
