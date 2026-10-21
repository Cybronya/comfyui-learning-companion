---
key: 图片生成/图生图/千问image2.1图像编辑-不偏移版-自动优化提示词-可以抠图_2103044555493961729.json
name: 千问image2.1图像编辑-不偏移版-自动优化提示词-可以抠图_2103044555493961729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问image2.1图像编辑-不偏移版-自动优化提示词-可以抠图_2103044555493961729.json
hash: 03e44a58958bce04
coverage: 0.9
learned_at: 2026-10-21 00:50:39
nodes: [ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, LoadImage, LoadImage, LoadImage, Text Multiline, Seed (rgthree), XinbaoImageStandardizer, Image Comparer (rgthree), QwenPERewriteT8, SaveImageAdvanced, SaveImage, VAEDecode, 忽略多组孤海, LoadImage, TextEncodeQwenImage21, ShowText|pysssss, 忽略多组孤海, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 5526599403035, "steps": 25, "width": 1024}
---

# 图片生成/图生图/千问image2.1图像编辑-不偏移版-自动优化提示词-可以抠图_2103044555493961729.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问image2.1图像编辑-不偏移版-自动优化提示词-可以抠图_2103044555493961729.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `Seed (rgthree)`
- `XinbaoImageStandardizer`
- `Image Comparer (rgthree)`
- `QwenPERewriteT8`
- `SaveImageAdvanced`
- `SaveImage`
- `VAEDecode` ★核心
- `忽略多组孤海`
- `LoadImage`
- `TextEncodeQwenImage21`
- `ShowText|pysssss`
- `忽略多组孤海`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `5526599403035`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（27/30）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`LoadImage`、`Text Multiline`、`Seed (rgthree)`、`XinbaoImageStandardizer`、`QwenPERewriteT8`、`SaveImageAdvanced`、`SaveImage`、`VAEDecode`、`忽略多组孤海`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
