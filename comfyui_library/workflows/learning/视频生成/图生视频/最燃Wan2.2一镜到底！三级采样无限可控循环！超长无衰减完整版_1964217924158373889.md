---
key: 视频生成/图生视频/最燃Wan2.2一镜到底！三级采样无限可控循环！超长无衰减完整版_1964217924158373889.json
name: 最燃Wan2.2一镜到底！三级采样无限可控循环！超长无衰减完整版_1964217924158373889.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1964217924158373889.json
hash: 0eab6ba88566fffd
coverage: 0.457143
learned_at: 2026-10-15 22:31:34
nodes: [SetNode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), SetNode, GetNode, Label (rgthree), GetNode, GetNode, Note, UnetLoaderGGUF, wanBlockSwap, wanBlockSwap, UnetLoaderGGUF, Label (rgthree), CLIPTextEncode, SetNode, CLIPLoader, VAELoader, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, Note, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, PrimitiveInt, PrimitiveInt, SetNode, PrimitiveInt, PrimitiveFloat, PathchSageAttentionKJ, UNETLoader, Note, wanBlockSwap, ModelSamplingSD3, TorchCompileModel, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, GetNode, ImageFromBatch, LayerColor: BrightnessContrastV2, SetNode, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, wanBlockSwap, UNETLoader, TorchCompileModel, SetNode, Note, ImageBatchMulti, easy forLoopEnd, GetNode, VHS_VideoCombine, GetNode, Note, VHS_VideoCombine, Note, VHS_VideoCombine, GetNode, UpscalerTensorrt, LoadUpscalerTensorrtModel, GetNode, Fast Groups Bypasser (rgthree), RIFE VFI, MathExpression|pysssss, GetNode, MathExpression|pysssss, GetNode, ImageFromBatch, GetImageSizeAndCount, GetImageRangeFromBatch, VAEDecode, easy showAnything, easy forLoopStart, PreviewImage, easy showAnything, GetNode, SetNode, KSamplerAdvanced, GetNode, VHS_GetImageCount, CLIPTextEncode, SetNode, GetNode, CLIPTextEncode, SetNode, GetNode, Display Any (rgthree), Note, Note, CR Prompt List, GetNode, Note, MathExpression|pysssss, ImageResizeKJv2, CR Text, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced, PrimitiveInt, PrimitiveInt, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, WanImageToVideo, LoadImage, GetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, PrimitiveInt, PrimitiveStringMultiline, ImageColorMatch+, MathExpression|pysssss, PreviewImage, CR Seed, Note, Note, Note, Note, Note]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 4, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/最燃Wan2.2一镜到底！三级采样无限可控循环！超长无衰减完整版_1964217924158373889.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1964217924158373889.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（140 个）：
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `GetNode`
- `Label (rgthree)`
- `GetNode`
- `GetNode`
- `Note`
- `UnetLoaderGGUF` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `UnetLoaderGGUF` ★核心
- `Label (rgthree)`
- `CLIPTextEncode` ★核心
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `Note`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `TorchCompileModel`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `SetNode`
- `GetNode`
- `ImageFromBatch`
- `LayerColor: BrightnessContrastV2`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `wanBlockSwap`
- `UNETLoader` ★核心
- `TorchCompileModel`
- `SetNode`
- `Note`
- `ImageBatchMulti`
- `easy forLoopEnd`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `VHS_VideoCombine`
- `GetNode`
- `UpscalerTensorrt`
- `LoadUpscalerTensorrtModel`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `RIFE VFI`
- `MathExpression|pysssss`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `VAEDecode` ★核心
- `easy showAnything`
- `easy forLoopStart`
- `PreviewImage`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `VHS_GetImageCount`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `Display Any (rgthree)`
- `Note`
- `Note`
- `CR Prompt List`
- `GetNode`
- `Note`
- `MathExpression|pysssss`
- `ImageResizeKJv2`
- `CR Text`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `LoadImage`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `ImageColorMatch+`
- `MathExpression|pysssss`
- `PreviewImage`
- `CR Seed`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `4`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **46%**（64/140）

**有卡**：`Label (rgthree)`、`UnetLoaderGGUF`、`wanBlockSwap`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`UNETLoader`、`ModelSamplingSD3`、`TorchCompileModel`、`ImageFromBatch`、`LayerColor: BrightnessContrastV2`、`VAEDecode`、`ImageBatchMulti`、`easy forLoopEnd`、`UpscalerTensorrt`、`LoadUpscalerTensorrtModel`、`RIFE VFI`、`MathExpression|pysssss`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`easy forLoopStart`、`KSamplerAdvanced`、`VHS_GetImageCount`、`Display Any (rgthree)`、`CR Prompt List`、`ImageResizeKJv2`、`CR Text`、`WanImageToVideo`、`LoraLoaderModelOnly`、`LoadImage`、`ImageColorMatch+`、`CR Seed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
