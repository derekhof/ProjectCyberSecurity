# Used for sending and receiving HTTP data
import requests,json
from time import gmtime, strftime

# Define JSON content type so the server understands us. Also add the server side generated key for authentication.
headers = {'content-type': 'application/json', 'Authorization': 'ApiKey root:dac380125620a500f5a32fb2941e94f820693c63'}

# This is the URL to which we're going to send the HTTP POST
url = 'http://192.168.241.128:8000/api/v1/findings/'

class finding:

    def __init__(self,id,product,engagement,test,reporter):
        try:
                self.id = id
                self.product = product
                self.engagement = engagement
                self.test = test
                self.reporter = reporter
                self.title = "Grappy Finding"
                self.severity = "Low"
                self.date = strftime("%Y-%m-%d", gmtime())
                self.description = "Grappy scan resulted in findings"
                self.impact = "Information disclosure"
                self.created = strftime("%Y-%m-%d %H:%M", gmtime())
                self.mitigation = "remove comments from your productioncode"
                self.under_review = "False"
                self.mitigated = strftime("%Y-%m-%d %H:%M", gmtime())
                self.last_reviewed = strftime("%Y-%m-%d %H:%M", gmtime())
                self.status = "SUCCEED"
        except:

            self.status = "FAILED"

# Translate Python findings into JSON format
data = json.dumps(finding)

# Execute code HTTP post. "Verify" is set false because the SSL certificate is self signed.
r = requests.post(url, headers=headers, data=data, verify=False)







# # Declare finding variables in Python
# finding = {"id": 2,  # Mandatory, this is the Primary Key ID for the Finding. Must increment with each finding
#            "product": "/api/v1/products/1/",  # Mandatory, this is the product to which the finding is connected
#            "engagement": "/api/v1/engagements/4/",  # Mandatory, this is the engagment to which the finding is connected
#            "test": "/api/v1/tests/2/",  # Mandatory, this is the test to which the finding is connected
#            "reporter": "/api/v1/users/1/", # Mandatory, this is the user to which the finding is connected
#            "title": "This is the name/title in the GUI",  # Mandatory, title of the finding
#            "severity": "Medium",  # Mandatory, variable: info, low, medium, high or critical
#            "date": "2019-01-01", # Mandatory
#            "description": "-",  # Mandatory, finding description text
#            "impact": "Unknown",  # Mandatory, impact text
#            "created": "2019-01-01 12:00", # Mandatory
#            "mitigation": "Unknown", # Mandatory, mitigation text
#            "under_review": "False",  # Mandatory, true or false
#            "mitigated": "2019-01-01 12:00",  # Mandatory
#            "last_reviewed": "2019-01-01 12:00",  # Mandatory
#            "active": "True",  # True or false
#            "severity_justification": "",
#            "line_number": "",
#            "steps_to_reproduce": "",
#            "sourcefile": "",
#            "static_finding": "", # True or false
#            "thread_id": 0,
#            "references": "",
#            "dynamic_finding": "", # True or false
#            "scanner_confidence": 0,
#            "line": 0,
#            "payload": "",
#            "under_defect_review": "", # True or false
#            "hash_code": "",
#            "false_p": "", # True or false
#            "verified": "",
#            "is_template": "", # True or false
#            "url": "",
#            "duplicate": "", # True or false
#            "param": "",
#            "sourcefilepath": "",
#            "numerical_severity": "",
#            "out_of_scope": "",
#            "cwe": 0,
#            "file_path": "",
#            "resource_uri": ""}

