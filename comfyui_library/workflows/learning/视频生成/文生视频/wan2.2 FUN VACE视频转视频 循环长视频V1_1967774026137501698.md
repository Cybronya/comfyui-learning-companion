---
key: 视频生成/文生视频/wan2.2 FUN VACE视频转视频 循环长视频V1_1967774026137501698.json
name: wan2.2 FUN VACE视频转视频 循环长视频V1_1967774026137501698.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1967774026137501698.json
hash: 4e663e877859cd43
coverage: 0.58209
learned_at: 2026-10-15 22:43:45
nodes: [SetNode, SetNode, GetNode, GetNode, DiffusionModelSelector, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, easy cleanGpuUsed, VHS_VideoCombine, SetNode, SetNode, SetNode, SetNode, WanVaceToVideo, DWPreprocessor, GetImageSizeAndCount, DepthAnything_V2, PrimitiveInt, GetNode, KSamplerAdvanced, TrimVideoLatent, SetNode, KSamplerAdvanced, INTConstant, INTConstant, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, MathExpression|pysssss, GetNode, GetNode, MathExpression|pysssss, MathExpression|pysssss, SetNode, GetImagesFromBatchIndexed, easy clearCacheAll, PreviewImage, GetNode, GetImageRangeFromBatch, GetNode, GetNode, GetNode, SetNode, VHS_VideoCombine, ImageResizeKJv2, GetNode, easy forLoopEnd, GetNode, easy forLoopStart, VHS_VideoInfoLoaded, CLIPTextEncode, SetNode, CLIPLoader, VAELoader, easy cleanGpuUsed, ModelSamplingSD3, SetNode, ModelSamplingSD3, easy cleanGpuUsed, SetNode, SetNode, DiffusionModelLoaderKJ, Bjornulf_ShowInt, DiffusionModelLoaderKJ, DiffusionModelSelector, UNETLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, CFGNorm, easy cleanGpuUsed, easy clearCacheAll, PreviewImage, CLIPLoader, VAELoader, ImageResizeKJv2, ImageBatchGet, ImageScaleToTotalPixels, TextEncodeQwenImageEdit, TextEncodeQwenImageEdit, easy cleanGpuUsed, DWPreprocessor, ControlNetApplyAdvanced, SetUnionControlNetType, GetNode, KSampler, VAEEncode, ControlNetLoader, Primitive string multiline [Crystools], DF_Get_image_size, GetNode, PreviewImage, VAEDecode, CLIPTextEncode, GetImageSizeAndCount, DownloadAndLoadDepthAnythingV2Model, ColorMatch, easy batchAnything, CR Seed, VHS_VideoCombine, GetNode, LG_LoadImage, VHS_VideoCombine, VHS_LoadVideo, INTConstant, ImageResizeKJv2, GetNode, easy clearCacheAll, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LG_ImageSender, Switch image [Crystools], GetNode, WanVaceToVideo, GetNode, GetNode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 1.8000000000000003, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 49888161825358, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.2 FUN VACE视频转视频 循环长视频V1_1967774026137501698.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1967774026137501698.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（134 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `DiffusionModelSelector`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVaceToVideo`
- `DWPreprocessor`
- `GetImageSizeAndCount`
- `DepthAnything_V2`
- `PrimitiveInt`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `TrimVideoLatent`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SetNode`
- `GetImagesFromBatchIndexed`
- `easy clearCacheAll`
- `PreviewImage`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `GetNode`
- `easy forLoopEnd`
- `GetNode`
- `easy forLoopStart`
- `VHS_VideoInfoLoaded`
- `CLIPTextEncode` ★核心
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `SetNode`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `DiffusionModelLoaderKJ`
- `Bjornulf_ShowInt`
- `DiffusionModelLoaderKJ`
- `DiffusionModelSelector`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `PreviewImage`
- `CLIPLoader`
- `VAELoader`
- `ImageResizeKJv2`
- `ImageBatchGet`
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEdit`
- `easy cleanGpuUsed`
- `DWPreprocessor`
- `ControlNetApplyAdvanced` ★核心
- `SetUnionControlNetType`
- `GetNode`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `ControlNetLoader`
- `Primitive string multiline [Crystools]`
- `DF_Get_image_size`
- `GetNode`
- `PreviewImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSizeAndCount`
- `DownloadAndLoadDepthAnythingV2Model`
- `ColorMatch`
- `easy batchAnything`
- `CR Seed`
- `VHS_VideoCombine`
- `GetNode`
- `LG_LoadImage`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `INTConstant`
- `ImageResizeKJv2`
- `GetNode`
- `easy clearCacheAll`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LG_ImageSender`
- `Switch image [Crystools]`
- `GetNode`
- `WanVaceToVideo`
- `GetNode`
- `GetNode`

## 关键参数

- `seed` = `49888161825358`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1.8000000000000003`

## 知识

覆盖率 **58%**（78/134）

**有卡**：`DiffusionModelSelector`、`VAEDecode`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`WanVaceToVideo`、`DWPreprocessor`、`GetImageSizeAndCount`、`DepthAnything_V2`、`KSamplerAdvanced`、`TrimVideoLatent`、`INTConstant`、`MathExpression|pysssss`、`GetImagesFromBatchIndexed`、`easy clearCacheAll`、`GetImageRangeFromBatch`、`ImageResizeKJv2`、`easy forLoopEnd`、`easy forLoopStart`、`VHS_VideoInfoLoaded`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`DiffusionModelLoaderKJ`、`Bjornulf_ShowInt`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`CFGNorm`、`ImageBatchGet`、`ImageScaleToTotalPixels`、`TextEncodeQwenImageEdit`、`ControlNetApplyAdvanced`、`SetUnionControlNetType`、`KSampler`、`VAEEncode`、`ControlNetLoader`、`Primitive string multiline [Crystools]`、`DF_Get_image_size`、`DownloadAndLoadDepthAnythingV2Model`、`ColorMatch`、`easy batchAnything`、`CR Seed`、`LG_LoadImage`、`VHS_LoadVideo`、`LG_ImageSender`、`Switch image [Crystools]`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、ControlNetApplyAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
