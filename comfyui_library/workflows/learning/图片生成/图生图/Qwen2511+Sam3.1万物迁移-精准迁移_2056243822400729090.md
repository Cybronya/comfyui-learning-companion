---
key: 图片生成/图生图/Qwen2511+Sam3.1万物迁移-精准迁移_2056243822400729090.json
name: Qwen2511+Sam3.1万物迁移-精准迁移_2056243822400729090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2511+Sam3.1万物迁移-精准迁移_2056243822400729090.json
hash: 95205e44f11fa49d
coverage: 0.735849
learned_at: 2026-10-23 11:19:22
nodes: [CLIPLoader, KSampler, VAEDecode, ConditioningZeroOut, QwenEditConfigPreparer, PrimitiveStringMultiline, Image Comparer (rgthree), PreviewImage, CropWithPadInfo, PreviewImage, ImageScaleBy, PreviewImage, QwenEditOutputExtractor, QwenEditConfigPreparer, TextEncodeQwenImageEditPlusCustom_lrzjason, QwenEditAdaptiveLongestEdge, QwenEditAdaptiveLongestEdge, MaskPreview, MaskToImage, LayerUtility: ImageReel, QwenEditListExtractor, QwenEditAny2Image, LayerUtility: ImageReelComposit, PreviewImage, Image Comparer (rgthree), CropWithPadInfo, CropWithPadInfo, ModelSamplingAuraFlow, CFGNorm, ImageResizeKJv2, LayerMask: MaskGrow, TTP_Expand_And_Mask, LayerUtility: RestoreCropBox, SaveImage, LayerUtility: CropByMask V2, PreviewImage, PreviewImage, PreviewImage, PreviewImage, RMBG, SAM3_Detect, ImageResizeKJv2, Fast Groups Bypasser (rgthree), Any Switch (rgthree), MaskPreview, MarkdownNote, CheckpointLoaderSimple, UNETLoader, VAELoader, LoraLoaderModelOnly, LoadImage, LoadImage, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sam3.1-multiplex-fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 1091359629774735, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen2511+Sam3.1万物迁移-精准迁移_2056243822400729090.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2511+Sam3.1万物迁移-精准迁移_2056243822400729090.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `CLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `QwenEditConfigPreparer`
- `PrimitiveStringMultiline`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `CropWithPadInfo`
- `PreviewImage`
- `ImageScaleBy`
- `PreviewImage`
- `QwenEditOutputExtractor`
- `QwenEditConfigPreparer`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditAdaptiveLongestEdge`
- `MaskPreview`
- `MaskToImage`
- `LayerUtility: ImageReel`
- `QwenEditListExtractor`
- `QwenEditAny2Image`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `CropWithPadInfo`
- `CropWithPadInfo`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `ImageResizeKJv2`
- `LayerMask: MaskGrow`
- `TTP_Expand_And_Mask`
- `LayerUtility: RestoreCropBox`
- `SaveImage`
- `LayerUtility: CropByMask V2`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `RMBG`
- `SAM3_Detect`
- `ImageResizeKJv2`
- `Fast Groups Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `MaskPreview`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `1091359629774735`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **74%**（39/53）

**有卡**：`CLIPLoader`、`KSampler`、`VAEDecode`、`ConditioningZeroOut`、`QwenEditConfigPreparer`、`CropWithPadInfo`、`ImageScaleBy`、`QwenEditOutputExtractor`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`QwenEditAdaptiveLongestEdge`、`MaskPreview`、`MaskToImage`、`LayerUtility: ImageReel`、`QwenEditListExtractor`、`QwenEditAny2Image`、`LayerUtility: ImageReelComposit`、`ModelSamplingAuraFlow`、`CFGNorm`、`ImageResizeKJv2`、`LayerMask: MaskGrow`、`TTP_Expand_And_Mask`、`LayerUtility: RestoreCropBox`、`SaveImage`、`LayerUtility: CropByMask V2`、`RMBG`、`SAM3_Detect`、`CheckpointLoaderSimple`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
