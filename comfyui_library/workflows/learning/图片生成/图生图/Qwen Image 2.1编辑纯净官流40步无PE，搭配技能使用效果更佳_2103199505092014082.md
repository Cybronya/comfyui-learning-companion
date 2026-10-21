---
key: 图片生成/图生图/Qwen Image 2.1编辑纯净官流40步无PE，搭配技能使用效果更佳_2103199505092014082.json
name: Qwen Image 2.1编辑纯净官流40步无PE，搭配技能使用效果更佳_2103199505092014082
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1编辑纯净官流40步无PE，搭配技能使用效果更佳_2103199505092014082.json
hash: ebf6955ab7421bad
coverage: 0.865385
learned_at: 2026-10-21 00:42:44
nodes: [PixaromaRunTimer, ComfySwitchNode, UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, Fast Bypasser (rgthree), Image Comparer (rgthree), KSampler, LoadImage, LoadImage, LoadImage, LoadImage, PixaromaSeed, EmptyLatentImage, TextEncodeQwenImage21, PrimitiveBoolean, VAEDecode, SaveImage, LoadImage, ResolutionSelector, LoadImage, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1编辑纯净官流40步无PE，搭配技能使用效果更佳_2103199505092014082.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1编辑纯净官流40步无PE，搭配技能使用效果更佳_2103199505092014082.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（52 个）：
- `PixaromaRunTimer`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `Fast Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PixaromaSeed`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `PrimitiveBoolean`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `PrimitiveStringMultiline`
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

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（45/52）

**有卡**：`PixaromaRunTimer`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`Fast Bypasser (rgthree)`、`KSampler`、`LoadImage`、`PixaromaSeed`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`PrimitiveBoolean`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
