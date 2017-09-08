# Ramile
_Ramile a handy tool used to automatically extract 3000 lines of source codes from given project/folder, as a requirement of China Software Copyright application process. The goal of Ramile is to save 0.5~1 hour of your time spent on preparing the 60 pages of source code for each Software Copyright submission._

## Installation

Right now we can only run Ramile from source code. In the future it may be uploaded to pypi.

To run Ramile source code, clone the repository and install dependencies: `pip install -r requirements.txt`. Or if in China, mirros could be used ` pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ -r requirements.txt`

## Basic Usage

Running from source code:
```
python ramile-cli.py extract <path to you project root>
```
When extraction is completed, a file named `extracted_code.txt` will be generated under your project root directory, with 3000 lines of code. You can just paste the content into a word document, adjust the word document to exactly 60 full pages, then it's ready to go!

## Supported languages
| Language   | Extensions             |
| :--------- | :------------------ | 
| JavaScript | .js, .jsx  |
| Java | .java |
| PHP | .php |
| HTML | .html, .htm |
| CSS | .css, .less, .sass |
