---
key: 平台全量/首尾帧 Wan2.2_RemixV2 次用12.17 浮云_2001171916734033922.json
name: 首尾帧 Wan2.2_RemixV2 次用12.17 浮云_2001171916734033922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/首尾帧 Wan2.2_RemixV2 次用12.17 浮云_2001171916734033922.json
hash: 825dfa89b33f565e
coverage: 0.677966
learned_at: 2026-11-14 02:51:14
nodes: [GetImageSizeAndCount, VAEDecodeTiled, ImageResizeKJ, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, PathchSageAttentionKJ, ImpactFloat, PreviewImage, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, Reroute, WanFirstLastFrameToVideo, SetNode, GetImageSizeAndCount, easy seed, INTConstant, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, easy int, WanMoeKSampler, PathchSageAttentionKJ, UNETLoader, UNETLoader, WanVideoNAG, CLIPVisionLoader, GetImageSizeAndCount, GetImageSizeAndCount, CLIPVisionEncode, CLIPVisionEncode, GetImageSizeAndCount, easy positive, StringFunction|pysssss, MultiplePathsInput, easy showAnything, StringFunction|pysssss, SetNode, GetNode, ImageLoader, ImageLoader, SetNode, easy int, Qwen3_VQA, easy anythingIndexSwitch, easy int, easy positive, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 平台全量/首尾帧 Wan2.2_RemixV2 次用12.17 浮云_2001171916734033922.json

> 来源文件 `comfyui_library/workflows/平台全量/首尾帧 Wan2.2_RemixV2 次用12.17 浮云_2001171916734033922.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `GetImageSizeAndCount`
- `VAEDecodeTiled` ★核心
- `ImageResizeKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `ImpactFloat`
- `PreviewImage`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `Reroute`
- `WanFirstLastFrameToVideo`
- `SetNode`
- `GetImageSizeAndCount`
- `easy seed`
- `INTConstant`
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `WanMoeKSampler` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `WanVideoNAG`
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `GetImageSizeAndCount`
- `easy positive`
- `StringFunction|pysssss`
- `MultiplePathsInput`
- `easy showAnything`
- `StringFunction|pysssss`
- `SetNode`
- `GetNode`
- `ImageLoader`
- `ImageLoader`
- `SetNode`
- `easy int`
- `Qwen3_VQA`
- `easy anythingIndexSwitch`
- `easy int`
- `easy positive`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **68%**（40/59）

**有卡**：`GetImageSizeAndCount`、`VAEDecodeTiled`、`ImageResizeKJ`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`ImpactFloat`、`WanFirstLastFrameToVideo`、`easy seed`、`INTConstant`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`WanMoeKSampler`、`UNETLoader`、`WanVideoNAG`、`CLIPVisionLoader`、`CLIPVisionEncode`、`easy positive`、`StringFunction|pysssss`、`MultiplePathsInput`、`ImageLoader`、`Qwen3_VQA`、`easy anythingIndexSwitch`、`VHS_VideoCombine`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、UNETLoader、easy seed、WanMoeKSampler、CLIPVisionEncode
