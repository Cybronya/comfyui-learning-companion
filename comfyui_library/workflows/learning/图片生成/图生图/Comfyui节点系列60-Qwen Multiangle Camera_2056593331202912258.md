---
key: 图片生成/图生图/Comfyui节点系列60-Qwen Multiangle Camera_2056593331202912258.json
name: Comfyui节点系列60-Qwen Multiangle Camera_2056593331202912258
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Comfyui节点系列60-Qwen Multiangle Camera_2056593331202912258.json
hash: 065c4ef4b0b81e3b
coverage: 0.78125
learned_at: 2026-10-23 10:52:02
nodes: [ModelSamplingAuraFlow, CFGNorm, ConditioningZeroOut, TextEncodeQwenImageEditPlus, VAEEncode, LoraLoaderModelOnly, CLIPLoader, VAELoader, UNETLoader, KSampler, ImageScaleToTotalPixels, easy showAnything, LoraLoaderModelOnly, Note, PreviewAny, VNCCS_VisualPositionControl, QwenMultiangleCameraNode, GetNode, LoadImage, easy promptLine, easy promptLine, VAEDecode, Reroute, AddLabel, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, PreviewImage, SaveImage, easy promptLine]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 967811440312618, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Comfyui节点系列60-Qwen Multiangle Camera_2056593331202912258.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Comfyui节点系列60-Qwen Multiangle Camera_2056593331202912258.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ImageScaleToTotalPixels`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `PreviewAny`
- `VNCCS_VisualPositionControl`
- `QwenMultiangleCameraNode`
- `GetNode`
- `LoadImage`
- `easy promptLine`
- `easy promptLine`
- `VAEDecode` ★核心
- `Reroute`
- `AddLabel`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `easy promptLine`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `967811440312618`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（25/32）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`ConditioningZeroOut`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSampler`、`ImageScaleToTotalPixels`、`VNCCS_VisualPositionControl`、`QwenMultiangleCameraNode`、`LoadImage`、`easy promptLine`、`VAEDecode`、`AddLabel`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
