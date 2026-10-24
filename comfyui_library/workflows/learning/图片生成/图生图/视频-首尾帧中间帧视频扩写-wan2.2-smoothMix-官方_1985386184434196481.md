---
key: 图片生成/图生图/视频-首尾帧中间帧视频扩写-wan2.2-smoothMix-官方_1985386184434196481.json
name: 视频-首尾帧中间帧视频扩写-wan2.2-smoothMix-官方_1985386184434196481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/视频-首尾帧中间帧视频扩写-wan2.2-smoothMix-官方_1985386184434196481.json
hash: 82b86c98e47d2e0f
coverage: 0.654762
learned_at: 2026-10-23 13:25:59
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetNode, GetImageSizeAndCount, GetNode, GetNode, GetNode, ImageFromBatch, PreviewImage, PreviewImage, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, SetNode, SetNode, GetNode, GetImageSizeAndCount, SetNode, VHS_VideoCombine, CLIPLoader, VAELoader, StringFunction|pysssss, easy int, SetNode, StringFunction|pysssss, GetNode, GetImageSizeAndCount, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, ImageResizeKJ, GetNode, SetNode, ImageResizeKJ, SetNode, ImageLoader, GetNode, GetNode, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, GetNode, ColorMatch, GetImageSizeAndCount, easy positive, ImageConcanate, VHS_VideoCombine, MultiplePathsInput, ImageLoader, ImageLoader, WanVideoNAG, PathchSageAttentionKJ, LoraLoaderModelOnly, ImageConcatMulti, CLIPTextEncode, PathchSageAttentionKJ, easy positive, SetNode, SetNode, easy seed, SetNode, SetNode, PrimitiveFloat, easy int, ImpactFloat, SetNode, MathExpression|pysssss, Reroute, easy showAnything, MemoryCleaner, Qwen3_VQA, easy anythingIndexSwitch, GetImageSizeAndCount, GetImageSizeAndCount, GetImageSizeAndCount, WanFirstMiddleLastFrameToVideo, VAEDecodeTiled, ModelBlockSwap, ModelBlockSwap, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/视频-首尾帧中间帧视频扩写-wan2.2-smoothMix-官方_1985386184434196481.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/视频-首尾帧中间帧视频扩写-wan2.2-smoothMix-官方_1985386184434196481.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（84 个）：
- `easy showAnything`
- `easy imageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `PreviewImage`
- `PreviewImage`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `VHS_VideoCombine`
- `CLIPLoader`
- `VAELoader`
- `StringFunction|pysssss`
- `easy int`
- `SetNode`
- `StringFunction|pysssss`
- `GetNode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJ`
- `GetNode`
- `SetNode`
- `ImageResizeKJ`
- `SetNode`
- `ImageLoader`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `ColorMatch`
- `GetImageSizeAndCount`
- `easy positive`
- `ImageConcanate`
- `VHS_VideoCombine`
- `MultiplePathsInput`
- `ImageLoader`
- `ImageLoader`
- `WanVideoNAG`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ImageConcatMulti`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `easy positive`
- `SetNode`
- `SetNode`
- `easy seed`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `easy int`
- `ImpactFloat`
- `SetNode`
- `MathExpression|pysssss`
- `Reroute`
- `easy showAnything`
- `MemoryCleaner`
- `Qwen3_VQA`
- `easy anythingIndexSwitch`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `WanFirstMiddleLastFrameToVideo`
- `VAEDecodeTiled` ★核心
- `ModelBlockSwap`
- `ModelBlockSwap`
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **65%**（55/84）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`ImageFromBatch`、`VHS_VideoCombine`、`CLIPLoader`、`VAELoader`、`StringFunction|pysssss`、`easy int`、`ImageResizeKJ`、`ImageLoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`ColorMatch`、`easy positive`、`ImageConcanate`、`MultiplePathsInput`、`WanVideoNAG`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ImageConcatMulti`、`easy seed`、`ImpactFloat`、`MathExpression|pysssss`、`MemoryCleaner`、`Qwen3_VQA`、`easy anythingIndexSwitch`、`WanFirstMiddleLastFrameToVideo`、`VAEDecodeTiled`、`ModelBlockSwap`、`UNETLoader`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced、easy seed
