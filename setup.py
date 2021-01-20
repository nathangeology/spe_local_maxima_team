from setuptools import setup, find_packages

setup(name='local_maxima',
      version='0.0.1',
      description='SPE Gulf Coast ML Competition 2021',
      url='https://github.com/nathangeology/spe_local_maxima_team',
      author='Local Maxima Team',
      author_email='nathan.geology@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
            'lasio',
            'pandas',
            'numpy',
            'scikit-learn'

      ],
      zip_safe=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      # package_data={'crcdal': [
      #     'packageData/*.csv',
      #     'packageData/*.pkl',
      #     'packageData/*.yaml',
      #     'packageData/configurations/*.yaml',
      #     'packageData/forecast_model_dictionary/*.yaml',
      #     'packageData/database_name_cleaner_tables/*.csv']}
      )
