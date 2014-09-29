from setuptools import setup

packages = ['memory_tools']
required_modules = [
    "colorama==0.3.2",
    "psutil==2.1.1"
]


setup(name='memory_tools',
      version='0.1.0',
      description='Tools to help with memory leaks',
      url='http://github.com/jtushman/memory_utils',
      author='Jonathan Tushman',
      author_email='jonathan@zefr.com',
      install_requires=required_modules,
      license='MIT',
      packages=packages,
      zip_safe=False,
      tests_require=['nose'],
      test_suite='nose.collector',
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
      ]
)