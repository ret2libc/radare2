ifeq ($(OSTYPE),auto)
OSTYPE=$(shell uname | tr 'A-Z' 'a-z')
endif
ifneq (,$(findstring cygwin,${OSTYPE}))
PIC_CFLAGS=
PIC_CPPFLAGS=
else
ifneq (,$(findstring mingw32,${OSTYPE}))
PIC_CFLAGS=
PIC_CPPFLAGS=
else
ifneq (,$(findstring mingw64,${OSTYPE}))
PIC_CFLAGS=
PIC_CPPFLAGS=
else
ifneq (,$(findstring msys,${OSTYPE}))
PIC_CFLAGS=
PIC_CPPFLAGS=
else
PIC_CFLAGS=-fPIC
PIC_CPPFLAGS=-fPIC
endif
endif
endif
endif

