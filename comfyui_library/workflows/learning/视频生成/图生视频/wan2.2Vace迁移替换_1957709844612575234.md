---
key: 视频生成/图生视频/wan2.2Vace迁移替换_1957709844612575234.json
name: wan2.2Vace迁移替换_1957709844612575234.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1957709844612575234.json
hash: dc8cd4a56b7ee211
coverage: 0.574194
learned_at: 2026-10-15 22:31:17
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, PrimitiveNode, Text Load Line From File, easy showAnything, VHS_GetImageCount, SetNode, SetNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, GetNode, GetNode, easy showAnything, VHS_GetImageCount, easy showAnything, GetNode, GetNode, Note, Note, Note, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoVACEStartToEndFrame, LayerUtility: PurgeVRAM, Reroute, SetNode, PreviewImage, GetNode, GetNode, GetImageRangeFromBatch, MathExpression|pysssss, easy forLoopStart, GetImageRangeFromBatch, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, GetNode, SetNode, TrimVideoLatent, LayerUtility: PurgeVRAM, KSamplerAdvanced, KSamplerAdvanced, GetNode, GetNode, easy cleanGpuUsed, WanVaceToVideo, GetNode, easy cleanGpuUsed, GetNode, MathExpression|pysssss, CLIPTextEncode, easy cleanGpuUsed, easy showAnything, VHS_GetImageCount, CLIPLoader, SetNode, SetNode, ModelSamplingSD3, SetNode, ModelSamplingSD3, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, Text Load Line From File, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ModelPatchTorchSettings, WanVaceToVideo, TrimVideoLatent, VAEDecode, SetNode, Reroute, EsesImageEffectLevels, Fast Groups Bypasser (rgthree), VAEDecode, MathExpression|pysssss, ImageResizeKJv2, easy seed, GetNode, GetNode, MathExpression|pysssss, MathExpression|pysssss, INTConstant, SetNode, FloatConstant, AIO_Preprocessor, DWPreprocessor, EsesImageEffectLevels, SetNode, CR Image Input Switch (4 way), ImageFromBatch, ImageBatchMulti, easy forLoopEnd, LayerUtility: PurgeVRAM, easy int, MathExpression|pysssss, PathchSageAttentionKJ, WanVideoVACEStartToEndFrame, ModelPatchTorchSettings, SetNode, CLIPTextEncode, ImageResizeKJv2, ImageBlend, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, easy int, KSamplerAdvanced, GetNode, KSamplerAdvanced, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, INTConstant, ImageResizeKJv2, INTConstant, INTConstant, INTConstant, PathchSageAttentionKJ, VHS_VideoCombine, LoadImage, LoadImage, PrimitiveStringMultiline, LoadAndResizeImage, UnetLoaderGGUF, UnetLoaderGGUF, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, VHS_LoadVideo, GetNode, VAELoader, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "sa_solver", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2Vace迁移替换_1957709844612575234.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957709844612575234.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（155 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `Text Load Line From File`
- `easy showAnything`
- `VHS_GetImageCount`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `VHS_GetImageCount`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `Note`
- `Note`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVACEStartToEndFrame`
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `MathExpression|pysssss`
- `easy forLoopStart`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `SetNode`
- `TrimVideoLatent`
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVaceToVideo`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `easy showAnything`
- `VHS_GetImageCount`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `SetNode`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `Text Load Line From File`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ModelPatchTorchSettings`
- `WanVaceToVideo`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `SetNode`
- `Reroute`
- `EsesImageEffectLevels`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `MathExpression|pysssss`
- `ImageResizeKJv2`
- `easy seed`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `INTConstant`
- `SetNode`
- `FloatConstant`
- `AIO_Preprocessor`
- `DWPreprocessor`
- `EsesImageEffectLevels`
- `SetNode`
- `CR Image Input Switch (4 way)`
- `ImageFromBatch`
- `ImageBatchMulti`
- `easy forLoopEnd`
- `LayerUtility: PurgeVRAM`
- `easy int`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `WanVideoVACEStartToEndFrame`
- `ModelPatchTorchSettings`
- `SetNode`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `ImageBlend`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy int`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `INTConstant`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadAndResizeImage`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `VHS_LoadVideo`
- `GetNode`
- `VAELoader`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `sa_solver`
- `denoise` = `beta`

## 知识

覆盖率 **57%**（89/155）

**有卡**：`CLIPTextEncode`、`Text Load Line From File`、`VHS_GetImageCount`、`MathExpression|pysssss`、`WanVideoVACEStartToEndFrame`、`LayerUtility: PurgeVRAM`、`GetImageRangeFromBatch`、`easy forLoopStart`、`TrimVideoLatent`、`KSamplerAdvanced`、`easy cleanGpuUsed`、`WanVaceToVideo`、`CLIPLoader`、`ModelSamplingSD3`、`ModelPatchTorchSettings`、`VAEDecode`、`EsesImageEffectLevels`、`ImageResizeKJv2`、`easy seed`、`INTConstant`、`FloatConstant`、`AIO_Preprocessor`、`DWPreprocessor`、`CR Image Input Switch (4 way)`、`ImageFromBatch`、`ImageBatchMulti`、`easy forLoopEnd`、`easy int`、`PathchSageAttentionKJ`、`ImageBlend`、`VHS_VideoCombine`、`LoadImage`、`LoadAndResizeImage`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`VHS_LoadVideo`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、easy seed
