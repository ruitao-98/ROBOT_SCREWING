from setuptools import setup
import os
from glob import glob

package_name = 'mj_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yanji',
    maintainer_email='3194724637@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "robot_sim_env = mj_sim.robot_sim_env:main",
            "mpc_node = mj_sim.mpc_node:main",
        ],
    },
)
