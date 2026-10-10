---
key: 视频生成/文生视频/wan2.2教学工作流_2003733056534003713.json
name: wan2.2教学工作流_2003733056534003713
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2教学工作流_2003733056534003713.json
hash: bbbdcd883e720b39
coverage: 0.875
learned_at: 2026-10-11 02:57:39
nodes: [CLIPLoader, Int, EmptyHunyuanLatentVideo, CLIPTextEncode, VAELoader, SimpleMath+, ApplySageAttention, ModelSamplingSD3, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, ApplySageAttention, UNETLoader, UNETLoader, LoadImage, CLIPTextEncode, WanFirstLastFrameToVideo, CLIPVisionLoader, CLIPVisionEncode, WanMoeKSampler, ModelSamplingSD3, VAEDecode, VHS_VideoCombine]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+]
parameters: {"cfg": 6, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2教学工作流_2003733056534003713.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2教学工作流_2003733056534003713.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（24 个）：
- `CLIPLoader`
- `Int`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SimpleMath+`
- `ApplySageAttention`
- `ModelSamplingSD3`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionEncode`
- `ApplySageAttention`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `WanMoeKSampler` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`CLIPLoader`、`Int`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`VAELoader`、`ApplySageAttention`、`ModelSamplingSD3`、`LoadImage`、`CLIPVisionEncode`、`UNETLoader`、`WanFirstLastFrameToVideo`、`CLIPVisionLoader`、`WanMoeKSampler`、`VAEDecode`、`VHS_VideoCombine`

**缺卡**（3）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、CLIPVisionEncode

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
