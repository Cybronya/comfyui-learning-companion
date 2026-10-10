---
key: 视频生成/文生视频/首尾帧视频扩写-wan2.2-smoothMix-官方_2004136060017909761.json
name: 首尾帧视频扩写-wan2.2-smoothMix-官方_2004136060017909761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/首尾帧视频扩写-wan2.2-smoothMix-官方_2004136060017909761.json
hash: 0028a2e9ab8f356b
coverage: 0.492958
learned_at: 2026-10-11 02:57:41
nodes: [GetImageSizeAndCount, VAEDecodeTiled, CLIPTextEncode, GetNode, GetNode, GetImageSizeAndCount, VHS_VideoCombine, GetNode, SetNode, GetNode, GetNode, CLIPTextEncode, GetImageSizeAndCount, GetImageSizeAndCount, WanFirstLastFrameToVideo, easy seed, INTConstant, CLIPLoader, VAELoader, GetImageSizeAndCount, SetNode, SetNode, ImpactFloat, MathExpression|pysssss, SetNode, SetNode, Reroute, PathchSageAttentionKJ, WanMoeKSampler, WanVideoNAG, PathchSageAttentionKJ, UNETLoader, UNETLoader, ModelBlockSwap, ModelBlockSwap, GetNode, MultiplePathsInput, easy anythingIndexSwitch, easy showAnything, MemoryCleaner, StringFunction|pysssss, Qwen3_VQA, StringFunction|pysssss, easy positive, GetNode, SetNode, ImageLoader, easy positive, PrimitiveFloat, easy int, GetNode, easy showAnything, GetImageSizeAndCount, GetImageSizeAndCount, easy imageSize, VHS_VideoCombine, easy int, ImageLoader, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, ImageResizeKJ, PreviewImage, SetNode, GetImageSizeAndCount, SetNode, GetImageSizeAndCount, ImageFromBatch, PreviewImage, SetNode]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, StringFunction|pysssss, StringFunction|pysssss, easy anythingIndexSwitch, easy int, easy int, easy positive, easy positive, easy imageSize, easy seed]
parameters: {"cfg": 20, "denoise": "sa_solver", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **49%**（35/71）

**有卡**：`GetImageSizeAndCount`、`VAEDecodeTiled`、`CLIPTextEncode`、`VHS_VideoCombine`、`WanFirstLastFrameToVideo`、`INTConstant`、`CLIPLoader`、`VAELoader`、`ImpactFloat`、`PathchSageAttentionKJ`、`WanMoeKSampler`、`WanVideoNAG`、`UNETLoader`、`ModelBlockSwap`、`MultiplePathsInput`、`MemoryCleaner`、`Qwen3_VQA`、`ImageLoader`、`ImageResizeKJ`、`ImageFromBatch`

**缺卡**（11）：`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`StringFunction|pysssss`、`StringFunction|pysssss`、`easy anythingIndexSwitch`、`easy int`、`easy int`、`easy positive`、`easy positive`、`easy imageSize`、`easy seed`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、WanMoeKSampler、VAEDecodeTiled、GetImageSizeAndCount、ImageResizeKJ

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
