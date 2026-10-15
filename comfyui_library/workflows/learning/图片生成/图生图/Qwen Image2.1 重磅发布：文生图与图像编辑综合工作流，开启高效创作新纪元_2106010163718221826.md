---
key: 图片生成/图生图/Qwen Image2.1 重磅发布：文生图与图像编辑综合工作流，开启高效创作新纪元_2106010163718221826.json
name: Qwen Image2.1 重磅发布：文生图与图像编辑综合工作流，开启高效创作新纪元_2106010163718221826
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image2.1 重磅发布：文生图与图像编辑综合工作流，开启高效创作新纪元_2106010163718221826.json
hash: 2341a71068b86e32
coverage: 0.733333
learned_at: 2026-10-15 22:25:19
nodes: [VAELoader, Anything Everywhere, Text Multiline, CLIPLoader, UNETLoader, QwenImage21Cache, MarkdownNote, GetNode, VAEDecode, SetNode, 忽略多组孤海, 孤海注释, KSampler, AnySwitch, EmptyLatentImage, ImageScaleToTotalPixels, VAEEncode, 孤海注释, 孤海注释, 忽略多组孤海, TextEncodeQwenImage21, LoadImage, LoadImage, SaveImage, LoadImage, ResolutionSelector, Image Comparer (rgthree), LoadImage, Text Multiline, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1059976043427543, "steps": 30, "width": 1024}
---

# 图片生成/图生图/Qwen Image2.1 重磅发布：文生图与图像编辑综合工作流，开启高效创作新纪元_2106010163718221826.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image2.1 重磅发布：文生图与图像编辑综合工作流，开启高效创作新纪元_2106010163718221826.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `VAELoader`
- `Anything Everywhere`
- `Text Multiline`
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `MarkdownNote`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `忽略多组孤海`
- `孤海注释`
- `KSampler` ★核心
- `AnySwitch`
- `EmptyLatentImage` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `孤海注释`
- `孤海注释`
- `忽略多组孤海`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `ResolutionSelector`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Text Multiline`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1059976043427543`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（22/30）

**有卡**：`VAELoader`、`Text Multiline`、`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`VAEDecode`、`忽略多组孤海`、`KSampler`、`AnySwitch`、`EmptyLatentImage`、`ImageScaleToTotalPixels`、`VAEEncode`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
