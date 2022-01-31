from distutils.core import setup
setup(
  name = 'cwAPI',         
  packages = ['cwAPI'],   
  version = '0.0.3',      
  license='Apache',      
  description = 'A python wrapper for the Cardano-node API',  
  author = 'Leandros Holleman',                  
  author_email = 'leantrosh@gmail.com',     
  url = 'https://github.com/leo42/python-cardano-wallet-api',  
  download_url = 'https://github.com/leo42/python-cardano-wallet-api/archive/refs/tags/0.0.3.tar.gz',    
  keywords = ['Cardano-wallet', 'API', 'Wrapper'],  
  install_requires=[            # I get to this in a second
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either 3 - Alpha, 4 - Beta or 5 - ProductionStable as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'License :: OSI Approved :: Apache Software License',   # Again, pick a license
    'Programming Language :: Python :: 3'
  ],
)