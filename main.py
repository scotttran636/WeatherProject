# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2

class CustomPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<a href="http://google.com/">Google</a>')

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class DogPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('Woof Woof Woof')

class ManyDogPage(webapp2.RequestHandler):
	def get(self, number):
		self.response.headers['Content-Type'] = 'text/plain'
		l = ['{}:Woof Woof Woof\n'.format(i) for i in range(int(number))]
		l = []
		for i in range(int(number)):
			l.append('{}: Woof Woof Woof\n'.format(i))
		s = '\n'.join(l)
		self.response.write(s)

class SomeTextPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		s = open('sometext.txt').read( )
		self.response.write(s)

app = webapp2.WSGIApplication([
    ('/', MainPage),
	('/cs254', CustomPage),
	('/dog', DogPage),
	('/dog/(\d+)', ManyDogPage),
	('/txt', SomeTextPage),
], debug=True)
