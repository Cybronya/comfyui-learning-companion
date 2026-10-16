---
key: 视频生成/图生视频/Wan2.2图生视频无限版_1967394231394373634.json
name: Wan2.2图生视频无限版_1967394231394373634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1967394231394373634.json
hash: 8a19baade8696d00
coverage: 0.495575
learned_at: 2026-10-15 22:31:41
nodes: [SetNode, UNETLoader, TorchCompileModel, PathchSageAttentionKJ, ModelSamplingSD3, LoraLoaderModelOnly, UNETLoader, TorchCompileModel, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingSD3, GetNode, KSamplerAdvanced, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, KSamplerAdvanced, KSamplerAdvanced, WanImageToVideo, SetNode, VAEDecode, SetNode, ImpactInt, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, CLIPLoader, SetNode, VAELoader, CLIPTextEncode, SetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SetNode, LayerColor: BrightnessContrastV2, GetImageRangeFromBatch, Label (rgthree), KSamplerAdvanced, KSamplerAdvanced, SetNode, GetNode, GetNode, PrimitiveInt, easy seed, GetNode, GetNode, GetNode, GetNode, MathExpression|pysssss, GetNode, GetNode, VHS_GetImageCount, ImageFromBatch, GetNode, GetNode, PrimitiveInt, CR Seed, KSamplerAdvanced, GetNode, WanImageToVideo, GetNode, GetNode, GetNode, MathExpression|pysssss, GetImageSizeAndCount, Note, easy showAnything, easy showAnything, VAEDecode, MathExpression|pysssss, SetNode, GetNode, Note, GetNode, easy forLoopEnd, ImageBatchMulti, PrimitiveFloat, ImpactInt, ImpactInt, Fast Groups Bypasser (rgthree), ImageResizeKJv2, GetImageRangeFromBatch, RIFE VFI, ImpactInt, MathExpression|pysssss, GetNode, GetNode, Text Multiline, PreviewImage, Text Concatenate, easy showAnything, RH_Captioner, CLIPTextEncode, VHS_VideoCombine, LoadImage, easy promptLine, easy forLoopStart, easy showAnything, RH_Captioner, easy showAnything, CLIPTextEncode, VHS_VideoCombine, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2图生视频无限版_1967394231394373634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967394231394373634.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（113 个）：
- `SetNode`
- `UNETLoader` ★核心
- `TorchCompileModel`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `TorchCompileModel`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `ImpactInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SetNode`
- `LayerColor: BrightnessContrastV2`
- `GetImageRangeFromBatch`
- `Label (rgthree)`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `easy seed`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `VHS_GetImageCount`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `CR Seed`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `WanImageToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `GetImageSizeAndCount`
- `Note`
- `easy showAnything`
- `easy showAnything`
- `VAEDecode` ★核心
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `Note`
- `GetNode`
- `easy forLoopEnd`
- `ImageBatchMulti`
- `PrimitiveFloat`
- `ImpactInt`
- `ImpactInt`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `GetImageRangeFromBatch`
- `RIFE VFI`
- `ImpactInt`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `Text Multiline`
- `PreviewImage`
- `Text Concatenate`
- `easy showAnything`
- `RH_Captioner`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `easy promptLine`
- `easy forLoopStart`
- `easy showAnything`
- `RH_Captioner`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **50%**（56/113）

**有卡**：`UNETLoader`、`TorchCompileModel`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`WanImageToVideo`、`VAEDecode`、`ImpactInt`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerColor: BrightnessContrastV2`、`GetImageRangeFromBatch`、`Label (rgthree)`、`easy seed`、`MathExpression|pysssss`、`VHS_GetImageCount`、`ImageFromBatch`、`CR Seed`、`GetImageSizeAndCount`、`easy forLoopEnd`、`ImageBatchMulti`、`ImageResizeKJv2`、`RIFE VFI`、`Text Multiline`、`Text Concatenate`、`RH_Captioner`、`VHS_VideoCombine`、`LoadImage`、`easy promptLine`、`easy forLoopStart`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
