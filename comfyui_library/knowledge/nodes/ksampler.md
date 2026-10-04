# KSampler

## 节点类型

`KSampler`

## 分类

Diffusion Sampling

## 作用

`KSampler` 是 Stable Diffusion workflow 中最核心的生成节点。

它负责：

> 将随机噪声逐渐转换成符合 Prompt 的图像内容。

---

## Workflow 位置

```
MODEL
  |
  v

KSampler

  |
  v

LATENT

  |
  v

VAEDecode

  |
  v

IMAGE
```

---

## 输入

### model

来自：

```
CheckpointLoaderSimple
```

---

### positive

来自：

```
CLIPTextEncode
```

Positive Prompt。

---

### negative

Negative Prompt。

---

### latent_image

初始 Latent。

来自：

```
EmptyLatentImage
```

---

## 核心参数

## steps

采样次数。

例如：

```
20
```

代表模型进行 20 次去噪过程。

影响：

增加：

* 更多细节
* 更稳定

缺点：

* 更慢

---

## cfg

Prompt 控制强度。

例如：

```
7
```

数值越高：

* 更遵循 Prompt

过高：

* 图片可能僵硬
* 细节异常

---

## sampler_name

采样算法。

例如：

```
Euler
DPM++ 2M
```

不同算法会影响：

* 速度
* 细节
* 风格

---

## 初学者理解

KSampler 就像：

> 一个画家不断修改草稿，直到完成作品。

开始：

```
随机噪声
```

经过：

```
step 1
step 2
step 3
...
```

最后：

```
清晰图片
```

---

## 常见错误

### steps 太低

结果：

* 模糊
* 细节不足

### cfg 太高

结果：

* 颜色异常
* 画面僵硬

### sampler 不适合

结果：

* 质量下降

---

## 学习任务

实验：

固定：

```
Prompt
Checkpoint
Seed
```

修改：

```
steps:

20

↓

40
```

观察：

* 细节变化
* 生成速度变化

目标：

理解采样过程。
