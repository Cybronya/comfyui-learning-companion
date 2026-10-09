---
key: 图片生成/图生图/Qwen Image 2.1多图编辑文生图图生图处理工具_2102505314745667586.json
name: Qwen Image 2.1多图编辑文生图图生图处理工具_2102505314745667586.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多图编辑文生图图生图处理工具_2102505314745667586.json
hash: 90b27e65890c5fa9
coverage: 0.890909
learned_at: 2026-10-09 22:19:28
nodes: [UNETLoader, LoadImage, LoadImage, LoadImage, KSampler, CLIPLoader, VAELoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPLoader, TextEncodeQwenImage21, VAEDecode, EmptyLatentImage, QwenImage21Cache, TextGenerateLTX2Prompt, easy showAnything, JDCN_StringToList, CR Text, BatchImagesNode, LoadImage, SaveImageAdvanced, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1多图编辑文生图图生图处理工具_2102505314745667586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102505314745667586.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
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

覆盖率 **89%**（49/55）

**有卡**：`UNETLoader`、`LoadImage`、`KSampler`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`VAEDecode`、`EmptyLatentImage`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`JDCN_StringToList`、`BatchImagesNode`、`SaveImageAdvanced`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（1）：`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
