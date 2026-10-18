---
key: 视频生成/图生视频/Wan2.2-Animate-图生视频（动作迁移+前后视角一致性）_1991499381406908418.json
name: Wan2.2-Animate-图生视频（动作迁移+前后视角一致性）_1991499381406908418.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Animate-图生视频（动作迁移+前后视角一致性）_1991499381406908418.json
hash: ae4d80911ec4258b
coverage: 0.641304
learned_at: 2026-10-15 22:33:14
nodes: [CLIPVisionLoader, CLIPVisionLoader, SetNode, CLIPLoader, VAELoader, SetNode, ModelSamplingSD3, LoraLoaderModelOnly, UNETLoader, SetNode, SetNode, SetNode, DWPreprocessor, SetNode, TrimVideoLatent, KSampler, SetNode, VHS_VideoCombine, DWPreprocessor, LoraLoaderModelOnly, TrimVideoLatent, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, TrimVideoLatent, GetNode, GetNode, ImageBatchMulti, GetNode, GetNode, VHS_VideoCombine, Int, KSampler, easy seed, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, GetNode, WanAnimateToVideo, SimpleMath+, GetImageRangeFromBatch, GetImageRangeFromBatch, GetImageRangeFromBatch, VAEDecode, VHS_GetImageCount, VAEDecode, VHS_GetImageCount, VAEDecode, VHS_GetImageCount, SetNode, SetNode, VHS_VideoInfoLoaded, SimpleMath+, SetNode, SetNode, Int, Note, PixelPerfectResolution, Int, VHS_LoadVideo, WanAnimateToVideo, WanAnimateToVideo, GetNode, GetNode, Int, LayerMask: SegformerUltraV2, LoadImage, VHS_VideoCombine, GetNode, LayerMask: SegformerClothesPipelineLoader, LoadImage, VHS_VideoCombine, CLIPVisionEncode, Int, SetNode, ImageResizeKJv2, CLIPTextEncode, CLIPTextEncode, CM_IntToFloat, PreviewImage, ImageResizeKJv2, PreviewImage, LayerUtility: ImageRemoveAlpha, ImageAndMaskPreview, PreviewImage, RHHiddenNodes]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 733419822079050, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2-Animate-图生视频（动作迁移+前后视角一致性）_1991499381406908418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1991499381406908418.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `CLIPVisionLoader`
- `CLIPVisionLoader`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `DWPreprocessor`
- `SetNode`
- `TrimVideoLatent`
- `KSampler` ★核心
- `SetNode`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `LoraLoaderModelOnly` ★核心
- `TrimVideoLatent`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `ImageBatchMulti`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Int`
- `KSampler` ★核心
- `easy seed`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanAnimateToVideo`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `VAEDecode` ★核心
- `VHS_GetImageCount`
- `VAEDecode` ★核心
- `VHS_GetImageCount`
- `VAEDecode` ★核心
- `VHS_GetImageCount`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `Int`
- `Note`
- `PixelPerfectResolution`
- `Int`
- `VHS_LoadVideo`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `GetNode`
- `GetNode`
- `Int`
- `LayerMask: SegformerUltraV2`
- `LoadImage`
- `VHS_VideoCombine`
- `GetNode`
- `LayerMask: SegformerClothesPipelineLoader`
- `LoadImage`
- `VHS_VideoCombine`
- `CLIPVisionEncode`
- `Int`
- `SetNode`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CM_IntToFloat`
- `PreviewImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `LayerUtility: ImageRemoveAlpha`
- `ImageAndMaskPreview`
- `PreviewImage`
- `RHHiddenNodes`

## 关键参数

- `seed` = `733419822079050`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（59/92）

**有卡**：`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`UNETLoader`、`DWPreprocessor`、`TrimVideoLatent`、`KSampler`、`VHS_VideoCombine`、`ImageBatchMulti`、`Int`、`easy seed`、`WanAnimateToVideo`、`SimpleMath+`、`GetImageRangeFromBatch`、`VAEDecode`、`VHS_GetImageCount`、`VHS_VideoInfoLoaded`、`PixelPerfectResolution`、`VHS_LoadVideo`、`LayerMask: SegformerUltraV2`、`LoadImage`、`LayerMask: SegformerClothesPipelineLoader`、`CLIPVisionEncode`、`ImageResizeKJv2`、`CLIPTextEncode`、`CM_IntToFloat`、`LayerUtility: ImageRemoveAlpha`、`ImageAndMaskPreview`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
