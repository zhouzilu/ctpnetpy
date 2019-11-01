import setuptools
setuptools.setup(
     name='cTPnet',  
     version='0.2.6',
     author="Zilu Zhou",
     author_email="zhouzilu@pennmedicine.upenn.edu",
     description="support python pacakge for single cell transcriptome to surface protein imputation",
     long_description=open('README.md').read(),
     long_description_content_type="text/markdown",
     url="https://github.com/zhouzilu/cTPnetpy",
     packages=setuptools.find_packages(),
     python_requires='>=3.5',
     install_requires=['numpy>=1.15.4',
        'torch>=0.4.1',
        'pandas>=0.23.4'
        ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
         "Operating System :: OS Independent",
     ],
 )
