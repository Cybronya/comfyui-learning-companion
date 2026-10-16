---
key: 视频生成/图生视频/wan2.2-视频-图生视频扩写_2043579993401335809.json
name: wan2.2-视频-图生视频扩写_2043579993401335809.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2043579993401335809.json
hash: 8f9ac1b8a34d102a
coverage: 0.652174
learned_at: 2026-10-15 22:36:32
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetNode, SetNode, GetNode, PathchSageAttentionKJ, GetNode, SetNode, PathchSageAttentionKJ, PreviewImage, ImageFromBatch, VAEDecodeTiled, GetImageSizeAndCount, PreviewImage, INTConstant, VHS_VideoCombine, WanVideoVACEStartToEndFrame, GetImageSizeAndCount, SetNode, easy seed, CLIPLoader, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, VAELoader, GetImageSizeAndCount, WanImageToVideo, WanMoeKSampler, GetNode, ShowText|pysssss, GetImageSizeAndCount, GetNode, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, UNETLoader, GetImageSizeAndCount, GetImageSizeAndCount, ImageFromBatch+, StringFunction|pysssss, StringFunction|pysssss, GetNode, GetNode, VHS_VideoCombine, easy positive, ImpactFloat, SetNode, SetNode, easy int, easy positive, easy int, GetImageSizeAndCount, SetNode, MathExpression|pysssss, PrimitiveFloat, Qwen3_VQA, easy anythingIndexSwitch, easy showAnything, MemoryCleaner, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Reroute, ModelBlockSwap, ModelBlockSwap, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "sa_solver", "sampler_name": 1.5, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2-视频-图生视频扩写_2043579993401335809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043579993401335809.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `easy showAnything`
- `easy imageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `GetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `ImageFromBatch`
- `VAEDecodeTiled` ★核心
- `GetImageSizeAndCount`
- `PreviewImage`
- `INTConstant`
- `VHS_VideoCombine`
- `WanVideoVACEStartToEndFrame`
- `GetImageSizeAndCount`
- `SetNode`
- `easy seed`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `GetImageSizeAndCount`
- `WanImageToVideo`
- `WanMoeKSampler` ★核心
- `GetNode`
- `ShowText|pysssss`
- `GetImageSizeAndCount`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `StringFunction|pysssss`
- `StringFunction|pysssss`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `easy positive`
- `ImpactFloat`
- `SetNode`
- `SetNode`
- `easy int`
- `easy positive`
- `easy int`
- `GetImageSizeAndCount`
- `SetNode`
- `MathExpression|pysssss`
- `PrimitiveFloat`
- `Qwen3_VQA`
- `easy anythingIndexSwitch`
- `easy showAnything`
- `MemoryCleaner`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `ModelBlockSwap`
- `ModelBlockSwap`
- `LoadImage`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1.5`
- `scheduler` = `1`
- `denoise` = `sa_solver`

## 知识

覆盖率 **65%**（45/69）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`PathchSageAttentionKJ`、`ImageFromBatch`、`VAEDecodeTiled`、`INTConstant`、`VHS_VideoCombine`、`WanVideoVACEStartToEndFrame`、`easy seed`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`WanImageToVideo`、`WanMoeKSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`ImageFromBatch+`、`StringFunction|pysssss`、`easy positive`、`ImpactFloat`、`easy int`、`MathExpression|pysssss`、`Qwen3_VQA`、`easy anythingIndexSwitch`、`MemoryCleaner`、`LoraLoaderModelOnly`、`ModelBlockSwap`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、easy seed
