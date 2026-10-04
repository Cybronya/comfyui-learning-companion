# Retrieval Rules


## Query Understanding


用户输入：


"低显存 Wan 视频"


解析：

```
task:
video_generation

model:
Wan

constraint:
low_vram
```



---


# Search Order


优先：


## 1 Workflow


寻找可执行方案。



## 2 Node


补充节点信息。



## 3 Model


确认资源。


---


# Result Format


返回：


Workflow:

name

Required Models:

Models

Required Nodes:

Nodes

VRAM:

Requirement

Notes:



---


# Missing Resource


如果缺少：


例如：

Workflow 需要：

Wan VAE


但是不存在


返回：


Missing:

Wan VAE

Location:

models/vae
