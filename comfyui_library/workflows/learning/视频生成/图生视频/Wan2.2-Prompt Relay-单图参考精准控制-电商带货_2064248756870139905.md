---
key: 视频生成/图生视频/Wan2.2-Prompt Relay-单图参考精准控制-电商带货_2064248756870139905.json
name: Wan2.2-Prompt Relay-单图参考精准控制-电商带货_2064248756870139905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Prompt Relay-单图参考精准控制-电商带货_2064248756870139905.json
hash: ffa3b6c6f0fd25f4
coverage: 0.884615
learned_at: 2026-10-15 22:39:22
nodes: [VAELoader, CLIPLoader, PathchSageAttentionKJ, UNETLoader, ConditioningZeroOut, WanImageToVideo, UNETLoader, PrimitiveFloat, EmptyHunyuanLatentVideo, VHS_VideoCombine, VHS_VideoCombine, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, ImageResizeKJv2, MarkdownNote, Int, Int, SimpleMath+, Int, LoadImage, PromptRelayEncodeTimeline, PromptRelayEncodeTimeline, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2-Prompt Relay-单图参考精准控制-电商带货_2064248756870139905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064248756870139905.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（26 个）：
- `VAELoader`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `WanImageToVideo`
- `UNETLoader` ★核心
- `PrimitiveFloat`
- `EmptyHunyuanLatentVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `MarkdownNote`
- `Int`
- `Int`
- `SimpleMath+`
- `Int`
- `LoadImage`
- `PromptRelayEncodeTimeline`
- `PromptRelayEncodeTimeline`
- `MarkdownNote`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`VAELoader`、`CLIPLoader`、`PathchSageAttentionKJ`、`UNETLoader`、`ConditioningZeroOut`、`WanImageToVideo`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`ImageResizeKJv2`、`Int`、`SimpleMath+`、`LoadImage`、`PromptRelayEncodeTimeline`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
