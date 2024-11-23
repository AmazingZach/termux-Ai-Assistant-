# File: setup.py
from setuptools import setup, find_packages

setup(
    name="termux_ai_assistant",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "google-cloud-aiplatform>=1.35.0",
        "prompt-toolkit>=3.0.38",
        "rich>=13.6.0",
        "pyyaml>=6.0.1",
    ],
    entry_points={
        "console_scripts": [
            "tai=termux_ai_assistant.terminal_ui:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered code assistant for Termux",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
