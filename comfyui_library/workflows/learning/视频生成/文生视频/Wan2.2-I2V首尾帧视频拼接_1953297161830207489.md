---
key: 视频生成/文生视频/Wan2.2-I2V首尾帧视频拼接_1953297161830207489.json
name: Wan2.2-I2V首尾帧视频拼接_1953297161830207489.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1953297161830207489.json
hash: 0deb90bdd28a297e
coverage: 0.576923
learned_at: 2026-10-15 22:43:38
nodes: [SetNode, SetNode, GetNode, INTConstant, INTConstant, CLIPTextEncode, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, SetNode, ModelSamplingSD3, SetNode, CLIPLoader, TrimVideoLatent, GetNode, GetNode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, TrimVideoLatent, VAEDecode, GetNode, easy cleanGpuUsed, easy int, GetNode, VAEDecode, SetNode, VHS_VideoCombine, RIFE VFI, LayerFilter: AddGrain, Image Levels Adjustment, LayerUtility: PurgeVRAM, Reroute, INTConstant, CLIPVisionEncode, GetImageRangeFromBatch, FloatConstant, INTConstant, SetNode, SetNode, SetNode, CLIPTextEncode, KSamplerAdvanced, GetNode, PrimitiveNode, VHS_GetImageCount, ImageResizeKJv2, SetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, GetNode, GetNode, VHS_VideoCombine, LayerUtility: PurgeVRAM, MathExpression|pysssss, GetImageRangeFromBatch, MathExpression|pysssss, VHS_GetImageCount, PrimitiveNode, WanImageToVideo, KSamplerAdvanced, GetNode, CLIPVisionLoader, GetNode, easy cleanGpuUsed, GetNode, GetNode, CLIPTextEncode, VHS_GetImageCount, easy showAnything, GetNode, GetNode, GetNode, GetNode, GetNode, WanFirstLastFrameToVideo, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, KSamplerAdvanced, VHS_VideoCombine, SetNode, easy int, KSamplerAdvanced, GetNode, GetNode, GetNode, ImageBatchMulti, PreviewImage, ImageFromBatch, ImageFromBatch, SetNode, SetNode, PreviewImage, LoraLoaderModelOnly, LoraLoaderModelOnly, easy seed, VHS_LoadVideo, VHS_LoadVideo, UnetLoaderGGUF, UnetLoaderGGUF, VAELoader, LoadAndResizeImage, Fast Groups Bypasser (rgthree), CR Text]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2-I2V首尾帧视频拼接_1953297161830207489.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1953297161830207489.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（130 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `SetNode`
- `CLIPLoader`
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `GetNode`
- `easy cleanGpuUsed`
- `easy int`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `VHS_VideoCombine`
- `RIFE VFI`
- `LayerFilter: AddGrain`
- `Image Levels Adjustment`
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `INTConstant`
- `CLIPVisionEncode`
- `GetImageRangeFromBatch`
- `FloatConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `PrimitiveNode`
- `VHS_GetImageCount`
- `ImageResizeKJv2`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `MathExpression|pysssss`
- `GetImageRangeFromBatch`
- `MathExpression|pysssss`
- `VHS_GetImageCount`
- `PrimitiveNode`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `VHS_GetImageCount`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanFirstLastFrameToVideo`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `easy int`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBatchMulti`
- `PreviewImage`
- `ImageFromBatch`
- `ImageFromBatch`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy seed`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `VAELoader`
- `LoadAndResizeImage`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **58%**（75/130）

**有卡**：`INTConstant`、`CLIPTextEncode`、`ImageResizeKJv2`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`TrimVideoLatent`、`LayerUtility: PurgeVRAM`、`easy cleanGpuUsed`、`VAEDecode`、`easy int`、`VHS_VideoCombine`、`RIFE VFI`、`LayerFilter: AddGrain`、`Image Levels Adjustment`、`CLIPVisionEncode`、`GetImageRangeFromBatch`、`FloatConstant`、`KSamplerAdvanced`、`VHS_GetImageCount`、`MathExpression|pysssss`、`WanImageToVideo`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`VHS_LoadVideo`、`ImageBatchMulti`、`ImageFromBatch`、`LoraLoaderModelOnly`、`easy seed`、`UnetLoaderGGUF`、`VAELoader`、`LoadAndResizeImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、KSamplerAdvanced、easy seed、CLIPVisionEncode
