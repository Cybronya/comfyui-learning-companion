# CLIPTextEncode

## 节点类型

`CLIPTextEncode`

## 分类

Text Conditioning

## 作用

`CLIPTextEncode` 负责把文字 Prompt 转换为模型可以理解的信息。

Stable Diffusion 并不是直接读取文字，而是通过 CLIP 将文字转换成 Conditioning。

---

## Workflow 位置

```
Prompt

 ↓

CLIPTextEncode

 ↓

KSampler

 ↓

Image
```

---

## 输入

### text

用户输入的 Prompt。

例如：

```
a beautiful girl,
cinematic lighting,
high detail
```

---

### CLIP

来自：

```
CheckpointLoaderSimple
```

---

## 输出

### CONDITIONING

提供给：

```
KSampler
```

用于控制生成方向。

---

## 初学者理解

可以理解为：

> CLIPTextEncode 是翻译器。

人类语言：

```
一只猫坐在森林里
```

经过转换后：

```
模型能够理解的视觉概念
```

---

## Positive Prompt

描述希望出现的内容：

例如：

```
beautiful landscape
sunset
high quality
```

---

## Negative Prompt

描述希望避免的内容：

例如：

```
low quality
bad anatomy
blurry
```

---

## 常见错误

### Prompt 过于复杂

导致：

* 模型无法理解重点

### Negative Prompt 使用错误

可能导致：

* 图片质量下降

---

## 学习任务

实验：

保持其他参数不变：

Prompt A:

```
portrait photo
```

Prompt B:

```
anime portrait
```

观察：

CLIP 如何影响最终图片风格。
