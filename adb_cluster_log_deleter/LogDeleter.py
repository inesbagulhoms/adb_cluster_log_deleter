class LogDeleter:

    def __init__(self,cluster_path):

        ''' Generic Guesser class to create a 'diviner' of numbers based on simple arithmetic calculations

        Attributes:

            cluster_path represents the DBFS path where the cluster logs are saved (e.g. "/cluster-logs-script/0928-211731-34160a28") 
        '''

        self.spark_api_cluster_path = "dbfs:" + cluster_path
        self.file_api_cluster_path = "/dbfs" + cluster_path

