# Spark Study
1. Windows 10 spark 환경설정

   jupyter notebook으로 pyspark session을 생성할 때, 환경설정을 하지 않아 오류가 발생하는 경우가 있다. 오류 내용은 "py4j.protocol.Py4JError: org.apache.spark.api.python.PythonUtils.getEncryptionEnabled does not exist in the JVM" 이며 이에 대한 해결법은 하단과 같다.
   
   ```bash
   # 하단처럼 환경변수 설정
   SPARK_HOME	=>	{SPARK 폴더 상위 경로}/spark-x.x.x-bin-hadoopx.x
   PYTHONPATH	=>	%SPARK_HOME%/python;%SPARK_HOME%/python/lib/py4j-x.x.x-src.zip;
   PATH		=>	%SPARK_HOME%/bin;%SPARK_HOME%/python
   ```
   
   상단처럼 설정하면, jupyter notebook에서 pyspark session 생성 및 관련한 함수를 사용할 수 있는 것을 확인했다.
   
   

------

해야할 일

> 