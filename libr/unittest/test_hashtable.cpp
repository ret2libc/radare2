extern "C" {
#include <r_util.h>
#include "minunit.h"
}

bool test_r_hashtable_insert_lookup(void) {
	RHashTable* ht = r_hashtable_new ();
	const char* test1_key = "AAAA";
	const char* test2_key = "BBBB";
	const char* test3_key = "CCCC";
	const char* test1_data = "1111";
	const char* test2_data = "2222";
	const char* test3_data = "3333";
	const char* data_lookup;
	mu_assert ("insert first key-value",
			r_hashtable_insert (ht, r_str_hash (test1_key), (void*)test1_data));
	mu_assert ("insert second key-value",
			r_hashtable_insert (ht, r_str_hash (test2_key), (void*)test2_data));
	mu_assert ("insert third key-value",
			r_hashtable_insert (ht, r_str_hash (test3_key), (void*)test3_data));
	data_lookup = (const char *)r_hashtable_lookup (ht, r_str_hash (test1_key));
	mu_assert_streq (data_lookup, test1_data, "AAAA key value lookup");
	data_lookup = (const char *)r_hashtable_lookup (ht, r_str_hash (test2_key));
	mu_assert_streq (data_lookup, test2_data, "AAAA key value lookup");
	data_lookup = (const char *)r_hashtable_lookup (ht, r_str_hash (test3_key));
	mu_assert_streq (data_lookup, test3_data, "AAAA key value lookup");
	r_hashtable_free (ht);
	mu_end;
}

bool test_r_hashtable_removal_lookup(void) {
	RHashTable* ht = r_hashtable_new ();
	const char* test1_key = "AAAA";
	const char* test1_data = "1111";
	const char* data_lookup;
	// First insert AAAA.
	mu_assert ("insert first key-value",
			r_hashtable_insert (ht, r_str_hash (test1_key), (void*)test1_data));
	// Check we can look it up.
	data_lookup = (const char *)r_hashtable_lookup (ht, r_str_hash (test1_key));
	mu_assert_streq (data_lookup, test1_data, "AAAA key value lookup");
	// Now remove it, make sure it's really gone.
	r_hashtable_remove (ht, r_str_hash (test1_key));
	mu_assert_eq (
			(int)(intptr_t)(const char *)r_hashtable_lookup (ht, r_str_hash (test1_key)), 0,
			"lookup of removed key");
	r_hashtable_free (ht);
	mu_end;
}

bool test_r_hashtable_insert_collision(void) {
	RHashTable* ht = r_hashtable_new ();
	const char* test1_key = "AAAA";
	const char* test1_data = "1111";
	const char* test1_data_2 = "2222";
	const char* data_lookup;
	// First insert AAAA.
	mu_assert_eq (r_hashtable_insert (ht, r_str_hash (test1_key),
				(void*)test1_data),
			true, "insert without collision");
	//XXX: THIS BEHAVIOR IS BROKEN! This should fail (return false) on failure.
	mu_test_status = MU_TEST_BROKEN; // Only for this assertion.
	mu_assert_eq (r_hashtable_insert (ht, r_str_hash (test1_key),
				(void*)test1_data_2),
			false, "insert collision!");
	// Check we can look it up. Should be the first one because the second
	// failed to add.
	data_lookup = (const char *)r_hashtable_lookup (ht, r_str_hash (test1_key));
	mu_assert_streq (data_lookup, test1_data, "AAAA key value lookup");
	r_hashtable_free (ht);
	mu_end;
}

int all_tests() {
	mu_run_test(test_r_hashtable_insert_lookup);
	mu_run_test(test_r_hashtable_removal_lookup);
	mu_run_test(test_r_hashtable_insert_collision);
	return tests_passed != tests_run;
}

int main(int argc, char **argv) {
	return all_tests();
}
