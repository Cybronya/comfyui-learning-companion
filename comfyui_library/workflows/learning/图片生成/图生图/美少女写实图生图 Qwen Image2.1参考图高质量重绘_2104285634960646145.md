---
key: 图片生成/图生图/美少女写实图生图 Qwen Image2.1参考图高质量重绘_2104285634960646145.json
name: 美少女写实图生图 Qwen Image2.1参考图高质量重绘_2104285634960646145
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/美少女写实图生图 Qwen Image2.1参考图高质量重绘_2104285634960646145.json
hash: 17ac3969bb1e34f3
coverage: 0.866667
learned_at: 2026-10-21 00:55:46
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, ComfySwitchNode, QwenImage21Cache, SaveImageAdvanced, LoadImage, Text, VAEDecode, SaveImage, EmptyLatentImage, TextEncodeQwenImage21, ResolutionSelector, Image Comparer (rgthree), LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/美少女写实图生图 Qwen Image2.1参考图高质量重绘_2104285634960646145.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/美少女写实图生图 Qwen Image2.1参考图高质量重绘_2104285634960646145.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `SaveImageAdvanced`
- `LoadImage`
- `Text`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `Image Comparer (rgthree)`
- `LoadImage`
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

覆盖率 **87%**（39/45）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`QwenImage21Cache`、`SaveImageAdvanced`、`LoadImage`、`Text`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
