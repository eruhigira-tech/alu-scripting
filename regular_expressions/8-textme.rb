#!/usr/bin/env ruby

line = ARGV[0]

from = line.match(/\[from:(.*?)\]/)[1]
to = line.match(/\[to:(.*?)\]/)[1]
flags = line.match(/\[flags:(.*?)\]/)[1]

puts "#{from},#{to},#{flags}"
