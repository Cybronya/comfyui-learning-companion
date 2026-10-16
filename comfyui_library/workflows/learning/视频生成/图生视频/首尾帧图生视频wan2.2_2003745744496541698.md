---
key: 视频生成/图生视频/首尾帧图生视频wan2.2_2003745744496541698.json
name: 首尾帧图生视频wan2.2_2003745744496541698.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2003745744496541698.json
hash: 9c598d44baf679c4
coverage: 0.647887
learned_at: 2026-10-15 22:33:52
nodes: [easy anythingIndexSwitch, StringFunction|pysssss, SetNode, MemoryCleaner, GetImageSizeAndCount, MathExpression|pysssss, easy int, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, Reroute, GetImageSizeAndCount, GetImageSizeAndCount, CLIPTextEncode, WanFirstLastFrameToVideo, GetImageSizeAndCount, ImageFromBatch, PathchSageAttentionKJ, SetNode, INTConstant, PathchSageAttentionKJ, ModelBlockSwap, ModelBlockSwap, WanMoeKSampler, WanVideoNAG, VAEDecodeTiled, GetImageSizeAndCount, easy seed, easy int, SetNode, SetNode, SetNode, PreviewImage, GetImageSizeAndCount, SetNode, GetImageSizeAndCount, ImageResizeKJ, ImpactFloat, GetImageSizeAndCount, SetNode, easy showAnything, PreviewImage, StringFunction|pysssss, SetNode, Qwen3_VQA, GetNode, easy positive, MultiplePathsInput, ImageLoader, ImageLoader, PrimitiveFloat, VHS_VideoCombine, UNETLoader, GetNode, GetImageSizeAndCount, GetImageSizeAndCount, easy imageSize, GetNode, easy showAnything, VHS_VideoCombine, easy positive]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "sa_solver", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧图生视频wan2.2_2003745744496541698.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2003745744496541698.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `easy anythingIndexSwitch`
- `StringFunction|pysssss`
- `SetNode`
- `MemoryCleaner`
- `GetImageSizeAndCount`
- `MathExpression|pysssss`
- `easy int`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `PathchSageAttentionKJ`
- `SetNode`
- `INTConstant`
- `PathchSageAttentionKJ`
- `ModelBlockSwap`
- `ModelBlockSwap`
- `WanMoeKSampler` ★核心
- `WanVideoNAG`
- `VAEDecodeTiled` ★核心
- `GetImageSizeAndCount`
- `easy seed`
- `easy int`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetImageSizeAndCount`
- `SetNode`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `ImpactFloat`
- `GetImageSizeAndCount`
- `SetNode`
- `easy showAnything`
- `PreviewImage`
- `StringFunction|pysssss`
- `SetNode`
- `Qwen3_VQA`
- `GetNode`
- `easy positive`
- `MultiplePathsInput`
- `ImageLoader`
- `ImageLoader`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `GetNode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `easy imageSize`
- `GetNode`
- `easy showAnything`
- `VHS_VideoCombine`
- `easy positive`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `sa_solver`

## 知识

覆盖率 **65%**（46/71）

**有卡**：`easy anythingIndexSwitch`、`StringFunction|pysssss`、`MemoryCleaner`、`GetImageSizeAndCount`、`MathExpression|pysssss`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`WanFirstLastFrameToVideo`、`ImageFromBatch`、`PathchSageAttentionKJ`、`INTConstant`、`ModelBlockSwap`、`WanMoeKSampler`、`WanVideoNAG`、`VAEDecodeTiled`、`easy seed`、`ImageResizeKJ`、`ImpactFloat`、`Qwen3_VQA`、`easy positive`、`MultiplePathsInput`、`ImageLoader`、`VHS_VideoCombine`、`easy imageSize`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、WanMoeKSampler、easy seed、VAEDecodeTiled
