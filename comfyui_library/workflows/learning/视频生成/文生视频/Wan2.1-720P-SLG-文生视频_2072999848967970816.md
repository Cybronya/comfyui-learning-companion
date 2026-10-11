---
key: 视频生成/文生视频/Wan2.1-720P-SLG-文生视频_2072999848967970816.json
name: Wan2.1-720P-SLG-文生视频_2072999848967970816
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1-720P-SLG-文生视频_2072999848967970816.json
hash: 3c7f90e036d5efce
coverage: 0.9375
learned_at: 2026-10-11 20:38:42
nodes: [CLIPLoader, CLIPTextEncode, VAEDecode, KSampler, PathchSageAttentionKJ, ModelSamplingSD3, TorchCompileModelWanVideo, VHS_VideoCombine, WanVideoEnhanceAVideoKJ, CLIPTextEncode, SkipLayerGuidanceWanVideo, Note, VAELoader, UNETLoader, WanVideoTeaCacheKJ, EmptyHunyuanLatentVideo]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 580391778244663, "steps": 30}
---

# 视频生成/文生视频/Wan2.1-720P-SLG-文生视频_2072999848967970816.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.1-720P-SLG-文生视频_2072999848967970816.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（16 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `TorchCompileModelWanVideo`
- `VHS_VideoCombine`
- `WanVideoEnhanceAVideoKJ`
- `CLIPTextEncode` ★核心
- `SkipLayerGuidanceWanVideo`
- `Note`
- `VAELoader`
- `UNETLoader` ★核心
- `WanVideoTeaCacheKJ`
- `EmptyHunyuanLatentVideo`

## 关键参数

- `seed` = `580391778244663`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`TorchCompileModelWanVideo`、`VHS_VideoCombine`、`WanVideoEnhanceAVideoKJ`、`SkipLayerGuidanceWanVideo`、`VAELoader`、`UNETLoader`、`WanVideoTeaCacheKJ`、`EmptyHunyuanLatentVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、SkipLayerGuidanceWanVideo、EmptyHunyuanLatentVideo
