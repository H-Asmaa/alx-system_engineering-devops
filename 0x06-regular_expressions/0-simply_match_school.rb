#!/usr/bin/env ruby

input = ARGV[0]
regex = /School/
search = input.scan(regex).join
puts search
