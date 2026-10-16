---
key: 视频生成/文生视频/AI帮你实现不一样的人生之旅！Wan2.2延长术生成长视频教程_1966178940819771393.json
name: AI帮你实现不一样的人生之旅！Wan2.2延长术生成长视频教程_1966178940819771393.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1966178940819771393.json
hash: e233e642d46b7310
coverage: 0.5
learned_at: 2026-10-15 22:43:45
nodes: [VAEDecode, easy forLoopEnd, GetNode, GetNode, GetNode, GetNode, SetNode, CLIPLoader, SetNode, VAELoader, ModelSamplingSD3, VAEDecode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, Label (rgthree), GetNode, GetImageSizeAndCount, CR Seed, GetNode, GetNode, SetNode, GetNode, PrimitiveInt, GetNode, GetNode, GetNode, GetNode, easy showAnything, MathExpression|pysssss, ImageFromBatch, ImageBatchMulti, VHS_VideoCombine, PrimitiveInt, GetNode, VHS_VideoCombine, KSamplerAdvanced, PrimitiveInt, PrimitiveInt, CR Seed, SetNode, Note, PathchSageAttentionKJ, UnetLoaderGGUF, wanBlockSwap, wanBlockSwap, UnetLoaderGGUF, PathchSageAttentionKJ, ModelSamplingSD3, TorchCompileModel, Label (rgthree), SetNode, Note, Note, TorchCompileModel, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, SetNode, SetNode, SetNode, Note, Note, MathExpression|pysssss, GetNode, GetNode, easy showAnything, CLIPTextEncode, MathExpression|pysssss, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, FromListGet1String, ShowText, GetNode, KSamplerAdvanced, GetNode, GetNode, ImageResizeKJv2, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), ImageResizeKJv2, string_util_StrSplit, CLIPTextEncode, PrimitiveStringMultiline, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageBatchMulti, PreviewImage, easy forLoopStart, SetNode, GetNode, PreviewImage, ImageFromBatch, SetNode, ImageFromBatch, SetNode, WanFirstLastFrameToVideo, ImageResizeKJv2, GetNode, WanFirstLastFrameToVideo, MathExpression|pysssss, PrimitiveInt, PrimitiveInt, GetImageRangeFromBatch, GetNode, PreviewImage, VHS_VideoCombine, UNETLoader, GetNode, GetNode, VHS_GetImageCount, GetNode, Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/AI帮你实现不一样的人生之旅！Wan2.2延长术生成长视频教程_1966178940819771393.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1966178940819771393.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（146 个）：
- `VAEDecode` ★核心
- `easy forLoopEnd`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `GetNode`
- `GetImageSizeAndCount`
- `CR Seed`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `MathExpression|pysssss`
- `ImageFromBatch`
- `ImageBatchMulti`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `GetNode`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `CR Seed`
- `SetNode`
- `Note`
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `UnetLoaderGGUF` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `TorchCompileModel`
- `Label (rgthree)`
- `SetNode`
- `Note`
- `Note`
- `TorchCompileModel`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `Note`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `FromListGet1String`
- `ShowText`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `string_util_StrSplit`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageBatchMulti`
- `PreviewImage`
- `easy forLoopStart`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `ImageFromBatch`
- `SetNode`
- `ImageFromBatch`
- `SetNode`
- `WanFirstLastFrameToVideo`
- `ImageResizeKJv2`
- `GetNode`
- `WanFirstLastFrameToVideo`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `PrimitiveInt`
- `GetImageRangeFromBatch`
- `GetNode`
- `PreviewImage`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `VHS_GetImageCount`
- `GetNode`
- `Label (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **50%**（73/146）

**有卡**：`VAEDecode`、`easy forLoopEnd`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`Label (rgthree)`、`GetImageSizeAndCount`、`CR Seed`、`MathExpression|pysssss`、`ImageFromBatch`、`ImageBatchMulti`、`VHS_VideoCombine`、`KSamplerAdvanced`、`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`wanBlockSwap`、`TorchCompileModel`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`FromListGet1String`、`ShowText`、`ImageResizeKJv2`、`LoadImage`、`string_util_StrSplit`、`easy forLoopStart`、`WanFirstLastFrameToVideo`、`GetImageRangeFromBatch`、`VHS_GetImageCount`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
