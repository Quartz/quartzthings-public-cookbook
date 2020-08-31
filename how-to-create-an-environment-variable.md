# How to create an environment variable
Environment variables are helpful when you need to store API keys or other private information but don't want to risk putting those into a script that would be committed to a public place or use information that would be different for other people who use a script.

## Figuring out which shell you're using
Where you store an environment variable depends on what shell software you use.

You can figure that out by running `echo $0` in your terminal

Below are instructions for what to do if you're using bash or zsh. If you're using a different shell, I assume you already know how to do this.

## Using bash

### In a text editor
1. open `~/.bash_profile`
2. scroll to the bottom of the file
3. add your variable in the following format:
```bash
export VARIABLE_NAME='variable_value'
```
  for instance:
```bash
export US_CENSUS_API_KEY='GBOVbxftRxgBqtQTc0AtnQ'
```  
4. save the file
5. run `source ~/.bash_profile` in your terminal to load your new settings

### From the command line
1. In your terminal, run `echo "export VARIABLE_NAME='variable_value'" >> ~/.bash_profile` for instance `echo "export US_CENSUS_API_KEY='GBOVbxftRxgBqtQTc0AtnQ'" >> ~/.bash_profile`
2. run `source ~/.bash_profile` in your terminal to load your new settings

## Using zsh

### In a text editor
1. open `~/.zshrc`
2. scroll to the bottom of the file
3. add your variable in the following format:
```bash
export VARIABLE_NAME='variable_value'
```
  for instance:
```bash
export US_CENSUS_API_KEY='GBOVbxftRxgBqtQTc0AtnQ'
```  
4. save the file
5. run `~/.zshrc` in your terminal to load your new settings

### From the command line
1. In your terminal, run `echo "export VARIABLE_NAME='variable_value'" >> ~/.zshrc` for instance `echo "export US_CENSUS_API_KEY='GBOVbxftRxgBqtQTc0AtnQ'" >> ~/.zshrc`
2. run `source ~/.zshrc` in your terminal to load your new settings
