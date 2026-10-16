---
key: 视频生成/图生视频/Wan2.2_PromptRelay_2058829735278497793.json
name: Wan2.2_PromptRelay_2058829735278497793.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2058829735278497793.json
hash: fcfcf1039bd07220
coverage: 0.9
learned_at: 2026-10-15 22:38:30
nodes: [VAELoader, CLIPLoader, WanImageToVideo, UNETLoader, UNETLoader, LoadImage, ImageResizeKJv2, PrimitiveNode, PathchSageAttentionKJ, ModelSamplingSD3, EmptyHunyuanLatentVideo, ModelSamplingSD3, ConditioningZeroOut, PromptRelayEncodeTimeline, PromptRelayEncodeTimeline, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2_PromptRelay_2058829735278497793.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058829735278497793.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（20 个）：
- `VAELoader`
- `CLIPLoader`
- `WanImageToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `PrimitiveNode`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `ConditioningZeroOut`
- `PromptRelayEncodeTimeline`
- `PromptRelayEncodeTimeline`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `MarkdownNote`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`VAELoader`、`CLIPLoader`、`WanImageToVideo`、`UNETLoader`、`LoadImage`、`ImageResizeKJv2`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`ConditioningZeroOut`、`PromptRelayEncodeTimeline`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
