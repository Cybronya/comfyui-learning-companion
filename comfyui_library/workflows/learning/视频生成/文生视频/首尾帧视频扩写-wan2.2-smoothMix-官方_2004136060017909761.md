---
key: 视频生成/文生视频/首尾帧视频扩写-wan2.2-smoothMix-官方_2004136060017909761.json
name: 首尾帧视频扩写-wan2.2-smoothMix-官方_2004136060017909761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/首尾帧视频扩写-wan2.2-smoothMix-官方_2004136060017909761.json
hash: 0028a2e9ab8f356b
coverage: 0.647887
learned_at: 2026-10-15 22:49:07
nodes: [GetImageSizeAndCount, VAEDecodeTiled, CLIPTextEncode, GetNode, GetNode, GetImageSizeAndCount, VHS_VideoCombine, GetNode, SetNode, GetNode, GetNode, CLIPTextEncode, GetImageSizeAndCount, GetImageSizeAndCount, WanFirstLastFrameToVideo, easy seed, INTConstant, CLIPLoader, VAELoader, GetImageSizeAndCount, SetNode, SetNode, ImpactFloat, MathExpression|pysssss, SetNode, SetNode, Reroute, PathchSageAttentionKJ, WanMoeKSampler, WanVideoNAG, PathchSageAttentionKJ, UNETLoader, UNETLoader, ModelBlockSwap, ModelBlockSwap, GetNode, MultiplePathsInput, easy anythingIndexSwitch, easy showAnything, MemoryCleaner, StringFunction|pysssss, Qwen3_VQA, StringFunction|pysssss, easy positive, GetNode, SetNode, ImageLoader, easy positive, PrimitiveFloat, easy int, GetNode, easy showAnything, GetImageSizeAndCount, GetImageSizeAndCount, easy imageSize, VHS_VideoCombine, easy int, ImageLoader, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, ImageResizeKJ, PreviewImage, SetNode, GetImageSizeAndCount, SetNode, GetImageSizeAndCount, ImageFromBatch, PreviewImage, SetNode]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "sa_solver", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/文生视频/首尾帧视频扩写-wan2.2-smoothMix-官方_2004136060017909761.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/首尾帧视频扩写-wan2.2-smoothMix-官方_2004136060017909761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `GetImageSizeAndCount`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `WanFirstLastFrameToVideo`
- `easy seed`
- `INTConstant`
- `CLIPLoader`
- `VAELoader`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `ImpactFloat`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `Reroute`
- `PathchSageAttentionKJ`
- `WanMoeKSampler` ★核心
- `WanVideoNAG`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelBlockSwap`
- `ModelBlockSwap`
- `GetNode`
- `MultiplePathsInput`
- `easy anythingIndexSwitch`
- `easy showAnything`
- `MemoryCleaner`
- `StringFunction|pysssss`
- `Qwen3_VQA`
- `StringFunction|pysssss`
- `easy positive`
- `GetNode`
- `SetNode`
- `ImageLoader`
- `easy positive`
- `PrimitiveFloat`
- `easy int`
- `GetNode`
- `easy showAnything`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `easy imageSize`
- `VHS_VideoCombine`
- `easy int`
- `ImageLoader`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `PreviewImage`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `PreviewImage`
- `SetNode`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `sa_solver`

## 知识

覆盖率 **65%**（46/71）

**有卡**：`GetImageSizeAndCount`、`VAEDecodeTiled`、`CLIPTextEncode`、`VHS_VideoCombine`、`WanFirstLastFrameToVideo`、`easy seed`、`INTConstant`、`CLIPLoader`、`VAELoader`、`ImpactFloat`、`MathExpression|pysssss`、`PathchSageAttentionKJ`、`WanMoeKSampler`、`WanVideoNAG`、`UNETLoader`、`ModelBlockSwap`、`MultiplePathsInput`、`easy anythingIndexSwitch`、`MemoryCleaner`、`StringFunction|pysssss`、`Qwen3_VQA`、`easy positive`、`ImageLoader`、`easy int`、`easy imageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJ`、`ImageFromBatch`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、WanMoeKSampler、easy seed、VAEDecodeTiled
