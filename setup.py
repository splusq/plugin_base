from setuptools import setup, find_packages

setup(
       name='plugin_base',
       version='0.1.0',
       description='Shared utility modules for all plugins',
       author='Microsoft',
       author_email='noreply@microsoft.com',
       packages=find_packages(),
       install_requires=[
        "aiohttp",
        "fastapi",
        "pydantic",
        "python-jose",
        "uvicorn",
    ],
   )
