FROM ruby:2.5.0

COPY es.rb /es.rb

RUN gem install sinatra
RUN gem install thin 

EXPOSE 9200

CMD ["ruby", "es.rb"]
