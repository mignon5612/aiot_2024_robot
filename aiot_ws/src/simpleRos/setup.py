import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'simpleRos'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob(os.path.join('launch', '*.launch.py')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='test',
    maintainer_email='mignon5612@naver.com',
    description='simpleRos demo',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "hello = simpleRos.hello:main",
            "hello_class = simpleRos.hello_class:main",
            "hello_sub = simpleRos.hello_sub:main",
            "hello_pub = simpleRos.hello_pub:main",
            "time_pub = simpleRos.time_pub:main",
            "move_turtle = simpleRos.move_turtle:main",
            "move_turtle_time = simpleRos.move_turtle_time:main",
            "service_server = simpleRos.service_server:main",
            "service_client = simpleRos.service_client:main",
            "user_int_pub = simpleRos.user_int_pub:main",
            "service_server_int = simpleRos.service_server_int:main"
            ],
    },
)
