## Debug connection
```
kubectl run curlpod --image=radial/busyboxplus:curl -i --tty --rm
curl http://<service-name>.<namespace>.svc.cluster.local:<port>
```
