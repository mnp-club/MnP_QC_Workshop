from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
	name='mnp_qc_workshop_2020',
	version='0.1',
	description='Used for verifying the answers',
	long_description=readme,
    long_description_content_type="text/markdown",
	url='#',
	author='Mahadevan Subramanian',
	author_email='mahadevan.subramanian2432@gmail.com',
	license='unlicense',
	packages=find_packages(include=['mnp_qc_workshop_2020',
					  				'mnp_qc_workshop_2020.*']),
	classifiers=[
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
    ],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
)