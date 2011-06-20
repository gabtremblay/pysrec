#!/usr/bin/python
# srecparser.py
#
# Copyright (C) 2011 Gabriel Tremblay - initnull hat gmail.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""
    Motorola S-Record parser
    - Kudos to Montreal CISSP Groupies
"""

import sys
import srecutils
from optparse import OptionParser

def __generate_option_parser():
    usage_str = "usage: srecparser.py [options] filename"
    parser = OptionParser(usage=usage_str)

    return parser

if __name__ == "__main__":
    #http://docs.python.org/library/optparse.html
    parser = __generate_option_parser()
    (options, args) = parser.parse_args(sys.argv)

    if len(args) < 2:
        parser.print_help()
        sys.exit()






# Script entry point. hello world.
#if __name__ == "__main__":
#    scn_file = open(__FILE)
#    output = open('output.txt', "w")
#
#    if __WRAPAROUND:
#        print "- Wraparound enabled"
#
#    linecount = 0
#    for srec in scn_file:
#        # Strip some file info
#        srec = srec.strip("\n")
#        srec = srec.strip("\r")
#
#        # Validate checksum and parse record
#        if not __validate_srec_checksum(srec):
#            print "Invalid checksum found!"
#        else:
#            # Extract data from the srec
#            record_type, data_len, addr, data, checksum = __extract_data_from_srec(srec)
#
#            if record_type == 'S2':
#                # Apply offset with options
#                offset_data = __offset_data(data, __TEXT_OFFSET, __HUMAN_READABLE, __WRAPAROUND)
#
#                # If output is human readable, Get a non human readable for checksum calculation
#                if __HUMAN_READABLE:
#                    raw_offset_data = __offset_data(data, __TEXT_OFFSET, False, __WRAPAROUND)
#                else:
#                    raw_offset_data = offset_data
#
#                # Get checksum of the new offset srec
#                raw_offset_srec = ''.join([record_type, data_len, addr, raw_offset_data])
#                int_checksum = __compute_srec_checksum(raw_offset_srec)
#                checksum = __int_to_hex_byte(int_checksum)
#
#                # build output string
#                if __HUMAN_READABLE:
#                    output_str = offset_data
#                else:
#                    output_str = raw_offset_srec
#
#                if not __DATA_ONLY:
#                    output_str =  ''.join([raw_offset_srec, checksum])
#
#                if __SHOW_LINES:
#                    output_str = ''.join([str(linecount), ': ', output_str])
#
#                # output to file
#                output.write(''.join([output_str, '\n']))
#
#
#            # All the other record types
#            else:
#                output_str = ''.join([srec, '\n'])
#
#                if __SHOW_LINES:
#                   output_str = ''.join([str(linecount), ': ', output_str])
#
#                output.write(output_str)
#
#
#        # increment our fancy linecounter
#        linecount += 1
#
#    scn_file.close()
#    output.close()