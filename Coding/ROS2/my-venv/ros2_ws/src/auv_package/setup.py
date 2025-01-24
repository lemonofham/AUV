from setuptools import find_packages, setup

package_name = 'auv_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('lib/' + package_name + '/Python', [package_name+'/Python'+'/Detector.py']),
        ('lib/' + package_name + '/Python', [package_name+'/Python'+'/utils.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pratham',
    maintainer_email='prathamchollera0015@gmail.com',
    description='AUV Tasks',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = auv_package.camera_publisher:main',
            'listener = auv_package.detected_shapes_colours:main',
            'middle = auv_package.vision_detector_node:main',
        ],
    },
)
