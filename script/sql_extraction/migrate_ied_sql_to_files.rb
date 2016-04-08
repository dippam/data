#! /usr/bin/env ruby

require 'rubygems'
require 'mysql2'

client = Mysql2::Client.new host: 'localhost', username: 'root', password: '', database: 'dippam_development'

results = client.query 'SELECT id, transcript FROM ied_records;'

results.each_with_index do |row, i|
  File.write("#{row['id']}.txt", row['transcript'])
  puts i
end
