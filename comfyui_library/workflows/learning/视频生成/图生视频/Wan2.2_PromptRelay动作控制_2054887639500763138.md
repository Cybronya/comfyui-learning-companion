---
key: 视频生成/图生视频/Wan2.2_PromptRelay动作控制_2054887639500763138.json
name: Wan2.2_PromptRelay动作控制_2054887639500763138.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2_PromptRelay动作控制_2054887639500763138.json
hash: 5445cbc3032b0fe3
coverage: 0.95
learned_at: 2026-10-15 22:37:53
nodes: [VAEDecode, ModelSamplingSD3, ModelSamplingSD3, WanImageToVideo, PathchSageAttentionKJ, PromptRelayEncodeTimeline, ConditioningZeroOut, EmptyHunyuanLatentVideo, PromptRelayEncodeTimeline, ImageResizeKJv2, PathchSageAttentionKJ, PrimitiveInt, CLIPLoader, VAELoader, KSamplerAdvanced, VHS_VideoCombine, UNETLoader, UNETLoader, KSamplerAdvanced, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2_PromptRelay动作控制_2054887639500763138.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054887639500763138.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（20 个）：
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `PathchSageAttentionKJ`
- `PromptRelayEncodeTimeline`
- `ConditioningZeroOut`
- `EmptyHunyuanLatentVideo`
- `PromptRelayEncodeTimeline`
- `ImageResizeKJv2`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`VAEDecode`、`ModelSamplingSD3`、`WanImageToVideo`、`PathchSageAttentionKJ`、`PromptRelayEncodeTimeline`、`ConditioningZeroOut`、`EmptyHunyuanLatentVideo`、`ImageResizeKJv2`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`VHS_VideoCombine`、`UNETLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
