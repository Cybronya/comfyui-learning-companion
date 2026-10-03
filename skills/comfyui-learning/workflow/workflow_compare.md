# Workflow Comparison Rules


Version:

0.3.1



# Purpose


用于比较两个或者多个 ComfyUI Workflow。


目标：

发现：

- 相同结构
- 技术差异
- 优化方向
- 新增知识



---

# Comparison Principle


不要只比较 Node 数量。


重点比较：

```
Pipeline

    ↓

Model

    ↓

Node Group

    ↓

Parameters

    ↓

Purpose
```



---

# Comparison Steps


## Step 1

比较 Workflow 类型


例如：


A:

Wan I2V


B:

Wan I2V



如果类型不同：

说明主要区别。



---

# Step 2

比较 Pipeline


例如：


Workflow A:

```
Image

    ↓

Wan Model

    ↓

Sampler

    ↓

Video
```


Workflow B:

```
Image

    ↓

Wan Model

    ↓

ControlNet

    ↓

Sampler

    ↓

Video
```


分析：


B 增加：

Control Layer



---

# Step 3

比较 Node


分类：


## Common Nodes


两个 Workflow 都存在。



## Added Nodes


新增 Node。



## Removed Nodes


删除 Node。



---

# Step 4

比较 Model


分析：


- Model 是否相同
- Model 家族是否相同
- 是否替换模型



---

# Step 5

比较 Parameters


包括：


- Steps
- CFG
- Sampler
- Resolution
- Denoise



---

# Step 6

总结技术区别


输出：


## Similarity


相似程度。


例如：

80%


---

## Difference


主要区别。


---

## Learning Conclusion


告诉用户：


这个比较可以学习什么。



---

# 输出模板



Workflow A:

Workflow B:

Common Structure:

Main Differences:

Technical Changes:

Learning Value:

New Pattern Candidate:
