---
key: 视频生成/图生视频/视频-图生视频双图参考-wan2.2-FFGO-官方_1996837849146302466.json
name: 视频-图生视频双图参考-wan2.2-FFGO-官方_1996837849146302466.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频-图生视频双图参考-wan2.2-FFGO-官方_1996837849146302466.json
hash: 679b8e1ca921ea8f
coverage: 0.710145
learned_at: 2026-10-15 22:33:27
nodes: [SetNode, PathchSageAttentionKJ, GetNode, PathchSageAttentionKJ, INTConstant, WanVideoVACEStartToEndFrame, SetNode, easy seed, CLIPLoader, GetNode, CLIPTextEncode, VAELoader, WanMoeKSampler, GetNode, GetImageSizeAndCount, ImageFromBatch+, StringFunction|pysssss, GetNode, GetNode, PrimitiveFloat, easy showAnything, MemoryCleaner, Reroute, SetNode, SetNode, SetNode, ShowText|pysssss, SetNode, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, ImageFromBatch, GetImageSizeAndCount, MathExpression|pysssss, VAEDecodeTiled, ImageFromBatch+, GetImageSizeAndCount, VHS_VideoCombine, Qwen3_VQA, GetNode, GetImageSizeAndCount, PreviewImage, GetNode, WanImageToVideo, GetImageSizeAndCount, GetImageSizeAndCount, CLIPVisionLoader, CLIPVisionEncode, LoadImage, ImpactFloat, SetNode, LoadImage, easy imageRemBg, StringFunction|pysssss, easy positive, easy int, easy positive, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, PreviewImage, easy positive, easy int, LayerUtility: ImageScaleByAspectRatio V2, ImageStitch, ModelBlockSwap, ModelBlockSwap, easy anythingIndexSwitch]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "sa_solver", "sampler_name": 1.5, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/视频-图生视频双图参考-wan2.2-FFGO-官方_1996837849146302466.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1996837849146302466.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `SetNode`
- `PathchSageAttentionKJ`
- `GetNode`
- `PathchSageAttentionKJ`
- `INTConstant`
- `WanVideoVACEStartToEndFrame`
- `SetNode`
- `easy seed`
- `CLIPLoader`
- `GetNode`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `WanMoeKSampler` ★核心
- `GetNode`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `StringFunction|pysssss`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `easy showAnything`
- `MemoryCleaner`
- `Reroute`
- `SetNode`
- `SetNode`
- `SetNode`
- `ShowText|pysssss`
- `SetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `MathExpression|pysssss`
- `VAEDecodeTiled` ★核心
- `ImageFromBatch+`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `Qwen3_VQA`
- `GetNode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `GetNode`
- `WanImageToVideo`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `LoadImage`
- `ImpactFloat`
- `SetNode`
- `LoadImage`
- `easy imageRemBg`
- `StringFunction|pysssss`
- `easy positive`
- `easy int`
- `easy positive`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `easy positive`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageStitch`
- `ModelBlockSwap`
- `ModelBlockSwap`
- `easy anythingIndexSwitch`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1.5`
- `scheduler` = `1`
- `denoise` = `sa_solver`

## 知识

覆盖率 **71%**（49/69）

**有卡**：`PathchSageAttentionKJ`、`INTConstant`、`WanVideoVACEStartToEndFrame`、`easy seed`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`WanMoeKSampler`、`GetImageSizeAndCount`、`ImageFromBatch+`、`StringFunction|pysssss`、`MemoryCleaner`、`UNETLoader`、`LoraLoaderModelOnly`、`ImageFromBatch`、`MathExpression|pysssss`、`VAEDecodeTiled`、`VHS_VideoCombine`、`Qwen3_VQA`、`WanImageToVideo`、`CLIPVisionLoader`、`CLIPVisionEncode`、`LoadImage`、`ImpactFloat`、`easy imageRemBg`、`easy positive`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageStitch`、`ModelBlockSwap`、`easy anythingIndexSwitch`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、easy seed
