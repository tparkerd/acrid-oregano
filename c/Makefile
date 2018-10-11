CC := gcc
CFLAGS := -std=gnu89 -Wall -Wextra -Werror -O3

all: array_multi_index.so summarize_variant.so imputed_genotype.so 

%.o: %.c
	$(CC) $(CFLAGS) -I/usr/pgsql-9.6/include/server -fpic -c $< # NOTE(timp): this might be the issue when it comes to installation as the guide says to use version 9.5

%.so: %.o
	$(CC) $(CFLAGS) -shared -o $@ $<

.PHONY: clean

clean:
	rm -f *.o *.so

