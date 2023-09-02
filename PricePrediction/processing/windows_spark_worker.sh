
SPARK_HOME="D:/spark/spark-3.4.1-bin-hadoop3"

MASTER_BIN_PATH="$SPARK_HOME/bin/spark-class org.apache.spark.deploy.worker.Worker"
HOST="spark://127.0.0.1:7078 --host 127.0.0.1"

COMMAND="$MASTER_BIN_PATH  $HOST"
echo $COMMAND
cmd.exe /c $COMMAND