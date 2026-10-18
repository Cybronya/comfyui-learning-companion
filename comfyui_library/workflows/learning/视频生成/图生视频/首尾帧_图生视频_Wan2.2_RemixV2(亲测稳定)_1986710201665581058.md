---
key: 视频生成/图生视频/首尾帧_图生视频_Wan2.2_RemixV2(亲测稳定)_1986710201665581058.json
name: 首尾帧_图生视频_Wan2.2_RemixV2(亲测稳定)_1986710201665581058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧_图生视频_Wan2.2_RemixV2(亲测稳定)_1986710201665581058.json
hash: 12f0810bf50655d5
coverage: 0.677966
learned_at: 2026-10-15 22:32:56
nodes: [GetImageSizeAndCount, VAEDecodeTiled, ImageResizeKJ, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, PathchSageAttentionKJ, ImpactFloat, PreviewImage, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, Reroute, WanFirstLastFrameToVideo, easy int, SetNode, GetImageSizeAndCount, easy seed, INTConstant, CLIPLoader, VAELoader, easy int, LayerUtility: ImageScaleByAspectRatio V2, easy int, WanMoeKSampler, PathchSageAttentionKJ, UNETLoader, UNETLoader, WanVideoNAG, easy positive, CLIPVisionLoader, GetImageSizeAndCount, GetImageSizeAndCount, CLIPVisionEncode, CLIPVisionEncode, GetImageSizeAndCount, VHS_VideoCombine, easy positive, StringFunction|pysssss, MultiplePathsInput, Qwen3_VQA, easy anythingIndexSwitch, easy showAnything, StringFunction|pysssss, SetNode, GetNode, SetNode, ImageLoader, ImageLoader]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧_图生视频_Wan2.2_RemixV2(亲测稳定)_1986710201665581058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986710201665581058.json`

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
- `easy int`
- `SetNode`
- `GetImageSizeAndCount`
- `easy seed`
- `INTConstant`
- `CLIPLoader`
- `VAELoader`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `WanMoeKSampler` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `WanVideoNAG`
- `easy positive`
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `easy positive`
- `StringFunction|pysssss`
- `MultiplePathsInput`
- `Qwen3_VQA`
- `easy anythingIndexSwitch`
- `easy showAnything`
- `StringFunction|pysssss`
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageLoader`
- `ImageLoader`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **68%**（40/59）

**有卡**：`GetImageSizeAndCount`、`VAEDecodeTiled`、`ImageResizeKJ`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`ImpactFloat`、`WanFirstLastFrameToVideo`、`easy int`、`easy seed`、`INTConstant`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanMoeKSampler`、`UNETLoader`、`WanVideoNAG`、`easy positive`、`CLIPVisionLoader`、`CLIPVisionEncode`、`VHS_VideoCombine`、`StringFunction|pysssss`、`MultiplePathsInput`、`Qwen3_VQA`、`easy anythingIndexSwitch`、`ImageLoader`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、WanMoeKSampler、easy seed、VAEDecodeTiled
