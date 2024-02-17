# Datagrok-test

## App1
App1 is on default route of localhost on port 80.
Inside container it has port `5000`, external port is `5001`.

## App2 
App2 is on localhost/app2 route on port 80.
Inside container it has port `5000`, external port is `5002`.

## Functionality
Apps are collecting metrics such as: cpu, memory, disk usage, network usage and outputting them in json format.
Also apps have health-check endpoints, you can find it on route `http://localhost/health-check:5001` for app1 or `http://localhost/health-check:5002`.
