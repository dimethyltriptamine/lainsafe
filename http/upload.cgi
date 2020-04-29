#!/usr/bin/perl
# This file is part of lainsafe.

# lainsafe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# lainsafe is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with lainsafe.  If not, see <https://www.gnu.org/licenses/>.

use CGI;
use CGI::Carp qw(fatalsToBrowser);
my $q = CGI->new;

my $filename = $q->param('file');
# TODO: fix 502

my $upload_dir = "files/";
print $q->header();
$size    = $ENV{CONTENT_LENGTH};

# Configuration

$MAX_SIZE = 1024*1024*10; # Change for your size
$MAX_SIZE_MB = $MAX_SIZE / 1024 / 1024; # Don't change this

if($filename eq "")
{
    print("What are you looking for?");
    exit;
}

if($size > $MAX_SIZE)
{
    print("Max size for a file is $MAX_SIZE_MB MBs");
    exit;
}

my $extension = $filename;
$extension =~ s/.*\.//; # tar.gz sucks with this

my @chars = ("A".."Z", "a".."z");
my $string;
$string .= $chars[rand @chars] for 1..8;
my $upload_filehandle = $q->upload("file");

$filename = $string . "." . $extension;

open(FILE,">$upload_dir/$filename");
binmode(FILE);
while(<$upload_filehandle>)
{
    print FILE;
}

close FILE;

print $ENV{HTTP_REFERER} . "$upload_dir$filename";
