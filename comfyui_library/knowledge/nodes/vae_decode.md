# VAEDecode

## 节点类型

`VAEDecode`

## 分类

Latent Conversion

## 作用

`VAEDecode` 负责把 Stable Diffusion 生成的 Latent 转换成最终图片。

它是生成流程中的最后转换步骤。

---

## Workflow 位置

```text
KSampler

     ↓

LATENT

     ↓

VAEDecode

     ↓

IMAGE

     ↓

SaveImage
```

---

## 输入

### samples

来自：

```text
KSampler
```

这是生成完成后的 Latent。

---

### vae

来自：

```text
CheckpointLoaderSimple
```

---

## 输出

### IMAGE

最终图片数据。

可以提供给：

```text
SaveImage
```

保存。

---

# VAE 是什么？

VAE 全称：

```text
Variational Auto Encoder
```

它负责：

Latent 和 Image 之间转换。

两个方向：

---

## Encode

图片：

```text
IMAGE

↓

VAEEncode

↓

LATENT
```

用于：

* Image To Image
* Control workflow

---

## Decode

Latent：

```text
LATENT

↓

VAEDecode

↓

IMAGE
```

用于：

* 查看生成结果

---

## 初学者理解

如果 Latent 是 AI 内部语言：

那么：

`VAEDecode`

就是：

> 把 AI 的内部语言翻译成人类能看到的图片。

---

## 常见错误

### VAE 不匹配

表现：

* 色彩异常
* 细节损失
* 图片偏色

---

### 忽略 VAE 质量

不同 VAE：

可能影响：

* 色彩
* 清晰度
* 对比度

---

## 学习任务

实验：

保持 workflow 不变。

替换不同 VAE。

观察：

* 颜色变化
* 细节变化

学习目标：

理解 VAE 对最终图片质量的影响。
