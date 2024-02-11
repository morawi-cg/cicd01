# Monitor K8S

## connect to k8s on docker desktop</p>

```
kubectl config get-contexts
kubectl config use-context docker-desktop
```

##Prometheus</p>

##Gafana</p>

##GrafanaAgentKubernetes:</p>

### Install</p>

```

   kubectl apply -f https://raw.githubusercontent.com/grafana/agent/v0.39.0/production/kubernetes/operator/deployment.yaml

```
Check this out:</p>

```
kubectl rollout status deployment grafana-agent-operator

```

#### Grafana Python lib, dashboard builder

```
https://github.com/weaveworks/grafanalib.git
```



