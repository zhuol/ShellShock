#!/usr/bin/env perl
use strict;
use warnings;
use Carp 'croak';

my $version = get_version();
print "Bash version $version detected\n";

sub get_version {
    run_command( 'bash --version', qr/\d\.\d\.\d+/ );
}

sub run_command {
    my ( $command, $regex ) = @_;
    my $output = `$command`;
    $output =~ /($regex)/;
    $1 or croak "Command returned no output";
}
