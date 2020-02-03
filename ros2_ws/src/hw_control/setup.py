from setuptools import setup

package_name = 'hw_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Boris Boutillier',
    maintainer_email='boris.boutillier@gmail.com',
    description='Interaction with the hardware of a Jetbot',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motors = hw_control.cmd_vel_to_motors:main'
        ],
    },
)
