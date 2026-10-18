---
key: 视频生成/图生视频/视频-首尾帧视频扩写(动漫)-wan2.2-DasiwaV10-官方_2008209726496051201.json
name: 视频-首尾帧视频扩写(动漫)-wan2.2-DasiwaV10-官方_2008209726496051201.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频-首尾帧视频扩写(动漫)-wan2.2-DasiwaV10-官方_2008209726496051201.json
hash: 76f5f0e933d5d8f6
coverage: 0.653333
learned_at: 2026-10-15 22:34:06
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetNode, GetImageSizeAndCount, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, ImageFromBatch, PreviewImage, PreviewImage, GetImageSizeAndCount, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, CLIPTextEncode, GetImageSizeAndCount, WanFirstLastFrameToVideo, VHS_VideoCombine, easy seed, INTConstant, CLIPLoader, VAELoader, easy int, SetNode, StringFunction|pysssss, LayerUtility: ImageScaleByAspectRatio V2, SetNode, MemoryCleaner, SetNode, PrimitiveFloat, ImpactFloat, MathExpression|pysssss, SetNode, SetNode, Reroute, PathchSageAttentionKJ, WanVideoNAG, PathchSageAttentionKJ, ModelBlockSwap, ModelBlockSwap, WanMoeKSampler, ImageLoader, easy int, easy showAnything, ImageLoader, easy positive, GetNode, StringFunction|pysssss, GetImageSizeAndCount, GetImageSizeAndCount, RH_LLMAPI_NODE, MultiplePathsInput, Qwen3_VQA, VHS_VideoCombine, VAEDecodeTiled, GetImageSizeAndCount, GetImageSizeAndCount, GetImageSizeAndCount, SetNode, ImageResizeKJ, GetImageSizeAndCount, PreviewImage, ImageConcanate, ImageConcanate, easy positive, easy anythingIndexSwitch, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "sa_solver", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/视频-首尾帧视频扩写(动漫)-wan2.2-DasiwaV10-官方_2008209726496051201.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008209726496051201.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `easy showAnything`
- `easy imageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `PreviewImage`
- `PreviewImage`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetImageSizeAndCount`
- `WanFirstLastFrameToVideo`
- `VHS_VideoCombine`
- `easy seed`
- `INTConstant`
- `CLIPLoader`
- `VAELoader`
- `easy int`
- `SetNode`
- `StringFunction|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `MemoryCleaner`
- `SetNode`
- `PrimitiveFloat`
- `ImpactFloat`
- `MathExpression|pysssss`
- `SetNode`
- `SetNode`
- `Reroute`
- `PathchSageAttentionKJ`
- `WanVideoNAG`
- `PathchSageAttentionKJ`
- `ModelBlockSwap`
- `ModelBlockSwap`
- `WanMoeKSampler` ★核心
- `ImageLoader`
- `easy int`
- `easy showAnything`
- `ImageLoader`
- `easy positive`
- `GetNode`
- `StringFunction|pysssss`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `RH_LLMAPI_NODE`
- `MultiplePathsInput`
- `Qwen3_VQA`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `SetNode`
- `ImageResizeKJ`
- `GetImageSizeAndCount`
- `PreviewImage`
- `ImageConcanate`
- `ImageConcanate`
- `easy positive`
- `easy anythingIndexSwitch`
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `sa_solver`

## 知识

覆盖率 **65%**（49/75）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`CLIPTextEncode`、`ImageFromBatch`、`WanFirstLastFrameToVideo`、`VHS_VideoCombine`、`easy seed`、`INTConstant`、`CLIPLoader`、`VAELoader`、`easy int`、`StringFunction|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`MemoryCleaner`、`ImpactFloat`、`MathExpression|pysssss`、`PathchSageAttentionKJ`、`WanVideoNAG`、`ModelBlockSwap`、`WanMoeKSampler`、`ImageLoader`、`easy positive`、`RH_LLMAPI_NODE`、`MultiplePathsInput`、`Qwen3_VQA`、`VAEDecodeTiled`、`ImageResizeKJ`、`ImageConcanate`、`easy anythingIndexSwitch`、`UNETLoader`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、WanMoeKSampler、easy seed、VAEDecodeTiled
