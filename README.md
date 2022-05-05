# ez_alias

## what?

ez_alias is an alias helper for the burn again shell.
Adding aliases to .bashrc can now be done with a simple command
brought to you by python.

## how?

You need to have >= python3 installed.\
Clone this repo with ```git clone https://github.com/1R13/ez_alias.git ```.
After cloning make the install file executable with ```chmod +x install```.
By executing it ```./install```, it will add an alias for ez_alias and source .bashrc.\
You're finished setting up.

## help

	Usage:  c_alias [options]
		
	Options:
	-l                                      list all aliases
	-a <alias_name> <alias_function>        add alias
	-r <alias_name>                         remove alias
	-f <alias_name>                         find alias
