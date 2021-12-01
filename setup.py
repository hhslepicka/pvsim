import versioneer
from setuptools import (setup, find_packages)

with open('requirements.txt') as f:
    requirements = f.read().split()

git_requirements = [r for r in requirements if r.startswith('git+')]
requirements = [r for r in requirements if not r.startswith('git+')]
if len(git_requirements) > 0:
    print("User must install the following packages manually:\n" +
          "\n".join(f' {r}' for r in git_requirements))

setup(name='pvsim',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      license='Apache License 2.0',
      author='hhslepicka',
      install_requires=requirements,
      packages=find_packages(),
      description='Small simulator of PVAccess PVs',
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'pvsim=pvsim:main'
          ]
      }
      )