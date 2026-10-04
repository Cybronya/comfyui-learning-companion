# CheckpointLoaderSimple

## 节点类型

`CheckpointLoaderSimple`

## 分类

Model Loading

## 作用

`CheckpointLoaderSimple` 负责加载 Stable Diffusion 模型。

它是整个生成流程的起点。

一个 Stable Diffusion workflow 首先需要加载一个基础模型（Checkpoint），后续节点才能使用它进行图片生成。

---

## 在 Workflow 中的位置

典型流程：

```
CheckpointLoaderSimple

        ↓

CLIPTextEncode

        ↓

KSampler

        ↓

VAEDecode

        ↓

SaveImage
```

---

## 输入

### ckpt_name

选择需要加载的模型文件。

例如：

```
sd15_base_model.safetensors
```

不同 Checkpoint 会影响：

* 画风
* 人物特征
* 光影效果
* 生成质量

---

## 输出

### MODEL

提供给 `KSampler` 使用。

负责图片生成过程中的扩散模型计算。

### CLIP

提供给 `CLIPTextEncode`。

负责理解文字 Prompt。

### VAE

提供给 `VAEDecode`。

负责 Latent 和 Image 之间转换。

---

## 初学者理解

可以把 Checkpoint 理解为：

> 一个已经学习过绘画能力的大脑。

不同模型就像不同画家的能力。

例如：

* 写实模型 → 擅长真实照片
* Anime 模型 → 擅长动漫风格

---

## 常见错误

### 使用错误模型

表现：

* 图片风格异常
* 人物结构错误

### 模型版本不匹配

例如：

SD1.5 workflow 使用 SDXL Checkpoint。

可能导致：

* 尺寸问题
* 效果异常

---

## 学习任务

1. 更换不同 Checkpoint
2. 保持 Prompt 不变
3. 比较生成结果差异

学习目标：

理解模型对于生成结果的重要影响。
