#ifndef R2_CMD_H
#define R2_CMD_H

#include <string>
using std::string;

///
/// Represents a command that can be executed in r8 shell
///
class RCommand {
public:
	virtual bool execute(string input);
};

///
/// Collects all commands that the shell can run and execute them
///
class RCommandManager {
public:
	bool addCommand(string name);
	bool executeCommand(string cmd);
};

#endif
