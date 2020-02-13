import json
from datetime import datetime,date

data = dict()
data['name'] = 'robin'
data['time'] = datetime(2005, 7, 14, 12, 30)
print(data)

# class ComplexEncoder(json.JSONEncoder):
# 	def default(self, obj):
# 		if isinstance(obj, complex):
# 			return [obj.real, obj.imag]
# 			# Let the base class default method raise the TypeError
# 		return json.JSONEncoder.default(self, obj)

class DateTimeEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, datetime):
			return obj.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(obj, date):
			return obj.strftime('%Y-%m-%d')
		# Let the base class default method raise the TypeError
		return json.JSONEncoder.default(self, obj)

print(json.dumps(data, cls=DateTimeEncoder))