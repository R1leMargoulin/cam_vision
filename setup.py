from setuptools import find_packages, setup

package_name = 'cam_vision'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='r1',
    maintainer_email='erwan.martin@viacesi.fr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cam_publisher = cam_vision.cam_publisher:main',
            'cam_subscriber = cam_vision.cam_subscriber:main',
        ],
    },
)