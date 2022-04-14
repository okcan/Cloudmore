python test.py > sample.txt
cat sample.txt | curl --data-binary @- http://192.168.100.10:9091/metrics/job/weather/instance/192.168.100.10
