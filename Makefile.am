## Process this file with automake to produce Makefile.in
## Created by Anjuta

SUBDIRS = src 

dragonstheycomedocdir = ${prefix}/doc/dragonstheycome
dragonstheycomedoc_DATA = \
	README\
	COPYING\
	AUTHORS\
	ChangeLog\
	INSTALL\
	NEWS


EXTRA_DIST = $(dragonstheycomedoc_DATA)


# Remove doc directory on uninstall
uninstall-local:
	-rm -r $(dragonstheycomedocdir)
