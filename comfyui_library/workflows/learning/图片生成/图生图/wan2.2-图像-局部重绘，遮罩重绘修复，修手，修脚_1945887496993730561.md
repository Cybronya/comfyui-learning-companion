---
key: 图片生成/图生图/wan2.2-图像-局部重绘，遮罩重绘修复，修手，修脚_1945887496993730561.json
name: wan2.2-图像-局部重绘，遮罩重绘修复，修手，修脚_1945887496993730561
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2-图像-局部重绘，遮罩重绘修复，修手，修脚_1945887496993730561.json
hash: 365c2dbc5b71d342
coverage: 0.675
learned_at: 2026-10-23 11:46:00
nodes: [LayerMask: MaskPreview, LayerMask: LoadSegmentAnythingModels, EmptyImage, GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, SetNode, LayerMask: SegmentAnythingUltra V3, SetNode, VAEDecode, SetNode, InpaintCrop, Anything Everywhere3, KSampler, VAELoader, CLIPLoader, InpaintModelConditioning, InpaintStitch, GetNode, GetNode, SaveImage, LoadImage, Image Comparer (rgthree), ImageToMask, GetNode, GetNode, ImpactSwitch, GetNode, GetNode, PreviewImage, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text, ArgosTranslateTextNode, CLIPTextEncode, ArgosTranslateTextNode, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "heun", "scheduler": "beta", "seed": 248499599717118, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/wan2.2-图像-局部重绘，遮罩重绘修复，修手，修脚_1945887496993730561.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2-图像-局部重绘，遮罩重绘修复，修手，修脚_1945887496993730561.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LayerMask: MaskPreview`
- `LayerMask: LoadSegmentAnythingModels`
- `EmptyImage`
- `GetImageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `SetNode`
- `LayerMask: SegmentAnythingUltra V3`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `InpaintCrop`
- `Anything Everywhere3`
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `InpaintModelConditioning`
- `InpaintStitch`
- `GetNode`
- `GetNode`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `ImageToMask`
- `GetNode`
- `GetNode`
- `ImpactSwitch`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `ArgosTranslateTextNode`
- `CLIPTextEncode` ★核心
- `ArgosTranslateTextNode`
- `CR Text`

## 关键参数

- `seed` = `248499599717118`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **68%**（27/40）

**有卡**：`LayerMask: MaskPreview`、`LayerMask: LoadSegmentAnythingModels`、`EmptyImage`、`GetImageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`LayerMask: SegmentAnythingUltra V3`、`VAEDecode`、`InpaintCrop`、`KSampler`、`VAELoader`、`CLIPLoader`、`InpaintModelConditioning`、`InpaintStitch`、`SaveImage`、`LoadImage`、`ImageToMask`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`CR Text`、`ArgosTranslateTextNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
