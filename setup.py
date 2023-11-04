from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
desc = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="human_time",
    version="0.0.3",
    description="A module with functions to humanize time/duration.",
    long_description=desc,
    long_description_content_type="text/markdown",
    author="aiokev",
    url="https://github.com/aiokev/human_time",
    python_requires=">=3.6",
    packages=find_packages(include=["human_time", "human_time.*"]),
)
