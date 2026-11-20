---
key: 平台全量/Qwen_image_edit_plus_Multiple angles多角度视角生成_2009499550276395010.json
name: Qwen_image_edit_plus_Multiple angles多角度视角生成_2009499550276395010
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen_image_edit_plus_Multiple angles多角度视角生成_2009499550276395010.json
hash: 844593883ed83275
coverage: 0.857143
learned_at: 2026-11-14 00:53:42
nodes: [CLIPTextEncode, VAEDecode, KSampler, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, SaveImage, CLIPLoader, VAELoader, VAEEncode, EmptyLatentImage, LoadImage, VNCCS_VisualPositionControl, VNCCS_PositionControl, Note, PrimitiveBoolean, PrimitiveStringMultiline, QwenMultiangleCameraNode, easy ifElse, easy promptList]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 720, "sampler_name": "euler", "scheduler": "simple", "seed": 643662082487502, "steps": 8, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen_image_edit_plus_Multiple angles多角度视角生成_2009499550276395010.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen_image_edit_plus_Multiple angles多角度视角生成_2009499550276395010.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `VNCCS_VisualPositionControl`
- `VNCCS_PositionControl`
- `Note`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `QwenMultiangleCameraNode`
- `easy ifElse`
- `easy promptList`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `643662082487502`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`EmptyLatentImage`、`LoadImage`、`VNCCS_VisualPositionControl`、`VNCCS_PositionControl`、`PrimitiveBoolean`、`QwenMultiangleCameraNode`、`easy promptList`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
