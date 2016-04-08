#! /usr/bin/env ruby

require 'rubygems'
require 'mysql2'

client = Mysql2::Client.new host: 'localhost', username: 'root', password: '', database: 'dippam_development'

results = client.query 'SELECT id, clean_content FROM pages WHERE clean_content IS NOT NULL;'

results.each_with_index do |row, i|
  File.write("#{row['id']}.txt", row['clean_content'])
  puts i
end
