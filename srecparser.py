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
    usage_str = "usage: %prog [options] filename"
    parser = OptionParser(usage=usage_str)
    parser.add_option("-r", action="store_true",
                      dest="readable", help="Human-readable output [default: %default]", default=False)
    parser.add_option("-w", action="store_true",
                      dest="wraparound", help="Wrap around characters [default: %default]", default=True)
    parser.add_option("-c", action="store_true",
                      dest="validate_checksum", help="Disable checksum validation [default: %default]", default=False)
    parser.add_option("-l", action="store_true",
                      dest="print_lines_number", help="Print line number [default: %default]", default=False)
    parser.add_option("-d", action="store_true",
                      dest="data_only", help="Data only [default: %default]", default=False)
    parser.add_option("-o", metavar="OFFSET", dest="offset", help="Add OFFSET to bytes [default: %default]", default=0)

    return parser


if __name__ == "__main__":
    parser = __generate_option_parser()
    (options, args) = parser.parse_args(sys.argv)
    print options

    if len(args) <= 1 or len(args) > 2:
        parser.print_help()
        sys.exit()

    # open input file
    scn_file = open(args[1])

    if options.wraparound:
        print "- Wrap around enabled"

    linecount = 0
    for srec in scn_file:
        # Strip some file content
        srec = srec.strip("\n")
        srec = srec.strip("\r")

        # Validate checksum and parse record
        if options.validate_checksum and not srecutils.validate_srec_checksum(srec):
            print "Invalid checksum found!"
        else:
            # Extract data from the srec
            record_type, data_len, addr, data, checksum = srecutils.parse_srec(srec)

            if record_type == 'S2':
                # Apply offset with options
                if options.offset != int(0):
                    offset_data = srecutils.offset_data(data, int(options.offset), options.readable, options.wraparound)
                else:
                    offset_data = data

                # If output is human readable, Get a non human readable for checksum calculation
                if options.readable:
                    raw_offset_data = srecutils.offset_data(data, int(options.offset), False,  options.wraparound)
                else:
                    raw_offset_data = data

                # Get checksum of the new offset srec
                raw_offset_srec = ''.join([record_type, data_len, addr, raw_offset_data])
                int_checksum = srecutils.compute_srec_checksum(raw_offset_srec)
                checksum = srecutils.int_to_padded_hex_byte(int_checksum)

                # build output string
                if options.readable:
                    output_str = offset_data
                else:
                    output_str = raw_offset_srec

                if not options.data_only:
                    output_str =  ''.join([raw_offset_srec, checksum])

                if options.print_lines_number:
                    output_str = ''.join([str(linecount), ': ', output_str])

                # output to file
                print ''.join([output_str, '\n']),


            # All the other record types
            else:
                output_str = ''.join([srec, '\n'])

                if options.print_lines_number:
                   output_str = ''.join([str(linecount), ': ', output_str])

                print output_str,


        # increment our fancy linecounter
        linecount += 1

    scn_file.close()