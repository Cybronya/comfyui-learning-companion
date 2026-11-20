---
key: 平台全量/Better ReActor Face Swap + InstantID workflow_1868581753186304002.json
name: Better ReActor Face Swap + InstantID workflow_1868581753186304002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Better ReActor Face Swap + InstantID workflow_1868581753186304002.json
hash: a882d0ae38345427
coverage: 0.846154
learned_at: 2026-11-14 00:20:56
nodes: [ImpactSimpleDetectorSEGS, SEGSPreview, FaceKeypointsPreprocessor, CLIPTextEncode, CLIPTextEncode, LoadImage, ImageResize, SelfAttentionGuidance, ToBasicPipe, DenoiseSchedulerDetailerHookProvider, LoraLoader, ImpactSEGSOrderedFilter, DetailerForEachDebugPipe, PreviewImage, ApplyInstantID, ImpactSimpleDetectorSEGS, ImpactSEGSOrderedFilter, SEGSPreview, RescaleCFG, Note, Note, ControlNetApplyAdvanced, ControlNetLoader, Zoe-DepthMapPreprocessor, CannyEdgePreprocessor, Image Comparer (rgthree), PreviewImage, UltralyticsDetectorProvider, SAMLoader, ReActorMaskHelper, CheckpointLoaderSimple, ControlNetLoader, InstantIDFaceAnalysis, InstantIDModelLoader, ReActorFaceSwap, PreviewImage, SEGSPaste, SaveImage, LoadImage]
patterns: [lora]
missing: []
parameters: {"checkpoint": "MILU XL TurboLcm(mix)_v6.0.safetensors", "controlnet_strength": 0.7000000000000001, "lora_name": "XL\\SDXL_BetterFaces-LoRA_v1.safetensors", "strength_clip": 0.8, "strength_model": 0.8}
---

# 平台全量/Better ReActor Face Swap + InstantID workflow_1868581753186304002.json

> 来源文件 `comfyui_library/workflows/平台全量/Better ReActor Face Swap + InstantID workflow_1868581753186304002.json`

## 结构

**生成流程**：Model → Condition → Control → Process → Output → Other

**节点**（39 个）：
- `ImpactSimpleDetectorSEGS`
- `SEGSPreview`
- `FaceKeypointsPreprocessor`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageResize`
- `SelfAttentionGuidance`
- `ToBasicPipe`
- `DenoiseSchedulerDetailerHookProvider`
- `LoraLoader` ★核心
- `ImpactSEGSOrderedFilter`
- `DetailerForEachDebugPipe`
- `PreviewImage`
- `ApplyInstantID`
- `ImpactSimpleDetectorSEGS`
- `ImpactSEGSOrderedFilter`
- `SEGSPreview`
- `RescaleCFG`
- `Note`
- `Note`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `Zoe-DepthMapPreprocessor`
- `CannyEdgePreprocessor`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `ReActorMaskHelper`
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `ReActorFaceSwap`
- `PreviewImage`
- `SEGSPaste`
- `SaveImage`
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `XL\SDXL_BetterFaces-LoRA_v1.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `0.8`
- `controlnet_strength` = `0.7000000000000001`
- `checkpoint` = `MILU XL TurboLcm(mix)_v6.0.safetensors`

## 知识

覆盖率 **85%**（33/39）

**有卡**：`ImpactSimpleDetectorSEGS`、`SEGSPreview`、`FaceKeypointsPreprocessor`、`CLIPTextEncode`、`LoadImage`、`ImageResize`、`SelfAttentionGuidance`、`ToBasicPipe`、`DenoiseSchedulerDetailerHookProvider`、`LoraLoader`、`ImpactSEGSOrderedFilter`、`DetailerForEachDebugPipe`、`ApplyInstantID`、`RescaleCFG`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`Zoe-DepthMapPreprocessor`、`CannyEdgePreprocessor`、`UltralyticsDetectorProvider`、`SAMLoader`、`ReActorMaskHelper`、`CheckpointLoaderSimple`、`InstantIDFaceAnalysis`、`InstantIDModelLoader`、`ReActorFaceSwap`、`SEGSPaste`、`SaveImage`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CannyEdgePreprocessor、ControlNetApplyAdvanced、ControlNetLoader、Zoe-DepthMapPreprocessor、RescaleCFG
