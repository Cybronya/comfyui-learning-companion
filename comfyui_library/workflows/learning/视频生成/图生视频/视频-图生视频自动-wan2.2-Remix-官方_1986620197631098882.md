---
key: 视频生成/图生视频/视频-图生视频自动-wan2.2-Remix-官方_1986620197631098882.json
name: 视频-图生视频自动-wan2.2-Remix-官方_1986620197631098882.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频-图生视频自动-wan2.2-Remix-官方_1986620197631098882.json
hash: 9db034712a9c4ea7
coverage: 0.647059
learned_at: 2026-10-15 22:32:55
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetNode, SetNode, GetNode, GetNode, SetNode, PathchSageAttentionKJ, PreviewImage, ImageFromBatch, VAEDecodeTiled, GetImageSizeAndCount, PreviewImage, INTConstant, VHS_VideoCombine, WanVideoVACEStartToEndFrame, GetImageSizeAndCount, SetNode, easy seed, CLIPLoader, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, VAELoader, WanImageToVideo, GetNode, ShowText|pysssss, GetImageSizeAndCount, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, GetImageSizeAndCount, GetImageSizeAndCount, ImageFromBatch+, StringFunction|pysssss, StringFunction|pysssss, GetNode, GetNode, VHS_VideoCombine, easy positive, WanMoeKSampler, GetImageSizeAndCount, ImpactFloat, easy int, GetImageSizeAndCount, SetNode, SetNode, easy positive, easy showAnything, MemoryCleaner, easy anythingIndexSwitch, UNETLoader, CLIPVisionLoader, CLIPVisionEncode, UNETLoader, PathchSageAttentionKJ, Reroute, SetNode, MathExpression|pysssss, PrimitiveFloat, easy int, Qwen3_VQA, ModelBlockSwap, ModelBlockSwap]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "euler", "sampler_name": 1.5, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/视频-图生视频自动-wan2.2-Remix-官方_1986620197631098882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986620197631098882.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `easy showAnything`
- `easy imageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `GetNode`
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
- `WanImageToVideo`
- `GetNode`
- `ShowText|pysssss`
- `GetImageSizeAndCount`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `StringFunction|pysssss`
- `StringFunction|pysssss`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `easy positive`
- `WanMoeKSampler` ★核心
- `GetImageSizeAndCount`
- `ImpactFloat`
- `easy int`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `easy positive`
- `easy showAnything`
- `MemoryCleaner`
- `easy anythingIndexSwitch`
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `Reroute`
- `SetNode`
- `MathExpression|pysssss`
- `PrimitiveFloat`
- `easy int`
- `Qwen3_VQA`
- `ModelBlockSwap`
- `ModelBlockSwap`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1.5`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **65%**（44/68）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`PathchSageAttentionKJ`、`ImageFromBatch`、`VAEDecodeTiled`、`INTConstant`、`VHS_VideoCombine`、`WanVideoVACEStartToEndFrame`、`easy seed`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`WanImageToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`ImageFromBatch+`、`StringFunction|pysssss`、`easy positive`、`WanMoeKSampler`、`ImpactFloat`、`easy int`、`MemoryCleaner`、`easy anythingIndexSwitch`、`UNETLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`MathExpression|pysssss`、`Qwen3_VQA`、`ModelBlockSwap`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、easy seed、VAEDecodeTiled
