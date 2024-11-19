from setuptools import setup, find_packages 


setup(
    name="projC",                     
    version="0.1.0",                        
    author="Claudia Gabriela",                       
    author_email="claudiagabriela578@gmail.com",     
    description="Ver clima",
    long_description_content_type="text/markdown",
    url="https://claudiagabriela72.github.io/python/",  
    packages=find_packages(),                
    install_requires=[                       
        "requests>=2.0.0",                         
        "PIL",
        "pytz",
        "json"
    ],
    classifiers=[                            
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',                 
)
