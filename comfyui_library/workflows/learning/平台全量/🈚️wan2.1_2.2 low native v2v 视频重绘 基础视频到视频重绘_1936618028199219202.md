---
key: 平台全量/🈚️wan2.1_2.2 low native v2v 视频重绘 基础视频到视频重绘_1936618028199219202.json
name: 🈚️wan2.1_2.2 low native v2v 视频重绘 基础视频到视频重绘_1936618028199219202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🈚️wan2.1_2.2 low native v2v 视频重绘 基础视频到视频重绘_1936618028199219202.json
hash: ff1f113c13020c9a
coverage: 0.581818
learned_at: 2026-11-14 02:54:30
nodes: [SetNode, SetNode, CLIPTextEncode, SetNode, SetNode, ImageConcatMulti, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, GetNode, Int, GetNode, ImageSmartSharpen+, SetNode, SetNode, Float, VAELoader, CLIPLoader, ImpactSwitch, ReverseImageBatch, GetImageRangeFromBatch, SetNode, SetNode, SetNode, CLIPTextEncode, ImageBatchMulti, GetImageRangeFromBatch, UNETLoader, VHS_VideoCombine, PrimitiveNode, UpscaleModelLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, CFGNorm, GetNode, VAEEncodeTiled, GetNode, GetNode, GetNode, LatentPixelScale, VHS_VideoCombine, LoraLoaderModelOnly, UNETLoader, VHS_LoadVideo, GetNode, GetNode, VAEDecode, KSampler, ModelSamplingSD3, WanContextWindowsManual, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.5000000000000001, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 318277446991052, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/🈚️wan2.1_2.2 low native v2v 视频重绘 基础视频到视频重绘_1936618028199219202.json

> 来源文件 `comfyui_library/workflows/平台全量/🈚️wan2.1_2.2 low native v2v 视频重绘 基础视频到视频重绘_1936618028199219202.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（55 个）：
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `GetNode`
- `ImageSmartSharpen+`
- `SetNode`
- `SetNode`
- `Float`
- `VAELoader`
- `CLIPLoader`
- `ImpactSwitch`
- `ReverseImageBatch`
- `GetImageRangeFromBatch`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `ImageBatchMulti`
- `GetImageRangeFromBatch`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `PrimitiveNode`
- `UpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CFGNorm`
- `GetNode`
- `VAEEncodeTiled` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LatentPixelScale`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `WanContextWindowsManual`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `318277446991052`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **58%**（32/55）

**有卡**：`CLIPTextEncode`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`ImageSmartSharpen+`、`Float`、`VAELoader`、`CLIPLoader`、`ReverseImageBatch`、`GetImageRangeFromBatch`、`ImageBatchMulti`、`UNETLoader`、`VHS_VideoCombine`、`UpscaleModelLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CFGNorm`、`VAEEncodeTiled`、`LatentPixelScale`、`VHS_LoadVideo`、`VAEDecode`、`KSampler`、`ModelSamplingSD3`、`WanContextWindowsManual`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
