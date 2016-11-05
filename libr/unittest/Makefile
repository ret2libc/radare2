include ../config.mk

OBJECTS = $(patsubst %.cpp,%,$(wildcard *.cpp))
LDFLAGS += -L../util -lr_util
CPPFLAGS += -I../include -g

all: $(OBJECTS)

$(OBJECTS):%:%.cpp
	$(CPP) $(CPPFLAGS) $< -o $@ $(LDFLAGS)

run: $(OBJECTS)
	./run_unit.sh

clean:
	rm -f $(OBJECTS)

.PHONY: all run
