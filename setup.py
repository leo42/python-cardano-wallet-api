from distutils.core import setup
setup(
  name = 'python-cardano-wallet-api',         
  packages = ['python-cardano-wallet-api'],   
  version = '0.0.1',      
  license='Apache',      
  description = 'A python wrapper for the Cardano-node API',  
  author = 'Leandros Holleman',                  
  author_email = 'leantrosh@gmail.com',     
  url = 'https://github.com/leo42/python-cardano-wallet-api',  
  download_url = 'https://github.com/leo42/python-cardano-wallet-api/archive/refs/tags/0.0.1.tar.gz',    
  keywords = ['Cardano-wallet', 'API', 'Wrapper'],  
  install_requires=[            # I get to this in a second
          'json',
          'requests',
      ],
  classifiers=[
    'Development Status  3 - Alpha',      # Chose either 3 - Alpha, 4 - Beta or 5 - ProductionStable as the current state of your package
    'Intended Audience  Developers',      # Define that your audience are developers
    'Topic  Software Development  Build Tools',
    'License  OSI Approved  Apache License',   # Again, pick a license
    'Programming Language  Python  3',      #Specify which pyhton versions that you want to support
    'Programming Language  Python  3.4',
    'Programming Language  Python  3.5',
    'Programming Language  Python  3.6',
  ],
)