---
key: 平台全量/去除字幕水印｜bernini-1.3B视频一键处理_2093752910789300226.json
name: 去除字幕水印｜bernini-1.3B视频一键处理_2093752910789300226
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/去除字幕水印｜bernini-1.3B视频一键处理_2093752910789300226.json
hash: b7638bb931e14aed
coverage: 0.71831
learned_at: 2026-11-14 01:50:18
nodes: [SetNode, SetNode, ImageFromBatch, BatchCount+, RepeatImageBatch, BatchImagesNode, SetNode, SetNode, ImageFromBatch, BatchCount+, GetNode, GetNode, SetNode, GetNode, KSamplerAdvanced, easy showAnything, easy showAnything, GetNode, BatchCount+, SimpleMath+, SetNode, VAEDecode, INTConstant, INTConstant, SetNode, ImageResizeKJv2, easy showAnything, easy showAnything, GetNode, SimpleMath+, BerniniConditioning, VHS_LoadVideo, VHS_VideoCombine, Seed (rgthree), UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, VAELoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, WanContextWindowsManual, ModelPreviewOverrideKJ, VHS_VideoInfoLoaded, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/去除字幕水印｜bernini-1.3B视频一键处理_2093752910789300226.json

> 来源文件 `comfyui_library/workflows/平台全量/去除字幕水印｜bernini-1.3B视频一键处理_2093752910789300226.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `SetNode`
- `SetNode`
- `ImageFromBatch`
- `BatchCount+`
- `RepeatImageBatch`
- `BatchImagesNode`
- `SetNode`
- `SetNode`
- `ImageFromBatch`
- `BatchCount+`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `BatchCount+`
- `SimpleMath+`
- `SetNode`
- `VAEDecode` ★核心
- `INTConstant`
- `INTConstant`
- `SetNode`
- `ImageResizeKJv2`
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `SimpleMath+`
- `BerniniConditioning`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanContextWindowsManual`
- `ModelPreviewOverrideKJ`
- `VHS_VideoInfoLoaded`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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

覆盖率 **72%**（51/71）

**有卡**：`ImageFromBatch`、`BatchCount+`、`RepeatImageBatch`、`BatchImagesNode`、`KSamplerAdvanced`、`SimpleMath+`、`VAEDecode`、`INTConstant`、`ImageResizeKJv2`、`BerniniConditioning`、`VHS_LoadVideo`、`VHS_VideoCombine`、`Seed (rgthree)`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`WanContextWindowsManual`、`ModelPreviewOverrideKJ`、`VHS_VideoInfoLoaded`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
