import traceback
import sys
from operations import TopOperation
from operations import JoinOperation
from operations import AggregationOperation
from operations import FormulaOperation
from operations import FilterOperation
from connectors import DBFSConnector
from connectors import CosmosDBConnector
from datatransformations import TranformationsMainFlow
from automl import tpot_execution
from core import PipelineNotification
import json

try: 
	PipelineNotification.PipelineNotification().started_notification('5e1c162b5b457a9e66200985','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
	PredictChurn_DBFSS = DBFSConnector.DBFSConnector.fetch([], {}, "5e1c162b5b457a9e66200985", spark, "{'url': '/Demo/PredictiveChurnTrain.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapi743e2d3cc92a32916f8c2fa9bd7d0606', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

	PipelineNotification.PipelineNotification().completed_notification('5e1c162b5b457a9e66200985','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e1c162b5b457a9e66200985','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify','http://104.40.91.74:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e1c162b5b457a9e66200986','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
	PredictChurn_AutoFE = TranformationsMainFlow.TramformationMain.run(["5e1c162b5b457a9e66200985"],{"5e1c162b5b457a9e66200985": PredictChurn_DBFSS}, "5e1c162b5b457a9e66200986", spark,json.dumps( {"FE": [{"transformationsData": {"feature_label": "State"}, "feature": "State", "transformation": "String Indexer", "type": "string", "selected": "True", "stats": {"count": "333", "mean": "", "stddev": "", "min": "AK", "max": "WY", "missing": "0", "distinct": "51"}}, {"feature": "Account_Length", "transformation": "", "type": "numeric", "selected": "True", "stats": {"count": "333", "mean": "101.22", "stddev": "41.85", "min": "2", "max": "243", "missing": "0"}}, {"feature": "Area_Code", "transformation": "", "type": "numeric", "selected": "True", "stats": {"count": "333", "mean": "434.96", "stddev": "40.97", "min": "408", "max": "510", "missing": "0"}}, {"transformationsData": {"feature_label": "Phone"}, "feature": "Phone", "transformation": "String Indexer", "type": "string", "selected": "True", "stats": {"count": "333", "mean": "", "stddev": "", "min": "327-5817", "max": "422-6685", "missing": "0", "distinct": "333"}}, {"transformationsData": {"feature_label": "Intl_Plan"}, "feature": "Intl_Plan", "transformation": "String Indexer", "type": "string", "selected": "True", "stats": {"count": "333", "mean": "", "stddev": "", "min": "no", "max": "yes", "missing": "0", "distinct": "2"}}, {"transformationsData": {"feature_label": "VMail_Plan"}, "feature": "VMail_Plan", "transformation": "String Indexer", "type": "string", "selected": "True", "stats": {"count": "333", "mean": "", "stddev": "", "min": "no", "max": "yes", "missing": "0", "distinct": "2"}}, {"feature": "VMail_Message", "transformation": "", "type": "numeric", "selected": "True", "stats": {"count": "333", "mean": "8.35", "stddev": "13.73", "min": "0", "max": "45", "missing": "0"}}, {"feature": "Day_Mins", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "333", "mean": "181.67", "stddev": "55.52", "min": "29.9", "max": "350.8", "missing": "0"}}, {"feature": "Day_Calls", "transformation": "", "type": "numeric", "selected": "True", "stats": {"count": "333", "mean": "99.67", "stddev": "19.88", "min": "35", "max": "151", "missing": "0"}}, {"feature": "Day_Charge", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "333", "mean": "30.88", "stddev": "9.44", "min": "5.08", "max": "59.64", "missing": "0"}}, {"feature": "Eve_Mins", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "333", "mean": "196.73", "stddev": "49.82", "min": "42.5", "max": "350.9", "missing": "0"}}, {"feature": "Eve_Calls", "transformation": "", "type": "numeric", "selected": "True", "stats": {"count": "333", "mean": "100.05", "stddev": "19.67", "min": "49", "max": "152", "missing": "0"}}, {"feature": "Eve_Charge", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "333", "mean": "16.72", "stddev": "4.23", "min": "3.61", "max": "29.83", "missing": "0"}}, {"feature": "Night_Mins", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "333", "mean": "202.38", "stddev": "52.22", "min": "67.7", "max": "377.5", "missing": "0"}}, {"feature": "Night_Calls", "transformation": "", "type": "numeric", "selected": "True", "stats": {"count": "333", "mean": "99.19", "stddev": "20.49", "min": "38", "max": "157", "missing": "0"}}, {"feature": "Night_Charge", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "333", "mean": "9.11", "stddev": "2.35", "min": "3.05", "max": "16.99", "missing": "0"}}, {"feature": "Intl_Mins", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "333", "mean": "10.26", "stddev": "2.85", "min": "0.0", "max": "18.4", "missing": "0"}}, {"feature": "total_Mins", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "333", "mean": "591.03", "stddev": "92.69", "min": "319.9", "max": "831.3", "missing": "0"}}, {"feature": "Intl_Calls", "transformation": "", "type": "numeric", "selected": "True", "stats": {"count": "333", "mean": "4.31", "stddev": "2.32", "min": "0", "max": "13", "missing": "0"}}, {"feature": "Intl_Charge", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "333", "mean": "2.77", "stddev": "0.77", "min": "0.0", "max": "4.97", "missing": "0"}}, {"feature": "Total_Charge", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "333", "mean": "59.48", "stddev": "10.87", "min": "27.02", "max": "92.2", "missing": "0"}}, {"feature": "CustServ_Calls", "transformation": "", "type": "numeric", "selected": "True", "stats": {"count": "333", "mean": "1.55", "stddev": "1.32", "min": "0", "max": "9", "missing": "0"}}, {"feature": "Churn", "transformation": "", "type": "numeric", "selected": "True", "stats": {"count": "333", "mean": "0.13", "stddev": "0.33", "min": "0", "max": "1", "missing": "0"}}, {"transformationsData": {"feature_label": "cluster_labels"}, "feature": "cluster_labels", "transformation": "String Indexer", "type": "string", "selected": "True", "stats": {"count": "333", "mean": "", "stddev": "", "min": "day_callers", "max": "vmailers", "missing": "0", "distinct": "6"}}, {"feature": "State_transform", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "333", "mean": "20.32", "stddev": "14.04", "min": "0.0", "max": "50.0", "missing": "0"}}, {"feature": "Phone_transform", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "333", "mean": "166.0", "stddev": "96.27", "min": "0.0", "max": "332.0", "missing": "0"}}, {"feature": "Intl_Plan_transform", "transformation": "", "type": "numeric", "selected": "True", "stats": {"count": "333", "mean": "0.07", "stddev": "0.26", "min": "0", "max": "1", "missing": "0"}}, {"feature": "VMail_Plan_transform", "transformation": "", "type": "numeric", "selected": "True", "stats": {"count": "333", "mean": "0.29", "stddev": "0.45", "min": "0", "max": "1", "missing": "0"}}, {"feature": "cluster_labels_transform", "transformation": "", "type": "real", "selected": "True", "stats": {"count": "333", "mean": "2.34", "stddev": "1.69", "min": "0.0", "max": "5.0", "missing": "0"}}]}))

	PipelineNotification.PipelineNotification().completed_notification('5e1c162b5b457a9e66200986','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e1c162b5b457a9e66200986','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify','http://104.40.91.74:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e1c162b5b457a9e66200987','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
	PredictChurn_AutoML = tpot_execution.Tpot_execution.run(["5e1c162b5b457a9e66200986"],{"5e1c162b5b457a9e66200986": PredictChurn_AutoFE}, "5e1c162b5b457a9e66200987", spark,json.dumps( {"model_type": "classification", "label": "Churn", "features": ["State", "Account_Length", "Area_Code", "Phone", "Intl_Plan", "VMail_Plan", "VMail_Message", "Day_Mins", "Day_Calls", "Day_Charge", "Eve_Mins", "Eve_Calls", "Eve_Charge", "Night_Mins", "Night_Calls", "Night_Charge", "Intl_Mins", "total_Mins", "Intl_Calls", "Intl_Charge", "Total_Charge", "CustServ_Calls", "cluster_labels"], "percentage": "40", "executionTime": 10, "sampling": "1", "sampling_value": "over", "model_id": "5e1c24021bfdaec91f39a6b3", "run_id": "", "ProjectName": "Retail Scenarios", "PipelineName": "PredictChurn", "userid": "567a95c8ca676c1d07d5e3e7", "runid": "", "url_ResultView": "http://104.40.91.74:3200", "experiment_id": "895518857185768"}))

	PipelineNotification.PipelineNotification().completed_notification('5e1c162b5b457a9e66200987','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e1c162b5b457a9e66200987','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify','http://104.40.91.74:3200/logs/getProductLogs')
	sys.exit(1)

