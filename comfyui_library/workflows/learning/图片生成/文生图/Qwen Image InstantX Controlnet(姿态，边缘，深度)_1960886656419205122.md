---
key: 图片生成/文生图/Qwen Image InstantX Controlnet(姿态，边缘，深度)_1960886656419205122.json
name: Qwen Image InstantX Controlnet(姿态，边缘，深度)_1960886656419205122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image InstantX Controlnet(姿态，边缘，深度)_1960886656419205122.json
hash: 7b7e0be7fa583e85
coverage: 0.819672
learned_at: 2026-10-10 20:58:55
nodes: [ModelSamplingAuraFlow, CFGNorm, Anything Everywhere3, EmptySD3LatentImage, ControlNetLoader, OpenposePreprocessor, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPTextEncode, SaveLatent, SaveImage, EmptySD3LatentImage, ControlNetLoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPTextEncode, SaveLatent, SeedVR2BlockSwap, SaveImage, AIO_Preprocessor, SetUnionControlNetType, EmptySD3LatentImage, ControlNetLoader, CLIPTextEncode, CLIPTextEncode, SaveLatent, SeedVR2BlockSwap, SetUnionControlNetType, AIO_Preprocessor, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, PreviewImage, LoraLoaderModelOnly, ControlNetApplySD3, LoadImage, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Text, Text, Text, ControlNetApplySD3, PreviewImage, KSampler, Fast Groups Bypasser (rgthree), PreviewImage, VAEDecode, KSampler, PreviewImage, VAEDecode, PreviewImage, VAEDecode, LoraLoaderModelOnly, ControlNetApplySD3, VAELoader, CLIPLoader, SetUnionControlNetType, KSampler, UNETLoader, PreviewImage, SaveImage]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 725569396043432, "steps": 8}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image InstantX Controlnet(姿态，边缘，深度)_1960886656419205122.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image InstantX Controlnet(姿态，边缘，深度)_1960886656419205122.json`

## 结构

**节点**（61 个）：
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `Anything Everywhere3`
- `EmptySD3LatentImage`
- `ControlNetLoader`
- `OpenposePreprocessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `SaveLatent`
- `SaveImage`
- `EmptySD3LatentImage`
- `ControlNetLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `SaveLatent`
- `SeedVR2BlockSwap`
- `SaveImage`
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `EmptySD3LatentImage`
- `ControlNetLoader`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `SaveLatent`
- `SeedVR2BlockSwap`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `PreviewImage`
- `LoraLoaderModelOnly`
- `ControlNetApplySD3`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Text`
- `Text`
- `Text`
- `ControlNetApplySD3`
- `PreviewImage`
- `KSampler`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `VAEDecode`
- `KSampler`
- `PreviewImage`
- `VAEDecode`
- `PreviewImage`
- `VAEDecode`
- `LoraLoaderModelOnly`
- `ControlNetApplySD3`
- `VAELoader`
- `CLIPLoader`
- `SetUnionControlNetType`
- `KSampler`
- `UNETLoader`
- `PreviewImage`
- `SaveImage`

## 关键参数

- `cfg` = `1`
- `controlnet_strength` = `1.0000000000000002`
- `denoise` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `seed` = `725569396043432`
- `steps` = `8`

## 知识

覆盖率 **82%**（50/61）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`Anything Everywhere3`、`EmptySD3LatentImage`、`ControlNetLoader`、`OpenposePreprocessor`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`SaveLatent`、`SaveImage`、`SeedVR2BlockSwap`、`AIO_Preprocessor`、`SetUnionControlNetType`、`DepthAnything_V2`、`DownloadAndLoadDepthAnythingV2Model`、`PreviewImage`、`LoraLoaderModelOnly`、`ControlNetApplySD3`、`LoadImage`、`Text`、`KSampler`、`Fast Groups Bypasser (rgthree)`、`VAEDecode`

**缺卡**（3）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
