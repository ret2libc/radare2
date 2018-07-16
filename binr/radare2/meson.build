executable('radare2', 'radare2.c',
  include_directories: [platform_inc],
  dependencies: [
    r_util_dep,
    r_socket_dep,
    r_core_dep,
    r_io_dep,
    r_fs_dep,
    r_bin_dep,
    r_flag_dep,
    r_cons_dep,
    r_asm_dep,
    r_debug_dep,
    r_config_dep,
    r_bp_dep,
    r_reg_dep,
    r_syscall_dep,
    r_anal_dep,
    r_parse_dep,
    r_egg_dep,
    r_search_dep,
    r_hash_dep,
    r_crypto_dep,
    r_magic_dep
  ],
  install: true,
  implicit_include_directories: false
)

if host_machine.system() != 'windows'
  link_file = '@0@/bin/r2'.format(r2_prefix)
  custom_target(
    output: link_file,
    build_by_default: true,
    build_always_stale: true,
#    command: 'ln -s @0@/bin/radare2 @1@'.format(r2_prefix, link_file)
  )
endif
