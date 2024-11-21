from setuptools import find_packages, setup

package_name = 'sysinfo_pkg'

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
    maintainer='Angel Velasco',
    maintainer_email='davidvp.advp@gmail.com',
    description='Demo Servicios',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service_srv = sysinfo_pkg.sisinfo_server:main',
            'service_client = sysinfo_pkg.sysinfo_client:main'
        ],
    },
)
