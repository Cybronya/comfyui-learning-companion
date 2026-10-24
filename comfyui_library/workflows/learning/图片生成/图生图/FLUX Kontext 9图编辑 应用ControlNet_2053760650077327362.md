---
key: 图片生成/图生图/FLUX Kontext 9图编辑 应用ControlNet_2053760650077327362.json
name: FLUX Kontext 9图编辑 应用ControlNet_2053760650077327362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX Kontext 9图编辑 应用ControlNet_2053760650077327362.json
hash: c3f90a0a51ce39a4
coverage: 0.964286
learned_at: 2026-10-23 10:53:23
nodes: [RandomNoise, KSamplerSelect, ApplyFBCacheOnModel, ReferenceLatent, DualCLIPLoader, UNETLoader, VAELoader, VAEDecode, easy cleanGpuUsed, DualCLIPLoader, SamplerCustomAdvanced, SetUnionControlNetType, ControlNetLoader, PreviewImage, ControlNetApplyAdvanced, BasicScheduler, FluxGuidance, CLIPTextEncode, BasicGuider, VAEEncode, LoadImage, RHUploadZip, LayerUtility: ImageScaleByAspectRatio V2, AIO_Preprocessor, ConstrainImage|pysssss, CLIPTextEncode, SaveImage, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"controlnet_strength": 1.0000000000000002}
---

# 图片生成/图生图/FLUX Kontext 9图编辑 应用ControlNet_2053760650077327362.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX Kontext 9图编辑 应用ControlNet_2053760650077327362.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ApplyFBCacheOnModel`
- `ReferenceLatent`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `DualCLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `SetUnionControlNetType`
- `ControlNetLoader`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `BasicScheduler`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `VAEEncode` ★核心
- `LoadImage`
- `RHUploadZip`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AIO_Preprocessor`
- `ConstrainImage|pysssss`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `controlnet_strength` = `1.0000000000000002`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`RandomNoise`、`KSamplerSelect`、`ApplyFBCacheOnModel`、`ReferenceLatent`、`DualCLIPLoader`、`UNETLoader`、`VAELoader`、`VAEDecode`、`easy cleanGpuUsed`、`SamplerCustomAdvanced`、`SetUnionControlNetType`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`BasicScheduler`、`FluxGuidance`、`CLIPTextEncode`、`BasicGuider`、`VAEEncode`、`LoadImage`、`RHUploadZip`、`LayerUtility: ImageScaleByAspectRatio V2`、`AIO_Preprocessor`、`ConstrainImage|pysssss`、`SaveImage`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
