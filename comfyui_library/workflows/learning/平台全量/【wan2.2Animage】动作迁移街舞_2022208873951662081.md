---
key: 平台全量/【wan2.2Animage】动作迁移街舞_2022208873951662081.json
name: 【wan2.2Animage】动作迁移街舞_2022208873951662081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【wan2.2Animage】动作迁移街舞_2022208873951662081.json
hash: 8ed8e086ce2f79bf
coverage: 0.987342
learned_at: 2026-11-14 01:22:30
nodes: [LoraLoaderModelOnly, VAELoader, easy setNode, UNETLoader, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, CLIPVisionLoader, easy setNode, WanAnimateToVideo, easy getNode, easy getNode, SimpleMath+, easy getNode, DWPreprocessor, easy getNode, easy setNode, VHS_VideoInfo, DWPreprocessor, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, easy setNode, easy setNode, easy setNode, Int, easy getNode, Label (rgthree), Label (rgthree), Label (rgthree), LayerUtility: PurgeVRAM, easy getNode, PreviewImage, ModelSamplingSD3, LayerUtility: PurgeVRAM, Int, easy getNode, VHS_LoadVideo, LoadImage, CLIPLoader, easy setNode, LoraLoaderModelOnly, PathchSageAttentionKJ, easy setNode, easy setNode, easy setNode, Int, ImageScaleByAspectRatio_UTK, ImageScaleByAspectRatio_UTK, easy setNode, easy getNode, OnnxDetectionModelLoader, easy setNode, Int, DrawViTPose, easy setNode, easy setNode, easy getNode, easy getNode, easy setNode, easy getNode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, easy getNode, CLIPTextEncode, PoseAndFaceDetection, KSampler, easy getNode, CLIPTextEncode, easy getNode, CLIPVisionEncode, ImageResizeKJv2, easy setNode, easy getNode, easy getNode, VHS_VideoCombine, VAEDecode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/【wan2.2Animage】动作迁移街舞_2022208873951662081.json

> 来源文件 `comfyui_library/workflows/平台全量/【wan2.2Animage】动作迁移街舞_2022208873951662081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `easy setNode`
- `UNETLoader` ★核心
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `CLIPVisionLoader`
- `easy setNode`
- `WanAnimateToVideo`
- `easy getNode`
- `easy getNode`
- `SimpleMath+`
- `easy getNode`
- `DWPreprocessor`
- `easy getNode`
- `easy setNode`
- `VHS_VideoInfo`
- `DWPreprocessor`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `Int`
- `easy getNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `LayerUtility: PurgeVRAM`
- `easy getNode`
- `PreviewImage`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `Int`
- `easy getNode`
- `VHS_LoadVideo`
- `LoadImage`
- `CLIPLoader`
- `easy setNode`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `Int`
- `ImageScaleByAspectRatio_UTK`
- `ImageScaleByAspectRatio_UTK`
- `easy setNode`
- `easy getNode`
- `OnnxDetectionModelLoader`
- `easy setNode`
- `Int`
- `DrawViTPose`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy getNode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `easy getNode`
- `CLIPTextEncode` ★核心
- `PoseAndFaceDetection`
- `KSampler` ★核心
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `CLIPVisionEncode`
- `ImageResizeKJv2`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `VHS_VideoCombine`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `0`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **99%**（78/79）

**有卡**：`LoraLoaderModelOnly`、`VAELoader`、`easy setNode`、`UNETLoader`、`easy getNode`、`CLIPVisionLoader`、`WanAnimateToVideo`、`SimpleMath+`、`DWPreprocessor`、`VHS_VideoInfo`、`LayerUtility: PurgeVRAM`、`Int`、`Label (rgthree)`、`ModelSamplingSD3`、`VHS_LoadVideo`、`LoadImage`、`CLIPLoader`、`PathchSageAttentionKJ`、`ImageScaleByAspectRatio_UTK`、`OnnxDetectionModelLoader`、`DrawViTPose`、`CLIPTextEncode`、`PoseAndFaceDetection`、`KSampler`、`CLIPVisionEncode`、`ImageResizeKJv2`、`VHS_VideoCombine`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
