from setuptools import setup

with open('README.rst') as f:
    LONG_DESCRIPTION = f.read()

if __name__ == "__main__":
    setup(
        # Needed to silence warnings (and to be a worthwhile package)
        name='Dnn-Inference',
        url='https://github.com/statmlben/dnn-inference',
        author='Ben Dai',
        author_email='bdai@umn.edu',
        # Needed to actually package something
        packages=['Dnn-Inference'],
        # Needed for dependencies
        install_requires=['numpy', 'keras', 'tensorflow', 'scipy', 'sklearn'],
        # *strongly* suggested for sharing
        version='0.1.1',
        # The license can be anything you like
        license='MIT',
        description='Dnn-Inference is a Python module for hypothesis testing based on deep neural networks.',
        #cmdclass={"build_ext": build_ext},
        # We will also need a readme eventually (there will be a warning)
        long_description=LONG_DESCRIPTION
    )
