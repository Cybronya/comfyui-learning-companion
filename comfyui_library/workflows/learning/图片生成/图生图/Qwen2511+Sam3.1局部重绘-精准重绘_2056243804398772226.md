---
key: 图片生成/图生图/Qwen2511+Sam3.1局部重绘-精准重绘_2056243804398772226.json
name: Qwen2511+Sam3.1局部重绘-精准重绘_2056243804398772226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2511+Sam3.1局部重绘-精准重绘_2056243804398772226.json
hash: c0a751909cdf5f2d
coverage: 0.714286
learned_at: 2026-10-23 11:19:22
nodes: [CLIPLoader, KSampler, VAEDecode, ConditioningZeroOut, Image Comparer (rgthree), CropWithPadInfo, ImageScaleBy, PreviewImage, QwenEditOutputExtractor, QwenEditConfigPreparer, TextEncodeQwenImageEditPlusCustom_lrzjason, QwenEditAdaptiveLongestEdge, MaskPreview, Image Comparer (rgthree), ModelSamplingAuraFlow, CFGNorm, LayerMask: MaskGrow, LayerUtility: RestoreCropBox, SaveImage, LayerUtility: CropByMask V2, PreviewImage, PreviewImage, CLIPTextEncode, SAM3_Detect, easy showAnything, Any Switch (rgthree), MarkdownNote, UNETLoader, LoraLoaderModelOnly, VAELoader, Fast Groups Bypasser (rgthree), CheckpointLoaderSimple, LoadImage, ImageResizeKJv2, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sam3.1-multiplex-fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 1091359629774735, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen2511+Sam3.1局部重绘-精准重绘_2056243804398772226.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2511+Sam3.1局部重绘-精准重绘_2056243804398772226.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `CLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `CropWithPadInfo`
- `ImageScaleBy`
- `PreviewImage`
- `QwenEditOutputExtractor`
- `QwenEditConfigPreparer`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `QwenEditAdaptiveLongestEdge`
- `MaskPreview`
- `Image Comparer (rgthree)`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `LayerMask: MaskGrow`
- `LayerUtility: RestoreCropBox`
- `SaveImage`
- `LayerUtility: CropByMask V2`
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `SAM3_Detect`
- `easy showAnything`
- `Any Switch (rgthree)`
- `MarkdownNote`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `1091359629774735`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **71%**（25/35）

**有卡**：`CLIPLoader`、`KSampler`、`VAEDecode`、`ConditioningZeroOut`、`CropWithPadInfo`、`ImageScaleBy`、`QwenEditOutputExtractor`、`QwenEditConfigPreparer`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`QwenEditAdaptiveLongestEdge`、`MaskPreview`、`ModelSamplingAuraFlow`、`CFGNorm`、`LayerMask: MaskGrow`、`LayerUtility: RestoreCropBox`、`SaveImage`、`LayerUtility: CropByMask V2`、`CLIPTextEncode`、`SAM3_Detect`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CheckpointLoaderSimple`、`LoadImage`、`ImageResizeKJv2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
