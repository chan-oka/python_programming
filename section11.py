# import logging
# from doctest import debug
#
# logging.basicConfig(level=logging.DEBUG)
# # logging.basicConfig(filename='test.log',level=logging.DEBUG)
#
# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

from optparse import OptionParser

def main():
    usage = 'usage: %prog [options] arg1 arg2'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', action='store', type='string',
                 dest='filename', help='File name')
    options, args = parser.parse_args()
    print(options.filename)
    print(type(args))

if __name__ == '__main__':
    main()