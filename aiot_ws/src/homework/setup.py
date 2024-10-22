from setuptools import find_packages, setup

package_name = 'homework'

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
    maintainer='test',
    maintainer_email='mignon5612@naver.com',
    description='homework demo',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "message_class = homework.message_class:main",
            "message_pub = homework.message_pub:main",
            "message_sub = homework.message_sub:main"
        ],
    },
)
