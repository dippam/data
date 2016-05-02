#!/usr/bin/env ruby

require 'json'

data = JSON.parse File.read('headers.json')
subjects = data.map{|x| x['lc_subject_heading']}.uniq.sort.map{|x| x.split(' - ')}
parent = tree = {}

subjects.each_with_index do |terms, i|
  break if i > 100

  parent = tree
  
  until terms.empty?
    term = terms.shift
    parent[term] ||= {}
    parent = parent[term]
  end
end
