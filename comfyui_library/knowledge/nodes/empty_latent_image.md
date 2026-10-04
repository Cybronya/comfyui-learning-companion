# EmptyLatentImage

## 节点类型

`EmptyLatentImage`

## 分类

Latent Generation

## 作用

`EmptyLatentImage` 用于创建 Stable Diffusion 开始生成时需要的初始 Latent。

在 Text To Image workflow 中，它负责定义：

* 图片尺寸
* Batch 数量

它提供一个"空白的潜空间画布"，让 `KSampler` 开始进行去噪生成。

---

## Workflow 位置

典型流程：

```text
CheckpointLoaderSimple

        ↓

EmptyLatentImage

        ↓

KSampler

        ↓

VAEDecode

        ↓

SaveImage
```

---

## 输入

### width

图片宽度。

例如：

```text
512
```

---

### height

图片高度。

例如：

```text
512
```

---

### batch_size

一次生成图片数量。

例如：

```text
1
```

设置为：

```text
4
```

表示一次生成 4 张图片。

---

## 输出

### LATENT

输出 Latent 数据。

提供给：

```text
KSampler
```

作为初始生成空间。

---

# 什么是 Latent？

Stable Diffusion 并不是直接在图片空间生成。

它主要工作在：

```text
Image Space

      ↓

Latent Space

      ↓

Image Space
```

Latent 是经过压缩后的图片信息表示。

---

## 初学者理解

可以把 `EmptyLatentImage` 理解为：

> 给 AI 准备一张没有内容的画布。

但是这张画布不是普通图片，而是在 Latent Space 中的画布。

---

## 为什么尺寸重要？

例如：

```text
512 × 512
```

适合：

* SD1.5 基础生成

更大：

```text
1024 × 1024
```

可能导致：

* 显存增加
* 细节问题
* 模型不适配

---

## 常见错误

### 使用错误尺寸

例如：

SD1.5：

```text
512 × 512
```

突然改：

```text
2048 × 2048
```

可能出现：

* OOM（显存不足）
* 图片结构异常

---

### 忽略模型训练尺寸

很多模型在特定尺寸下效果最好。

---

## 学习任务

实验：

保持：

```text
Checkpoint
Prompt
Seed
Steps
CFG
```

不变。

修改：

```text
512×512

↓

768×768
```

观察：

* 构图变化
* 细节变化
* 显存变化

学习目标：

理解 Latent Size 对生成结果的影响。
