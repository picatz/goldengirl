require "sinatra"
require "thin"
require "json"

set :bind, '0.0.0.0'
set :port, 9200
set :dump_errors, false
set :raise_errors, false
set :show_exceptions, false
set :logging, true

inserted = { "_id": 31337 }.to_json
found    = { found: true  }.to_json

before do
  content_type :json
end

post "/*" do
  status 201
  inserted  
end

get "/*" do
  status 200
  found
end

not_found do
  status 200
end

error do
  status 200
end
