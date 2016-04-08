#! /usr/bin/env ruby

require 'rubygems'
require 'mysql2'
require 'yaml'

def write_table table
  client = Mysql2::Client.new host: 'localhost', username: 'root', password: '', database: 'dippam_development'
  results = client.query "SELECT * FROM #{table};"
  File.write "#{table}.yml", results_to_yaml(results)
end

def results_to_yaml results
  hash = {}
  results.map { |r| hash[r['id']] = r }
  hash.to_yaml
end


tables = %w[eppi_breviates eppi_documents eppi_lc_subjects ied_categories ied_institutions ied_records pages vmr_age_groups vmr_decades vmr_denominations vmr_genders vmr_interviews]
tables.each {|t| write_table t}
