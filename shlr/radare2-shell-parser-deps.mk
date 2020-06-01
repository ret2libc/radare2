LINK+=$(STOP)/radare2-shell-parser/libshell-parser.$(EXT_AR)
ifeq ($(USE_LIB_TREESITTER),1)
LINK+=$(LIBTREE_SITTER)
LDFLAGS+=${LIBTREE_SITTER}
else
LINK+=$(STOP)/tree-sitter/libtree-sitter.$(EXT_AR)
endif
