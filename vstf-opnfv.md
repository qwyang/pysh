VSTF OpenNFV Guide.

== [[Informations] ==
wiki:
    https://wiki.opnfv.org/
Repositories:
    https://git.opnfv.org/cgit
CI:
    ​https://build.opnfv.org/ci/

== [[Bottleneck CI] ==
​Jenkins entry：
https://git.opnfv.org/cgit/bottlenecks/tree/ci/vstf_run.sh
https://git.opnfv.org/cgit/bottlenecks/tree/utils/infra_setup/heat_template/vstf_heat_template/vstf_HOT_create_instance.sh

== [[DashBoard work flow] ==
=== run testcase by ci and save result as files ===
=== collect data from result files and upload to mongo db ===
HowTo:
        self.target = http://213.77.62.197/results
        self.headers = {'Content-type': 'application/json'}
        self.timeout = 5
        self.result = {
            "project_name": "bottlenecks",
            "description": "bottlenecks test cases result",
             "pod_name" : "**"
             "installer" : "**"
             "version" : "**"
             "case_name" : "**"
             "details" : "**"
        }
        res = requests.post(self.target,
                        data=json.dumps(self.result),
                        headers=self.headers,
                        timeout=self.timeout)
example scripts:
    https://git.opnfv.org/cgit/bottlenecks/tree/utils/dashboard
=== retrieve data from mongo db and format the data ===
new code should add to:
    https://git.opnfv.org/cgit/releng/tree/utils/test/result_collection_api/dashboard/bottlenecks2Dashboard.py
HowTo:
    1. add test case names to get_bottlenecks_cases().
    2. add a function called format_XXX_for_dashboard(results) for each of your test case, XXX is your case name.
        def format_XXX_for_dashboard(results):
           """  
               @param results <list>:
               example:[
                    {
                        "project_name": "bottlenecks", 
                        "description": "bottlenecks test cases result", 
                        "creation_date": "2015-12-22 12:16:17.131438", 
                        "case_name": "rubbos", 
                        "version": "unknown", 
                        "details": [
                            {
                                "client": 200, 
                                "throughput": 20
                            }, 
                            {
                                "client": 300, 
                                "throughput": 50
                            }
                        ], 
                        "installer": "fuel", 
                        "_id": "56793f11514bc5068a345da4", 
                        "pod_name": "unknown-pod"
                    }, 
                    ...
                ]
               @return <dict>
               1. to draw a line, return:
               {
                    "name": "your titile"
                    "info": {"type":"graph", "xlabel": "time", "ylabel": "duration"}
                    "data_set":[{1,1},{2,2}...{x,y}]
               }
               2. to draw a bar, return:
               {
                    "name": "your titile"
                    "info": {"type":"bar"}
                    "data_set":[{"64":1.0,"128":1.0,"256":1.0,"512":1.0,"1024":1.0}]
               }
           """
Under the hood:
    results = requests.get("http://213.77.62.197/results?project=bottlenecks&case=vstf_tu")
    return format_vstf_tu_for_dashboard(results)
example scripts:
    https://git.opnfv.org/cgit/releng/tree/utils/test/result_collection_api/dashboard/yardstick2Dashboard.py

=== final results ===
https://www.opnfv.org/opnfvtestgraphs/per-test-projects
