---
key: 视频生成/图生视频/qwen_image2.1多图编辑进阶版｜文生图图生图自由切换｜批量改图高效_2104446242880315393.json
name: qwen_image2.1多图编辑进阶版｜文生图图生图自由切换｜批量改图高效_2104446242880315393
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/qwen_image2.1多图编辑进阶版｜文生图图生图自由切换｜批量改图高效_2104446242880315393.json
hash: 98eb58e412c15380
coverage: 0.942029
learned_at: 2026-10-17 22:19:17
nodes: [UNETLoader, LoadImage, LoadImage, LoadImage, KSampler, CLIPLoader, VAELoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPLoader, TextEncodeQwenImage21, VAEDecode, EmptyLatentImage, QwenImage21Cache, TextGenerateLTX2Prompt, easy showAnything, JDCN_StringToList, CR Text, BatchImagesNode, LoadImage, SaveImageAdvanced, SaveImage, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/qwen_image2.1多图编辑进阶版｜文生图图生图自由切换｜批量改图高效_2104446242880315393.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/qwen_image2.1多图编辑进阶版｜文生图图生图自由切换｜批量改图高效_2104446242880315393.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `JDCN_StringToList`
- `CR Text`
- `BatchImagesNode`
- `LoadImage`
- `SaveImageAdvanced`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **94%**（65/69）

**有卡**：`UNETLoader`、`LoadImage`、`KSampler`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`VAEDecode`、`EmptyLatentImage`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`JDCN_StringToList`、`CR Text`、`BatchImagesNode`、`SaveImageAdvanced`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
