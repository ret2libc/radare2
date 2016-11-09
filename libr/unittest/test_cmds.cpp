#include "minunit.h"

bool test_emptymgr(void) {
	RCommandManager mgr;
	mu_assert("no command should be executed", !mgr.executeCommand("notfound"));
	mu_end;
}

int all_tests() {
	mu_run_test(test_emptymgr);
	return tests_passed != tests_run;
}

int main(int argc, char **argv) {
	return all_tests();
}
