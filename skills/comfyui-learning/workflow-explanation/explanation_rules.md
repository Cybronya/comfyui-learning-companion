# Workflow Explanation Rules


# 1. Overall Summary


首先说明：

这个 Workflow 用于什么任务


例如：

```
这是一个 Wan 视频生成 Workflow。

输入：
文本提示词

输出：
视频序列
```



---


# 2. Workflow Stage Analysis


Workflow 不直接按节点列表解释。

需要按照功能阶段划分。


例如：


## Stage 1

模型加载

```
节点：
Load Diffusion Model
Load VAE

作用：
准备生成模型。
```


---

## Stage 2

条件输入

```
节点：
CLIP Text Encode

作用：
把文字转换为模型理解的信息。
```


---

## Stage 3

生成过程

```
节点：
Sampler

作用：
逐步生成 latent。
```


---

## Stage 4

解码输出

```
节点：
VAE Decode

作用：
latent 转换为图片或视频。
```


---


# 3. Node Explanation Rules


每个重要节点解释：

格式：

```
Node:
KSampler

Purpose:
负责扩散采样。

Input:
model
conditioning
latent

Output:
new latent

Why:
控制生成过程。
```



---


# 4. Connection Explanation


重点解释：

为什么连接。


例如：

不要：

```
A 连接 B
```


应该：

```
Text Encoder 产生的 conditioning
传递给 Sampler。

Sampler 根据文本条件控制生成方向。
```



---


# 5. Model Explanation


说明：


- 模型名称
- 模型类型
- 在 Workflow 中的职责


例如：

```
Wan 模型：
负责视频生成核心扩散过程。

VAE：
负责 latent 和视频像素转换。
```



---


# 6. Parameter Explanation


重点解释：


- steps
- cfg
- sampler
- resolution
- frames


说明：

影响什么。


---


# 7. Learning Recommendation


最后提供：

建议学习顺序：

```
1. 理解整体流程
2. 学习核心节点
3. 研究参数
4. 修改测试
```
