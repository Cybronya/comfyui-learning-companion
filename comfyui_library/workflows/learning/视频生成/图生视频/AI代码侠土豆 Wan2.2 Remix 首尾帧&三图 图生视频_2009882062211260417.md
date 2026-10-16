---
key: 视频生成/图生视频/AI代码侠土豆 Wan2.2 Remix 首尾帧&三图 图生视频_2009882062211260417.json
name: AI代码侠土豆 Wan2.2 Remix 首尾帧&三图 图生视频_2009882062211260417.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2009882062211260417.json
hash: f64af7b9bc97b31f
coverage: 0.507937
learned_at: 2026-10-15 22:34:15
nodes: [LoraLoaderModelOnly, SetNode, SetNode, VAELoader, SetNode, SetNode, CLIPTextEncode, SetNode, SetNode, GetNode, GetNode, WanFirstLastFrameToVideo, wanBlock_Swap, VAEDecode, LayerUtility: PurgeVRAM, WanMoeKSampler, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, WanFirstMiddleLastFrameToVideo, GetNode, GetNode, LoadImage, CLIPTextEncode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanMoeKSampler, VAEDecode, VHS_VideoCombine, VHS_VideoCombine, wanBlock_Swap, UNETLoader, UNETLoader, Fast Groups Bypasser (rgthree), LoadImage, easy cleanGpuUsed, LoadImage, easy cleanGpuUsed]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/AI代码侠土豆 Wan2.2 Remix 首尾帧&三图 图生视频_2009882062211260417.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009882062211260417.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（63 个）：
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanFirstLastFrameToVideo`
- `wanBlock_Swap`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `WanMoeKSampler` ★核心
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanFirstMiddleLastFrameToVideo`
- `GetNode`
- `GetNode`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanMoeKSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `wanBlock_Swap`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `easy cleanGpuUsed`
- `LoadImage`
- `easy cleanGpuUsed`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **51%**（32/63）

**有卡**：`LoraLoaderModelOnly`、`VAELoader`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`wanBlock_Swap`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`WanMoeKSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`LoadImage`、`WanFirstMiddleLastFrameToVideo`、`VHS_VideoCombine`、`UNETLoader`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
