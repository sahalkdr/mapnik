#!/usr/bin/env python
import nose, sys, os, getopt

def usage():
    print "test.py -h | --help"
    print "test.py [-q | -v] [-p | --prefix <path>]"

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvqp:", ["help", "prefix="])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    prefix = None
    verbose = False
    quiet = False

    for o, a in opts:
        if o == "-q":
            quiet = True
        elif o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-p", "--prefix"):
            prefix = a
        else:
            assert False, "unhandled option"
   
    if quiet and verbose:
        usage()
        sys.exit(2)
 
    if prefix:
        # Allow python to find libraries for testing on the buildbot
        sys.path.insert(0, os.path.join(prefix, "lib/python%s/site-packages" % sys.version[:3]))

    import mapnik

    if not quiet:
        print "- mapnik path: %s" % mapnik.__file__
        print "- _mapnik.so path: %s" % mapnik._mapnik.__file__
        print "- Input plugins path: %s" % mapnik.inputpluginspath
        print "- Font path: %s" % mapnik.fontscollectionpath
        print
        print "- Running nosetests:"
        print

    argv = [__file__, '--exe']

    if not quiet:
        argv.append('-v')

    if verbose:
        argv.append('-v')
        argv.append('-v')

    nose.run(argv=argv)

if __name__ == "__main__":
    main()
