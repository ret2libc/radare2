#ifndef R2_CMD_HPP
#define R2_CMD_HPP

extern "C" {
#include "r_cmd.h"
}

#include <string>
#include <vector>
#include <functional>
using std::string;
using std::vector;
using std::function;

template <class T> class RCommandManager;

template <class T>
class RCommandExecutor {
public:
	virtual bool execute(RCommandManager<T> &mgr, string input) = 0;
};

///
/// Represents a command that can be executed in r8 shell
///
template <class T>
class RCommand : public RCommandExecutor<T> {
public:
	RCommand(T data, string command, r_cmd_callback(callback));
	void setShortDescription(const string &descr);
	void setLongDescription(const string &descr);
	bool execute(RCommandManager<T> &mgr, string input) override;
};

///
/// Represents an alias of an existing command or alias
///
template <class T>
class RCommandAlias : public RCommandExecutor<T> {
public:
	RCommandAlias(const string &alias, const string &command, int remote);
	bool execute(RCommandManager<T> &mgr, string input) override;
};

///
/// Represents a macro command
///
template <class T>
class RCommandMacro : public RCommandExecutor<T> {
public:
	RCommandMacro(const string &name);
	bool execute(RCommandManager<T> &mgr, string input) override;
};

///
/// Collects all commands that the shell can run and execute them
///
template <class T>
class RCommandManager {
public:
	RCommandManager(T data);

	bool addCommand(RCommand<T> &cmd);
	bool delCommand(RCommand<T> &cmd);
	RCommand<T>& getCommand(const string &name);
	const vector<RCommand<T> >& listCommands();

	bool addAlias(RCommandAlias<T> &alias);
	bool delAlias(RCommandAlias<T> &alias);
	RCommandAlias<T>& getAlias(const string &name);
	const vector<RCommandAlias<T> >& listAliases();

	bool addMacro(RCommandMacro<T> &macro);
	bool delMacro(RCommandMacro<T> &macro);
	RCommandMacro<T>& getMacro(const string &name);
	const vector<RCommandMacro<T> >& listMacros();

	bool executeCommand(string cmd);
};

#endif
