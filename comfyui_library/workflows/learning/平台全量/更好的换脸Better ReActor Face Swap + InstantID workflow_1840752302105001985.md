---
key: 平台全量/更好的换脸Better ReActor Face Swap + InstantID workflow_1840752302105001985.json
name: 更好的换脸Better ReActor Face Swap + InstantID workflow_1840752302105001985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/更好的换脸Better ReActor Face Swap + InstantID workflow_1840752302105001985.json
hash: 02feb3fb80cf8315
coverage: 0.868421
learned_at: 2026-11-14 02:13:46
nodes: [ImpactSimpleDetectorSEGS, UltralyticsDetectorProvider, SAMLoader, SEGSPreview, InstantIDModelLoader, InstantIDFaceAnalysis, FaceKeypointsPreprocessor, CLIPTextEncode, CLIPTextEncode, SelfAttentionGuidance, ToBasicPipe, DenoiseSchedulerDetailerHookProvider, LoraLoader, ImpactSEGSOrderedFilter, PreviewImage, ApplyInstantID, ImpactSimpleDetectorSEGS, ImpactSEGSOrderedFilter, RescaleCFG, Note, Note, ControlNetApplyAdvanced, ControlNetLoader, Zoe-DepthMapPreprocessor, ReActorMaskHelper, CannyEdgePreprocessor, ReActorFaceSwap, CheckpointLoaderSimple, LoadImage, ControlNetLoader, ImageResize, SEGSPreview, Image Comparer (rgthree), LoadImage, DetailerForEachDebugPipe, SEGSPaste, PreviewImage, SaveImage]
patterns: [lora]
missing: []
parameters: {"checkpoint": "AWPortrait XL_1.1.safetensors", "controlnet_strength": 0.7000000000000001, "lora_name": "XL\\SDXL_BetterFaces-LoRA_v1.safetensors", "strength_clip": 0.8, "strength_model": 0.8}
---

# 平台全量/更好的换脸Better ReActor Face Swap + InstantID workflow_1840752302105001985.json

> 来源文件 `comfyui_library/workflows/平台全量/更好的换脸Better ReActor Face Swap + InstantID workflow_1840752302105001985.json`

## 结构

**生成流程**：Model → Condition → Control → Process → Output → Other

**节点**（38 个）：
- `ImpactSimpleDetectorSEGS`
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `SEGSPreview`
- `InstantIDModelLoader`
- `InstantIDFaceAnalysis`
- `FaceKeypointsPreprocessor`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SelfAttentionGuidance`
- `ToBasicPipe`
- `DenoiseSchedulerDetailerHookProvider`
- `LoraLoader` ★核心
- `ImpactSEGSOrderedFilter`
- `PreviewImage`
- `ApplyInstantID`
- `ImpactSimpleDetectorSEGS`
- `ImpactSEGSOrderedFilter`
- `RescaleCFG`
- `Note`
- `Note`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `Zoe-DepthMapPreprocessor`
- `ReActorMaskHelper`
- `CannyEdgePreprocessor`
- `ReActorFaceSwap`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `ControlNetLoader`
- `ImageResize`
- `SEGSPreview`
- `Image Comparer (rgthree)`
- `LoadImage`
- `DetailerForEachDebugPipe`
- `SEGSPaste`
- `PreviewImage`
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `XL\SDXL_BetterFaces-LoRA_v1.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `0.8`
- `controlnet_strength` = `0.7000000000000001`
- `checkpoint` = `AWPortrait XL_1.1.safetensors`

## 知识

覆盖率 **87%**（33/38）

**有卡**：`ImpactSimpleDetectorSEGS`、`UltralyticsDetectorProvider`、`SAMLoader`、`SEGSPreview`、`InstantIDModelLoader`、`InstantIDFaceAnalysis`、`FaceKeypointsPreprocessor`、`CLIPTextEncode`、`SelfAttentionGuidance`、`ToBasicPipe`、`DenoiseSchedulerDetailerHookProvider`、`LoraLoader`、`ImpactSEGSOrderedFilter`、`ApplyInstantID`、`RescaleCFG`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`Zoe-DepthMapPreprocessor`、`ReActorMaskHelper`、`CannyEdgePreprocessor`、`ReActorFaceSwap`、`CheckpointLoaderSimple`、`LoadImage`、`ImageResize`、`DetailerForEachDebugPipe`、`SEGSPaste`、`SaveImage`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CannyEdgePreprocessor、ControlNetApplyAdvanced、ControlNetLoader、Zoe-DepthMapPreprocessor、RescaleCFG
