# Ramile

_Ramile a handy tool used to automatically extract 3000 lines of source codes from given project/folder, as a requirement of China Software Copyright application process. The goal of Ramile is to save 0.5~1 hour of your time spent on preparing the 60 pages of source code for each Software Copyright submission._
Currently Ramile has below features:

- Automatically extracting the source code and generating a docx file containing 3000 lines. (You have to manually remove the last few pages of the docx to make it exactly 60 pages, though)
- Supporting most of the commmon front-end projects: android/ios/web/Wechat mini program, etc
- Configurable. Just place a `.ramileconfig.json` under the project root folder. (See "Config" section for details)

Tested under python 3.6.1.

## Installation

Right now we can only run Ramile from source code. In the future it may be uploaded to pypi.

To run Ramile source code, clone the repository and install dependencies: `pip install -r requirements.txt`. Or if in China, mirros could be used `pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ -r requirements.txt`

## Basic Usage

Running from source code:

```
python ramile-cli.py extract <path to your project root>
```

When the extraction is completed, a file named `extracted_code.docx` will be generated under your project root directory, with 3000 lines of code. You just have to open it and remove unnecessary pages to make the document exact 60 pages.

If you want to strictly meet the [regulation](./著作权法.md#第十条-软件的鉴别材料包括程序和文档的鉴别材料), you can extract all the lines by append `Inf` to the command line:

```
python ramile-cli.py extract <path to your project root> Inf
```

And then you just have to open it and keep the first 30 pages and the last 30 pages, and remove all the intermediate pages.

## Config

Ramile automatically loads the config file `.ramileconfig.json` from the project root, if it exits. The file should be in json format. Possible config items as below:

| Key         | Description                                                                                                                                                                                                                          | Default | Example          |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ | :--------------- |
| ignore      | Sets the directories/files to be ignored by Ramile. "ignore" paths should be sub directories/files under source_root. Any directories/files starting with any one of the "ignore" items will be ignored. Wildcars are not supported. | []      | ['Pods', 'libs'] |
| source_root | Overwrites the root directory of source codes to avoid Ramile process from the project root.                                                                                                                                         | ''      | 'app'            |
| filters     | Sets the exclusive filters (which means, all other extensions will NOT be processed) for file extensions. By default all files will be processed.                                                                                    | []      | ['.js', '.vue']  |

## Supported Languages

| Language    | Extensions            |
| :---------- | :-------------------- |
| JavaScript  | .js, .jsx, .vue, .wpy |
| Java        | .java                 |
| PHP         | .php                  |
| HTML        | .html, .htm           |
| CSS         | .css, .less, .sass    |
| Swift       | .swift                |
| Objective-C | .m                    |
