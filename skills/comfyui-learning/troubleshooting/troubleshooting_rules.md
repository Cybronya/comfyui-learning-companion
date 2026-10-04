# Troubleshooting Rules


# 1. Error Classification


错误首先分类：


- Model
- Node
- Memory
- CUDA
- Workflow
- Dependency



---


# 2. CUDA Out Of Memory


错误：


CUDA out of memory


分析：

```
检查：
model size
resolution
batch
frames
precision
```


解释：


通常原因：

- 模型占用超过显存
- 视频帧过多
- 分辨率过高
- 多模型同时加载


---


# 3. Missing Node


错误：


Node type XXX not found


分析：

```
检查：
custom_nodes
package
installation
```


输出：

```
缺少：
XXX 节点

来源：
某 custom node 包
```



---


# 4. Missing Model


错误：


File not found

model missing


检查：


- model path
- filename
- workflow requirement



---


# 5. Tensor Shape Error


错误：


shape mismatch


可能原因：


- model incompatible
- wrong resolution
- wrong VAE
- wrong encoder



---


# 6. Device Error


错误：


Expected cuda:0 but got cuda:1


检查：


- model placement
- device map
- offload



---


# 7. Analysis Format


每次分析包含：

```
Problem

    ↓

Cause

    ↓

Evidence

    ↓

Solution Direction

    ↓

Learning Note
```


---

# 8. Learning Note


解释：

为什么会发生。


例如：


OOM 不是简单错误。

因为：

扩散模型推理过程需要：

- model
- latent
- attention
- activation

共同占用显存。
