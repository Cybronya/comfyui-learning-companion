---
key: 平台全量/wan2.1图生视频带加速版8g显存可用_1909149443008901121.json
name: wan2.1图生视频带加速版8g显存可用_1909149443008901121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1图生视频带加速版8g显存可用_1909149443008901121.json
hash: 6aa9c03fa50955f1
coverage: 1
learned_at: 2026-11-14 01:19:11
nodes: [PathchSageAttentionKJ, CFGGuider, VAELoader, LoadImage, CLIPTextEncode, CLIPVisionLoader, CLIPVisionEncode, SamplerCustomAdvanced, VAEDecodeTiled, ScheduledCFGGuidance, SamplerCustomAdvanced, RandomNoise, VAEDecodeTiled, GetLatentRangeFromBatch, KSamplerSelect, BasicScheduler, SplitSigmas, CLIPTextEncode, ImageScale, VHS_VideoCombine, VHS_VideoCombine, WanImageToVideo, UnetLoaderGGUF, WanVideoTeaCacheKJ, CLIPLoader]
patterns: []
missing: []
---

# 平台全量/wan2.1图生视频带加速版8g显存可用_1909149443008901121.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1图生视频带加速版8g显存可用_1909149443008901121.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `PathchSageAttentionKJ`
- `CFGGuider`
- `VAELoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `ScheduledCFGGuidance`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `GetLatentRangeFromBatch`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SplitSigmas`
- `CLIPTextEncode` ★核心
- `ImageScale`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `UnetLoaderGGUF` ★核心
- `WanVideoTeaCacheKJ`
- `CLIPLoader`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`PathchSageAttentionKJ`、`CFGGuider`、`VAELoader`、`LoadImage`、`CLIPTextEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`ScheduledCFGGuidance`、`RandomNoise`、`GetLatentRangeFromBatch`、`KSamplerSelect`、`BasicScheduler`、`SplitSigmas`、`ImageScale`、`VHS_VideoCombine`、`WanImageToVideo`、`UnetLoaderGGUF`、`WanVideoTeaCacheKJ`、`CLIPLoader`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、ScheduledCFGGuidance
