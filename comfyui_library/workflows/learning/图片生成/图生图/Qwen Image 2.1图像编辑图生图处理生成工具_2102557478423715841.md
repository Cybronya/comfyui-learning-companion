---
key: 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102557478423715841.json
name: Qwen Image 2.1图像编辑图生图处理生成工具_2102557478423715841.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102557478423715841.json
hash: ec2e9549b971e002
coverage: 0.661972
learned_at: 2026-10-09 22:19:29
nodes: [CLIPLoader, VAELoader, EmptyLatentImage, QwenImage21Cache, SetNode, SetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, LoadImage, SetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, TextEncodeQwenImage21, PreviewImage, GetNode, VAEDecode, SaveImage, GH_ImageVideoComparer, UNETLoader, KSampler, FastGroupsBypassSwitch, ResolutionSelector, FastGroupsBypassSwitch, LoadImage, Fast Groups Bypasser (rgthree), QwenPERewriteT8, JjkText, easy showAnything, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102557478423715841.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102557478423715841.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（71 个）：
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `GetNode`
- `VAEDecode` ★核心
- `SaveImage`
- `GH_ImageVideoComparer`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `FastGroupsBypassSwitch`
- `ResolutionSelector`
- `FastGroupsBypassSwitch`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `QwenPERewriteT8`
- `JjkText`
- `easy showAnything`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **66%**（47/71）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`LoadImage`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`GH_ImageVideoComparer`、`UNETLoader`、`KSampler`、`FastGroupsBypassSwitch`、`ResolutionSelector`、`QwenPERewriteT8`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
