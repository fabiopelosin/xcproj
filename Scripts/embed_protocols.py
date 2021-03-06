#!/usr/bin/env python

import plistlib, sys

def main():
    if len(sys.argv) != 3:
        print >> sys.stderr, "Usage: %s Info.plist Protocols.m" % sys.argv[0]
        exit(1)
    
    infoPlist = sys.argv[1]
    try:
        plist = plistlib.readPlist(infoPlist)
    except:
        plist = None
    
    if plist == None:
        print >> sys.stderr, "%s is not a valid Info.plist file" % infoPlist
        exit(1)
    
    with open(sys.argv[2], "w") as f:
        f.write("#import <DevToolsCore/DevToolsCore.h>\n\n")
        f.write("// For the compiler to \"embed\" the protocols in the binary\n\n")
        f.write("void protocols()\n{\n")
        for className in sorted(plist["XCDUndocumentedChecker"]["Classes"].keys()):
            f.write("\t(void)@protocol(%s);\n" % className)
        f.write("}\n")
    
if __name__ == '__main__':
    main()
