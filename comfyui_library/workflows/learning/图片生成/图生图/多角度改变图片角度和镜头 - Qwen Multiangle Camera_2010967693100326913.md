---
key: 图片生成/图生图/多角度改变图片角度和镜头 - Qwen Multiangle Camera_2010967693100326913.json
name: 多角度改变图片角度和镜头 - Qwen Multiangle Camera_2010967693100326913
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多角度改变图片角度和镜头 - Qwen Multiangle Camera_2010967693100326913.json
hash: 3e9320acb0ca8114
coverage: 0.913043
learned_at: 2026-10-23 12:46:09
nodes: [CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, INTConstant, easy showAnything, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, KSampler, ModelSamplingAuraFlow, CFGNorm, TextEncodeQwenImageEditPlus, VAEEncode, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, TextEncodeQwenImageEditPlus, VAEDecode, easy promptList, QwenMultiangleCameraNode, VNCCS_VisualPositionControl, SaveImage, easy showAnything]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 467249244358882, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/多角度改变图片角度和镜头 - Qwen Multiangle Camera_2010967693100326913.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多角度改变图片角度和镜头 - Qwen Multiangle Camera_2010967693100326913.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `INTConstant`
- `easy showAnything`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `easy promptList`
- `QwenMultiangleCameraNode`
- `VNCCS_VisualPositionControl`
- `SaveImage`
- `easy showAnything`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `467249244358882`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImage`、`INTConstant`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`ModelSamplingAuraFlow`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`FluxKontextMultiReferenceLatentMethod`、`VAEDecode`、`easy promptList`、`QwenMultiangleCameraNode`、`VNCCS_VisualPositionControl`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
