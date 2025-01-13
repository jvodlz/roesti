# Roesti

Check your file hash to verify file integrity.


## Features
- Modes: 
    - Compare File Hash
    - Generate File Hash
- Terminal help documentation
- Loading status bar

## Suported Hash Algorithms
- MD4
- MD5
- SHA-1
- SHA-256
- SHA-512

## What is a hash?
Hashes can verify that a file has not been altered or corrupted. By comparing the hash of a file, we can ensure its integrity.

## Mode Description
### Compare File Hash
 A common use case is verifying that a downloaded file or application has not been tampered with, providing assurance that the content is authentic and safe to use.

 **Roesti** will inform you whether or not the compared hashes are the same

 #### Hashes match 
 `Match success! Both hashes are the same.`

 #### Hash do not match
 `Both hashes are different.`

### Generate File Hash
You may consider generating file hashes when you want to verify its integrity **_before and after_** the file transfer, or when you have made a **_copy_** of it. 

> **Important:** ZIP files are supported. However, they are not the same as a directory/folder. It is important to ensure the file path provided to Roesti is not a directory. 

## Requirements
- [Python](https://www.python.org) is installed
- Install requirements using `pip install -r requirements.txt`

## Getting Started
- Use `python main.py roesti` to run the app
- For help, use `python main.py --help` to view available commands
    - For specific commands e.g. `python main.py generate-file-hash --help`
