---
key: 图片生成/文生图/平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122.json
name: 平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122.json
hash: 43f0d0a7add6034b
coverage: 0.907407
learned_at: 2026-10-07 01:57:57
nodes: [VAELoader, VAEDecode, EmptyLatentImage, ResolutionSelector, UNETLoader, CLIPLoader, SaveImage, TextEncodeQwenImage21, SaveImageAdvanced, KSampler, EmptyLatentImage, VAELoader, CLIPLoader, VAEDecode, QwenImage21Cache, ResolutionSelector, SaveImage, KSampler, SaveImageAdvanced, UNETLoader, TextEncodeQwenImage21, ComfySwitchNode, LoraLoaderModelOnly, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（54 个）：
- `VAELoader`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `SaveImage`
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `KSampler` ★核心
- `SaveImageAdvanced`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
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

覆盖率 **91%**（49/54）

**有卡**：`VAELoader`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`KSampler`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`LoadImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
