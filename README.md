# missao-monitoramento-elite


# Instalação no Kubernetes

https://artifacthub.io/packages/helm/prometheus-community/prometheus


## Adicionando o repositório

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

## Comando de Instalação

```
helm install prometheus prometheus-community/prometheus --set server.service.type=LoadBalancer
```