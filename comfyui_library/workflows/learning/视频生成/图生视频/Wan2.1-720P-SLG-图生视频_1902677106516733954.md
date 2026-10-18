---
key: 视频生成/图生视频/Wan2.1-720P-SLG-图生视频_1902677106516733954.json
name: Wan2.1-720P-SLG-图生视频_1902677106516733954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1-720P-SLG-图生视频_1902677106516733954.json
hash: 8d0e1394ef668f46
coverage: 0.916667
learned_at: 2026-10-15 22:29:24
nodes: [WanImageToVideo, WanVideoTeaCacheKJ, VAEDecode, CLIPTextEncode, CLIPTextEncode, VHS_VideoCombine, ImageResizeKJ, CLIPVisionEncode, ImpactInt, ImpactInt, PreviewImage, KSampler, WanVideoEnhanceAVideoKJ, SkipLayerGuidanceWanVideo, PathchSageAttentionKJ, ModelSamplingSD3, LoadImage, UNETLoader, CLIPLoader, VAELoader, CLIPVisionLoader, ImpactInt, TorchCompileModelWanVideo, Note]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 161892864946618, "steps": 20}
---

# 视频生成/图生视频/Wan2.1-720P-SLG-图生视频_1902677106516733954.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1902677106516733954.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `WanImageToVideo`
- `WanVideoTeaCacheKJ`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `CLIPVisionEncode`
- `ImpactInt`
- `ImpactInt`
- `PreviewImage`
- `KSampler` ★核心
- `WanVideoEnhanceAVideoKJ`
- `SkipLayerGuidanceWanVideo`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `ImpactInt`
- `TorchCompileModelWanVideo`
- `Note`

## 关键参数

- `seed` = `161892864946618`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`WanImageToVideo`、`WanVideoTeaCacheKJ`、`VAEDecode`、`CLIPTextEncode`、`VHS_VideoCombine`、`ImageResizeKJ`、`CLIPVisionEncode`、`ImpactInt`、`KSampler`、`WanVideoEnhanceAVideoKJ`、`SkipLayerGuidanceWanVideo`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`TorchCompileModelWanVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SkipLayerGuidanceWanVideo
