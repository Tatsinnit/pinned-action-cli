from setuptools import setup, find_packages

setup(
    name="pinned-actions-cli",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests", "pyyaml", "click"],
    entry_points={
        "console_scripts": [
            "pin-actions=pin_actions.pin:pin_actions",
        ],
    },
)
