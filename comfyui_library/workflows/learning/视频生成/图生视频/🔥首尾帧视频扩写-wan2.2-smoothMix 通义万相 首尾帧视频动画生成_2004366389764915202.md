---
key: 视频生成/图生视频/🔥首尾帧视频扩写-wan2.2-smoothMix 通义万相 首尾帧视频动画生成_2004366389764915202.json
name: 🔥首尾帧视频扩写-wan2.2-smoothMix 通义万相 首尾帧视频动画生成_2004366389764915202.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2004366389764915202.json
hash: 5d65cf533d10758a
coverage: 0.647887
learned_at: 2026-10-15 22:33:54
nodes: [easy imageSize, GetImageSizeAndCount, ImageResizeKJ, GetNode, GetNode, GetNode, GetNode, PreviewImage, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetImageSizeAndCount, GetImageSizeAndCount, CLIPLoader, VAELoader, StringFunction|pysssss, LayerUtility: ImageScaleByAspectRatio V2, Reroute, PathchSageAttentionKJ, WanVideoNAG, UNETLoader, UNETLoader, ModelBlockSwap, GetImageSizeAndCount, GetImageSizeAndCount, SetNode, ImageLoader, GetImageSizeAndCount, SetNode, ImageLoader, easy positive, PrimitiveFloat, easy int, SetNode, MathExpression|pysssss, ImpactFloat, easy int, SetNode, SetNode, easy seed, easy positive, GetNode, Qwen3_VQA, MultiplePathsInput, easy anythingIndexSwitch, easy showAnything, MemoryCleaner, StringFunction|pysssss, SetNode, SetNode, GetImageSizeAndCount, SetNode, GetImageSizeAndCount, PreviewImage, ImageFromBatch, SetNode, ModelBlockSwap, CLIPTextEncode, CLIPTextEncode, WanFirstLastFrameToVideo, INTConstant, PathchSageAttentionKJ, WanMoeKSampler, VAEDecodeTiled, GetImageSizeAndCount, VHS_VideoCombine, GetNode, easy showAnything, GetNode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "sa_solver", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/🔥首尾帧视频扩写-wan2.2-smoothMix 通义万相 首尾帧视频动画生成_2004366389764915202.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2004366389764915202.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `easy imageSize`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `CLIPLoader`
- `VAELoader`
- `StringFunction|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `PathchSageAttentionKJ`
- `WanVideoNAG`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelBlockSwap`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `SetNode`
- `ImageLoader`
- `GetImageSizeAndCount`
- `SetNode`
- `ImageLoader`
- `easy positive`
- `PrimitiveFloat`
- `easy int`
- `SetNode`
- `MathExpression|pysssss`
- `ImpactFloat`
- `easy int`
- `SetNode`
- `SetNode`
- `easy seed`
- `easy positive`
- `GetNode`
- `Qwen3_VQA`
- `MultiplePathsInput`
- `easy anythingIndexSwitch`
- `easy showAnything`
- `MemoryCleaner`
- `StringFunction|pysssss`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `ImageFromBatch`
- `SetNode`
- `ModelBlockSwap`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `INTConstant`
- `PathchSageAttentionKJ`
- `WanMoeKSampler` ★核心
- `VAEDecodeTiled` ★核心
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `sa_solver`

## 知识

覆盖率 **65%**（46/71）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`ImageResizeKJ`、`CLIPLoader`、`VAELoader`、`StringFunction|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`PathchSageAttentionKJ`、`WanVideoNAG`、`UNETLoader`、`ModelBlockSwap`、`ImageLoader`、`easy positive`、`easy int`、`MathExpression|pysssss`、`ImpactFloat`、`easy seed`、`Qwen3_VQA`、`MultiplePathsInput`、`easy anythingIndexSwitch`、`MemoryCleaner`、`ImageFromBatch`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`INTConstant`、`WanMoeKSampler`、`VAEDecodeTiled`、`VHS_VideoCombine`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、WanMoeKSampler、easy seed、VAEDecodeTiled
