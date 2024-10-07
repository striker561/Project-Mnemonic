# Project Mnemonic 

## Overview

Welcome to the **Project Mnemonic **! This Python application generates all possible combinations of BIP-39 Bitcoin mnemonic phrases. Using a combination of randomness and a list of words, it can create secure mnemonic phrases that help users manage their cryptocurrency wallets effectively.

## Disclaimer

**Important**: This tool is intended for educational and research purposes only. **Do not attempt to use this application to generate mnemonic phrases for other users' wallets or for any malicious activities**. Misuse of this tool can result in legal consequences and is strictly against ethical standards. Always respect users' privacy and security.


## Features

- **Generate BIP-39 compliant mnemonic phrases**: Create secure and easy-to-remember phrases to back up your wallet.
- **Configurable word count**: Customize the length of your mnemonic phrase (12, 15, 18, 21, or 24 words).
- **Random sampling**: Efficiently select unique phrases from generated permutations.

## Installation

To use this application, clone the repository to your local machine:

```bash
git clone https://github.com/striker/project-mnemonic.git
cd project-mnemonic
```

It uses python builtin dependencies and requirements

## Usage
To generate a mnemonic phrase, run the following command in your terminal:

```bash
python app.py
```

You can customize the number of words by modifying the get_random_phrases function call in app.py:

```bash
print(get_random_phrases(A_Z_WORDS, 24, True))  # Change 24 to your desired word count
```

## Saving Generated Phrases

The generated phrases can be saved to a text file. Simply call the save_to_txt function in your code to save your phrases:

```bash
save_to_txt("your_generated_phrases", "mnemonic_phrases.txt")
```

## Performance

This generator can handle large permutations, but remember, the real power comes when you have a CPU or GPU that can flex its muscles! 🚀💪 So, if you're planning to generate a vast number of phrases, make sure you have the hardware to back it up. Otherwise, you might just end up with a phrase like "This process is taking forever!"


## Contributing
Contributions are welcome! If you have ideas for enhancements or find bugs, please submit an issue or a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- BIP-39 Specification for the mnemonic phrase generation process.
- The open-source community for making development easier and more enjoyable.
