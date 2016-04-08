#! /usr/bin/env ruby

require 'zlib'

# From looking at the database, pages 99779..100554 belong
# to document 20601 and are in sorted order.

File.open './20601.txt', 'w' do |out|
  99779.upto 100554 do |i|
    Zlib::GzipReader.open("../../pages/gz/#{i}.txt.gz") do |gz|
      out.puts "#{gz.read}\f"
    end
  end
end
