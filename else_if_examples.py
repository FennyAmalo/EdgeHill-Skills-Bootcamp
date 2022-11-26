#! /usr/bin/env python
"""
This is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version. It is
distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
the code.  If not, see <http://www.gnu.org/licenses/>.

File name: 	else_if_examples.py
Created:	June 18th, 2020
Author:	Dr. Robert Lyon (lyonro@edgehill.ac.uk)

Contact: lyonro@edgehill.ac.uk
Web: www.edgehill.ac.uk/computerscience/people/academic-staff/robert-lyon/

This is a fully functional application that has a main function.
It shows you some more complicated examples that involve using multiple
if-else statements.
"""


def main():
    """
    The entry point for program execution.

    :return: N/A
    """

    person_age = 34

    if person_age < 4:
        print("The person is a toddler.")

    elif person_age < 11:
        print("The person is of primary school age.")

    elif person_age < 17:
        print("The person is of secondary school age.")

    elif person_age < 18:
        print("The person is of college age.")

    else:
        print("The person is old enough to be a university student or member of staff.")


if __name__ == "__main__":
    # Executes the main method only if run as a script. Will not
    # execute main() if only parts of this file are imported in
    # to another file.
    main()

# a 79-char ruler:
# 234567891123456789212345678931234567894123456789512345678961234567897123456789
