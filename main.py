import solve
import sys


def main():
    files = list()
    for param in sys.argv:
        files.append(param)
    Rfile = open(files[1], 'r')
    Wfile = open(files[2], 'w')
    solve.solve(Rfile, Wfile)
    Rfile.close()
    Wfile.close()


main()