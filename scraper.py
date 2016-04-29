import boto3
import requests
import json
import pprint

client = boto3.client('dynamodb')
pp = pprint.PrettyPrinter(indent = 2)

# req = requests.get('', auth = ('user', 'pass'))


dynamodb = boto3.resource('dynamodb', region_name='us-west-1', endpoint_url="https://dynamodb.us-west-1.amazonaws.com")

url = 'https://api.stocktwits.com/api/2/streams/symbol/AAPL.json'

# params = dict(
#     origin='Chicago,IL',
#     destination='Los+Angeles,CA',
#     waypoints='Joplin,MO|Oklahoma+City,OK',
#     sensor='false'
# )

resp = requests.get(url=url)#, params=params)
data = json.loads(resp.text)

pp.pprint(data)

# table = dynamodb.Table('ticker')

# response = client.create_table(
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'ticker',
#             'AttributeType': 'S'
#         },
# 		{
#             'AttributeName': 'tweet',
#             'AttributeType': 'S'
#         },
#     ],
#     TableName='tweets',
#     KeySchema=[
#         {
#             'AttributeName': 'ticker',
#             'KeyType': 'HASH'
#         },
# 		{
#             'AttributeName': 'tweet',
#             'KeyType': 'RANGE'
#         },
#     ],
# 	ProvisionedThroughput={
#         'ReadCapacityUnits': 400,
#         'WriteCapacityUnits': 400
#     }
# )
# print(response)
# tablelist = client.list_tables(
# 	ExclusiveStartTableName = 'tweets'
# )
# print(tablelist)
# response = client.put_item(
# 	TableName = 'tweets',
# 	Item = {
# 		"ticker" : {
# 			"S" : "TWTR",
# 		},
# 		"tweet" : {
# 			"S" : "ebola"
# 		}
# 		# "FB" : {
# 		# 	"S" : "blah1234"
# 		# }
# 	}
# )
# print(response)
