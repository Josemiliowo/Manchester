from setuptools import find_packages, setup
import os
from glob import glob
from setuptools import setup

package_name = 'challenge1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Linea que hay que anadir para que se sourcee el launch folder
	    (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='emilio',
    maintainer_email='coshe1111@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            # Anadir los end-points de los 2 nodos
            'signal_generator = challenge1.signal_generator:main',
            'process_node = challenge1.process_node:main'
        ],
    },
)
