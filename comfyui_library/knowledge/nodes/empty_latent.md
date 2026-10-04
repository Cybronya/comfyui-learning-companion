# EmptyLatentImage

## 节点类型

`EmptyLatentImage`

## 分类

Latent Creation

## 作用

`EmptyLatentImage` 负责创建一张"空白画布"。

文生图（txt2img）从零开始生成图片，所以需要一个初始 Latent 作为起点。

KSampler 会在这张空白画布上，一步步把噪声转换成图像。

---

## 在 Workflow 中的位置

典型流程：

```
EmptyLatentImage

        ↓
      LATENT

KSampler

        ↓

VAEDecode

        ↓
      IMAGE
```

---

## 输入

### width

图片宽度。

例如：

```
512
```

SD1.5 常用 512 系分辨率（最高 768 系）。

---

### height

图片高度。

例如：

```
512
```

---

### batch_size

一次生成几张图。

例如：

```
1
```

数值越大，显存占用越高。

---

## 输出

### LATENT

提供给：

```
KSampler
```

作为初始 Latent。

---

## 初学者理解

可以把 EmptyLatentImage 理解为：

> 一张决定尺寸的空白画布。

画布多大，最终图片就多大。

例如：

* 512×512 → 正方形
* 512×768 → 竖版
* 768×512 → 横版

---

## 常见错误

### 分辨率过大

例如：

SD1.5 workflow 使用 1024×1024。

可能导致：

* 构图崩坏（多人、重复肢体）
* 内容异常

SD1.5 应使用 512 系分辨率，SDXL 才适合 1024 系。

### 分辨率不是 8 的倍数

可能导致：

* 报错
* 生成失败

---

## 学习任务

1. 保持 Prompt 不变
2. 分别生成 512×512 和 768×512
3. 比较构图差异

学习目标：

理解分辨率对生成结果的影响。
