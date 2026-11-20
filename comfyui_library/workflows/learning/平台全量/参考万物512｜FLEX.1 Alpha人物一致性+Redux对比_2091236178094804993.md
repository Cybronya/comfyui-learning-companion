---
key: 平台全量/参考万物512｜FLEX.1 Alpha人物一致性+Redux对比_2091236178094804993.json
name: 参考万物512｜FLEX.1 Alpha人物一致性+Redux对比_2091236178094804993
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/参考万物512｜FLEX.1 Alpha人物一致性+Redux对比_2091236178094804993.json
hash: 30c4cfc82534352d
coverage: 0.864407
learned_at: 2026-11-14 01:50:31
nodes: [StyleModelApply, ConditioningZeroOut, VAEDecode, SaveImage, VAEDecode, Image Comparer (rgthree), Image Comparer (rgthree), SaveImage, SaveImage, AddLabel, AddLabel, AddLabel, ImageConcatMulti, PrimitiveNode, PrimitiveNode, VAEEncode, CLIPTextEncode, ImageResizeKJ, CLIPVisionEncode, StyleModelApply, CLIPVisionEncode, CLIPTextEncode, ConditioningZeroOut, KSampler, KSampler, LoadImage, CheckpointLoaderSimple, CLIPVisionLoader, StyleModelLoader, CheckpointLoaderSimple, CLIPVisionLoader, StyleModelLoader, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "Flex.1-alpha.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/参考万物512｜FLEX.1 Alpha人物一致性+Redux对比_2091236178094804993.json

> 来源文件 `comfyui_library/workflows/平台全量/参考万物512｜FLEX.1 Alpha人物一致性+Redux对比_2091236178094804993.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `StyleModelApply`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `CLIPVisionEncode`
- `StyleModelApply`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `KSampler` ★核心
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPVisionLoader`
- `StyleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `CLIPVisionLoader`
- `StyleModelLoader`
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

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Flex.1-alpha.safetensors`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（51/59）

**有卡**：`StyleModelApply`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`AddLabel`、`ImageConcatMulti`、`VAEEncode`、`CLIPTextEncode`、`ImageResizeKJ`、`CLIPVisionEncode`、`KSampler`、`LoadImage`、`CheckpointLoaderSimple`、`CLIPVisionLoader`、`StyleModelLoader`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
