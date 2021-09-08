from setuptools import setup
from setuptools_rust import Binding, RustExtension

extras = {}
extras["testing"] = ["pytest"]

setup(
    name="tokenizers_HF",
    version="0.9.4",
    description="Fast and Customizable Tokenizers",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="NLP tokenizer BPE transformer deep learning",
    author="Anthony MOI",
    author_email="anthony@huggingface.co",
    url="https://github.com/huggingface/tokenizers",
    license="Apache License 2.0",
    rust_extensions=[RustExtension("tokenizers_HF.tokenizers", binding=Binding.PyO3, debug=False)],
    extras_require=extras,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    package_dir={"": "py_src"},
    packages=[
        "tokenizers_HF",
        "tokenizers_HF.models",
        "tokenizers_HF.decoders",
        "tokenizers_HF.normalizers",
        "tokenizers_HF.pre_tokenizers",
        "tokenizers_HF.processors",
        "tokenizers_HF.trainers",
        "tokenizers_HF.implementations",
    ],
    package_data={
        "tokenizers_HF": ["py.typed", "__init__.pyi"],
        "tokenizers_HF.models": ["py.typed", "__init__.pyi"],
        "tokenizers_HF.decoders": ["py.typed", "__init__.pyi"],
        "tokenizers_HF.normalizers": ["py.typed", "__init__.pyi"],
        "tokenizers_HF.pre_tokenizers": ["py.typed", "__init__.pyi"],
        "tokenizers_HF.processors": ["py.typed", "__init__.pyi"],
        "tokenizers_HF.trainers": ["py.typed", "__init__.pyi"],
        "tokenizers_HF.implementations": ["py.typed"],
    },
    zip_safe=False,
)
