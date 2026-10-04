# VAEDecode

## 节点类型

`VAEDecode`

## 分类

Latent / Image Conversion

## 作用

`VAEDecode` 负责把 Latent 空间的数据解码成真正的图片。

Stable Diffusion 的生成过程发生在 Latent 空间，KSampler 输出的不是图片本身，而是一种压缩的数学表示。

必须经过 `VAEDecode`，才能变成可以查看和保存的 IMAGE。

---

## 在 Workflow 中的位置

典型流程：

```
KSampler

        ↓
     LATENT

VAEDecode

        ↓
      IMAGE

SaveImage
```

它是生成链路的"最后一公里"。

---

## 输入

### samples

来自：

```
KSampler
```

类型是 LATENT。

包含采样完成后、尚未变成图片的图像信息。

---

### vae

来自：

```
CheckpointLoaderSimple
```

负责 Latent 和 Image 之间转换的解码器。

---

## 输出

### IMAGE

提供给：

```
SaveImage
```

可以直接保存为 PNG 文件。

---

## 初学者理解

可以把 VAE 理解为：

> 一台翻译机器的"出口"。

进入时：

```
模型眼中的抽象概念（Latent）
```

出来时：

```
人类能看懂的图片（Image）
```

与之相反的是 VAEEncode，负责把图片"送进去"（图生图会用到）。

---

## 常见错误

### VAE 来源不对

表现：

* 图片颜色异常（发灰、偏绿）
* 画面模糊

原因：

* 用了不匹配的 VAE
* Checkpoint 自带 VAE 与外部 VAE 混用

---

## 学习任务

1. 观察 Latent 直接输出的效果（绕过 VAEDecode 是不行的，理解为什么必须解码）
2. 更换不同 VAE
3. 比较解码结果的差异

学习目标：

理解 Latent 与 Image 之间的转换关系。
